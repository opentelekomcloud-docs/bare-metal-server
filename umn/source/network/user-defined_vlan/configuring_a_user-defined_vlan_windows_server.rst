:original_name: en-us_topic_0095251848.html

.. _en-us_topic_0095251848:

Configuring a User-defined VLAN (Windows Server)
================================================

This section uses Windows Server 2012 R2 Standard as an example to describe how to configure a user-defined VLAN for BMSs.

.. note::

   The configuration methods of other Windows Server OSs are similar to that of Windows Server 2012 R2 Standard.

#. Log in to a Windows BMS.

#. .. _en-us_topic_0095251848__li11441348154412:

   On the Windows PowerShell CLI of the BMS, run the following command to check the NIC information:

   **Get-NetAdapter**

   Information similar to the following is displayed.

   |image1|

   .. note::

      Among the devices, eth0 and eth1 bear the VPC, and eth2 and eth3 bear the user-defined VLAN. The following steps use eth2 and eth3 to configure a user-defined VLAN.

#. .. _en-us_topic_0095251848__li202764020268:

   To improve the outbound traffic on the OS, perform the operations in :ref:`Method 1 <en-us_topic_0095251848__li7981720132719>`. If there is no special requirement on traffic, perform the operations in :ref:`Method 2 <en-us_topic_0095251848__li15395216102810>`.

   -  .. _en-us_topic_0095251848__li7981720132719:

      **Method 1: Use the switch independent mode for the team in the OS. The outbound traffic is distributed across all active NICs, and the inbound traffic is received through one of the NICs in the team.**

   a. Run the following command to create a port group for the user-defined VLAN:

      **New-NetLbfoTeam -Name** *qinq* **-TeamMembers** **"**\ *eth2*\ **","**\ *eth3*\ **"** **-TeamingMode SwitchIndependent -LoadBalancingAlgorithm Dynamic -Confirm:$false**

      |image2|

      .. note::

         In the command, *qinq* is the name of the port group planned for the user-defined VLAN, and *eth2* and *eth3* are the network devices that bear the user-defined VLAN obtained in step :ref:`2 <en-us_topic_0095251848__li11441348154412>`.

   b. Run the following command to query the network adapters:

      **Get-NetLbfoTeamMember**

      |image3|

      **Get-NetAdapter**

      |image4|

   -  .. _en-us_topic_0095251848__li15395216102810:

      **Method 2: Use the active-active mode for the team in the OS.**

   a. .. _en-us_topic_0095251848__li125519380337:

      Run the following command to create a port group for the user-defined VLAN:

      **New-NetLbfoTeam -Name** *Team2* **-TeamMembers** **"**\ *eth2*\ **","**\ *eth3*\ **" -TeamingMode SwitchIndependent -LoadBalancingAlgorithm IPAddresses -Confirm:$false**

      |image5|

      .. note::

         In the command, *Team2* is the name of the port group planned for the user-defined VLAN, and *eth2* and *eth3* are the network devices that bear the user-defined VLAN obtained in step :ref:`2 <en-us_topic_0095251848__li11441348154412>`.

   b. Run the following command to set a network port of port group Team2 created in :ref:`3.a <en-us_topic_0095251848__li125519380337>` to the standby port:

      **Set-NetLbfoTeamMember -Name "**\ *eth2*\ **"** **-AdministrativeMode Standby -Confirm:$false**

      .. note::

         The port group configured for the user-defined VLAN supports only the active/standby mode. *eth2* is one of the ports of the port group. You can determine which port is configured as the standby port based on your planning.

      **get-NetLbfoTeamMember**

      |image6|

      **Get-NetAdapter**

      |image7|

#. .. _en-us_topic_0095251848__li1133314684418:

   Run the following command to enter the **Network Connections** page:

   **ncpa.cpl**

   Then enter the following page.

   |image8|

#. .. _en-us_topic_0095251848__li129292252615:

   Configure a user-defined VLAN.

   a. On the **Network Connections** page, double-click port group **Team2** created in :ref:`3 <en-us_topic_0095251848__li202764020268>` to switch to the **Team2 Status** page.

   b. Click **Next** to switch to the **Team2 Properties** page.

   c. On the **Networking** tab page, double-click **Internet Protocol Version 4 (TCP/IPv4)** to switch to the **Internet Protocol Version 4 (TCP/IPv4) Properties** page.

   d. Select **Use the following IP address**, configure the IP address and subnet mask, and click **OK**.

      |image9|

      .. note::

         If the IP address planned for the user-defined VLAN does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that BMSs communicating through the user-defined VLAN are in the same network segment as the user-defined VLAN.

#. Perform the preceding operations to configure other BMSs.

#. After all BMSs are configured, ping the IP addresses of other BMSs from each BMS.

   |image10|

#. If you want to configure VLAN sub-interfaces to isolate network planes, perform the following operations:

   Run the following command to create a VLAN sub-interface based on the existing Team2:

   **Add-NetLbfoTeamNIC** **-Team** **"Team2"** **-VlanID** *XXX* **-Confirm:$false**

   In the preceding command, **Team2** indicates the bond name, and *XXX* indicates the VLAN ID.

   |image11|

   After the VLAN sub-interface is created, configure the IP address and subnet mask of network port Team2-VLAN 500 by referring to :ref:`4 <en-us_topic_0095251848__li1133314684418>` and :ref:`5 <en-us_topic_0095251848__li129292252615>`.

.. |image1| image:: /_static/images/en-us_image_0143418134.png
.. |image2| image:: /_static/images/en-us_image_0143418429.png
.. |image3| image:: /_static/images/en-us_image_0143418996.png
.. |image4| image:: /_static/images/en-us_image_0143419843.png
.. |image5| image:: /_static/images/en-us_image_0143420306.png
.. |image6| image:: /_static/images/en-us_image_0143419873.png
.. |image7| image:: /_static/images/en-us_image_0143419878.png
.. |image8| image:: /_static/images/en-us_image_0143420818.png
.. |image9| image:: /_static/images/en-us_image_0143420905.png
.. |image10| image:: /_static/images/en-us_image_0143421275.png
.. |image11| image:: /_static/images/en-us_image_0147225511.png
