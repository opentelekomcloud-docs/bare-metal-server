:original_name: en-us_topic_0112790034.html

.. _en-us_topic_0112790034:

Configuring a NIC (Windows Server)
==================================

This section uses Windows Server 2012 R2 Standard as an example to describe how to configure a NIC added to or deleted from a BMS.

.. note::

   -  The configuration methods of other Windows Server OSs are similar to that of Windows Server 2012 R2 Standard.
   -  If the network is still disconnected after the NIC is added and the BMS is restarted, add the NIC again.

Add a NIC
---------

#. .. _en-us_topic_0112790034__li1558174719483:

   Obtain information about the NIC to be added.

   .. table:: **Table 1** NIC information

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                                       | Example Value         |
      +=======================+===================================================================================================================================+=======================+
      | VLAN and MAC address  | Specifies the VLAN information and MAC address of the NIC. To obtain them, perform the following operations:                      | 2812                  |
      |                       |                                                                                                                                   |                       |
      |                       | a. In the BMS list, click the name of the target BMS.                                                                             | fa:16:3e:15:38:07     |
      |                       |                                                                                                                                   |                       |
      |                       | b. .. _en-us_topic_0112790034__li58541779231:                                                                                     |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    Click the **NICs** tab, locate the row that contains the NIC to be added, and click |image1| to expand details.                |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Obtain the values of **VLAN** and **MAC Address**.                                                                             |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Gateway               | Specifies the gateway address of the NIC. To obtain them, perform the following operations:                                       | 192.168.1.1           |
      |                       |                                                                                                                                   |                       |
      |                       | a. .. _en-us_topic_0112790034__li32431027104614:                                                                                  |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    On the NIC details page in :ref:`2 <en-us_topic_0112790034__li58541779231>`, obtain the subnet information.                    |                       |
      |                       |                                                                                                                                   |                       |
      |                       | b. On the BMS details page, click the link following **VPC** to switch to the VPC list.                                           |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Click the name of the VPC to which the BMS belongs to go to the VPC details page.                                              |                       |
      |                       |                                                                                                                                   |                       |
      |                       | d. Click the **Subnets** tab and obtain the gateway address of the subnet in :ref:`1 <en-us_topic_0112790034__li32431027104614>`. |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Log in to a Windows BMS.

#. On the Windows PowerShell CLI of the BMS, run the following command to check whether the NIC information contains **Team1** (port group name of the VPC):

   **Get-NetAdapter**

   -  If yes, go to step :ref:`4 <en-us_topic_0112790034__li27700107517>`.
   -  If no, contact the customer service.

   Information similar to the following is displayed.

   |image2|

   .. note::

      **eth0** and **eth1** are the network devices that carry the VPC.

#. .. _en-us_topic_0112790034__li27700107517:

   Run the following commands to add the NIC:

   **Add-NetLbfoTeamNIC** **-Team** **"Team1"** **-VlanID** *vlan_id* **-Name** **"Team1-vlan-**\ *vlan_id*\ **"** **-Confirm:$false**

   **Set-NetAdapter** **-Name** **"Team1-vlan-**\ *vlan_id*\ **"** **-MacAddress** **"mac_addr"** **-Confirm:$false**

   In the preceding command, **Team1** is the port group name of the VPC, **vlan_id** is the VLAN information obtained in step :ref:`1 <en-us_topic_0112790034__li1558174719483>` (such as **2812**), and **mac_addr** is the MAC address obtained in step :ref:`1 <en-us_topic_0112790034__li1558174719483>` (such as **fa:16:3e:15:38:07**).

   |image3|

#. Run the following command to check the status of the NIC device:

   **Get-NetAdapter**

   Information similar to the following is displayed.

   |image4|

#. Ping the gateway from the new network device to check whether the network connectivity is normal.

   The IPv4 address of the added network device **Team1-vlan-2812** is that shown in the red box in the following figure.

   |image5|

   Use the gateway address obtained from step :ref:`1 <en-us_topic_0112790034__li1558174719483>`.

   Information similar to the following is displayed.

   |image6|

Delete a NIC
------------

#. .. _en-us_topic_0112790034__li960312341080:

   Obtain the VLAN and MAC address of the NIC to be deleted.

#. Log in to a Windows BMS.

#. On the Windows PowerShell CLI of the BMS, run the following command to check information about the NIC to be added:

   **Get-NetLbfoTeamNIC** **-Team** **Team1**

   |image7|

#. Run the following command to delete the NIC:

   **Remove-NetLbfoTeamNIC** **-Team** **"Team1"** **-VlanID** *vlan_id*

   In the command, *vlan_id* indicates the VLAN information obtained in step :ref:`1 <en-us_topic_0112790034__li960312341080>`.

   |image8|

#. Run the following commands to query the NIC information and verify that the NIC is deleted:

   **Get-NetLbfoTeamNIC** **-Team** **Team1**

   **Get-NetAdapter**

   |image9|

.. |image1| image:: /_static/images/en-us_image_0112918070.png
.. |image2| image:: /_static/images/en-us_image_0113093166.png
.. |image3| image:: /_static/images/en-us_image_0113093405.png
.. |image4| image:: /_static/images/en-us_image_0113096480.png
.. |image5| image:: /_static/images/en-us_image_0113099288.png
.. |image6| image:: /_static/images/en-us_image_0113099330.png
.. |image7| image:: /_static/images/en-us_image_0113100398.png
.. |image8| image:: /_static/images/en-us_image_0113100585.png
.. |image9| image:: /_static/images/en-us_image_0113102174.png
