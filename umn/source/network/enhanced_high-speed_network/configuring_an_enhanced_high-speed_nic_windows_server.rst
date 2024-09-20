:original_name: en-us_topic_0121593252.html

.. _en-us_topic_0121593252:

Configuring an Enhanced High-Speed NIC (Windows Server)
=======================================================

This section uses Windows Server 2012 R2 Standard as an example to describe how to configure an enhanced high-speed network bond of a BMS.

.. note::

   The configuration methods of other Windows Server OSs are similar to that of Windows Server 2012 R2 Standard.

.. _en-us_topic_0121593252__section136727354194:

Add a NIC
---------

#. Log in to a Windows BMS.

#. .. _en-us_topic_0121593252__li11441348154412:

   On the Windows PowerShell CLI of the BMS, run the following command to check the NIC information:

   **Get-NetAdapter**

   Information similar to the following is displayed.

   |image1|

   .. note::

      eth0 and eth1 bear the VPC, and eth3 and eth4 bear the enhanced high-speed network bond. The following steps use eth2 and eth3 to configure the enhanced high-speed network.

#. .. _en-us_topic_0121593252__li202764020268:

   To improve the outbound traffic on the OS, perform the operations in :ref:`Method 1 <en-us_topic_0121593252__li4677195455>`. If there is no special requirement on traffic, perform the operations in :ref:`Method 2 <en-us_topic_0121593252__li193105239458>`.

   -  .. _en-us_topic_0121593252__li4677195455:

      **Method 1: Use the switch standalone mode for the bond in the OS. The outbound traffic is distributed across all active NICs, and the inbound traffic is received through one of the NICs in the team.**

   a. Run the following command to create a bond port group for the enhanced high-speed network:

      **New-NetLbfoTeam** **-Name** *qinq* **-TeamMembers** **"**\ *eth2*\ **","**\ *eth3*\ **"** **-TeamingMode** **SwitchIndependent** **-LoadBalancingAlgorithm** **Dynamic** **-Confirm:$false**

      |image2|

      .. note::

         In the command, *qinq* is the name of the port group planned for the enhanced high-speed network, and *eth2* and *eth3* are the network devices that bear the enhanced high-speed network obtained in :ref:`2 <en-us_topic_0121593252__li11441348154412>`.

   b. Run the following command to query the network adapters:

      **get-NetLbfoTeamMember**

      |image3|

      **Get-NetAdapter**

      |image4|

   -  .. _en-us_topic_0121593252__li193105239458:

      **Method 2: Use the active/standby mode for the bond in the OS.**

   a. .. _en-us_topic_0121593252__li125519380337:

      Run the following command to create a bond port group for the enhanced high-speed network:

      **New-NetLbfoTeam** **-Name** *Team2* **-TeamMembers** **"**\ *eth2*\ **","**\ *eth3*\ **"** **-TeamingMode** **SwitchIndependent** **-LoadBalancingAlgorithm** **IPAddresses** **-Confirm:$false**

      |image5|

      .. note::

         In the command, *Team2* is the name of the port group planned for the enhanced high-speed network, and *eth2* and *eth3* are the network devices that bear the enhanced high-speed network obtained in :ref:`2 <en-us_topic_0121593252__li11441348154412>`.

   b. Run the following command to set a network port of port group Team2 created in :ref:`3.a <en-us_topic_0121593252__li125519380337>` to the standby port:

      **Set-NetLbfoTeamMember** **-Name** **"**\ *eth3*\ **"** **-AdministrativeMode** **Standby** **-Confirm:$false**

      .. note::

         The port group configured for the enhanced high-speed network supports only the active/standby mode. *eth3* is one of the ports of the port group. You can determine which port is configured as the standby port based on your planning.

      **get-NetLbfoTeamMember**

      |image6|

      **Get-NetAdapter**

      |image7|

#. Run the following command to enter the **Network Connections** page:

   **ncpa.cpl**

   Then enter the following page.

   |image8|

#. Configure the enhanced high-speed network.

   a. On the **Network Connections** page, double-click port group **Team2** created in :ref:`3 <en-us_topic_0121593252__li202764020268>` to switch to the **Team2 Status** page.

   b. Click **Next** to switch to the **Team2 Properties** page.

   c. On the **Networking** tab page, double-click **Internet Protocol Version 4 (TCP/IPv4)** to switch to the **Internet Protocol Version 4 (TCP/IPv4) Properties** page.

   d. Select **Use the following IP address**, configure the IP address and subnet mask, and click **OK**.

      |image9|

      .. note::

         If the IP address planned for the enhanced high-speed network does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that BMSs communicating through the enhanced high-speed network are in the same network segment as the enhanced high-speed network.

#. Perform the preceding operations to configure other BMSs.

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network of other BMSs from each BMS.

   |image10|

.. _en-us_topic_0121593252__section47181835181916:

Delete a NIC
------------

#. Log in to a Windows BMS.

#. On the Windows PowerShell CLI of the BMS, run the following command to query information about the bonded enhanced high-speed NICs to be deleted:

   **Get-NetLbfoTeamNIC** **-Team** **Team2**

   |image11|

#. Run the following command to delete the bonded NICs:

   **Remove-NetLbfoTeam** **-Name** **"Team2"**

   |image12|

#. Run the following commands to query the NIC information and verify that the NIC is deleted:

   **Get-NetAdapter**

   |image13|

.. |image1| image:: /_static/images/en-us_image_0137971700.png
.. |image2| image:: /_static/images/en-us_image_0137971813.png
.. |image3| image:: /_static/images/en-us_image_0137971815.png
.. |image4| image:: /_static/images/en-us_image_0137972005.png
.. |image5| image:: /_static/images/en-us_image_0137971819.png
.. |image6| image:: /_static/images/en-us_image_0137971823.png
.. |image7| image:: /_static/images/en-us_image_0137971825.png
.. |image8| image:: /_static/images/en-us_image_0131348146.png
.. |image9| image:: /_static/images/en-us_image_0131350057.png
.. |image10| image:: /_static/images/en-us_image_0131307619.png
.. |image11| image:: /_static/images/en-us_image_0131402473.png
.. |image12| image:: /_static/images/en-us_image_0131402484.png
.. |image13| image:: /_static/images/en-us_image_0131356351.png
