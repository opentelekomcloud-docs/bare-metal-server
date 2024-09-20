:original_name: en-us_topic_0112778364.html

.. _en-us_topic_0112778364:

Configuring a NIC (Red Hat, CentOS, Oracle Linux, and EulerOS)
==============================================================

This section uses CentOS 6.9 (x86_64) as an example to describe how to configure a NIC added to or deleted from a BMS.

.. note::

   -  The configuration methods of Red Hat, Oracle Linux, EulerOS, and CentOS are similar.

   -  If the network is disconnected after a NIC is added and the BMS is restarted, run the following command:

      **ifup** **bond0.**\ *vlan*

      *vlan* indicates the VLAN used by the NIC.

      If the network is still disconnected, add the NIC again.

Add a NIC
---------

Use a key or password to log in to the BMS as user **root**. Run the following command:

**blkid** **\|** **grep** **config-2**

If the command output is empty, use :ref:`Method 2 <en-us_topic_0112778364__li1229716019264>`. If the command output shown in the following figure is displayed, use :ref:`Method 1 <en-us_topic_0112778364__li1134025893>`.

|image1|

-  .. _en-us_topic_0112778364__li1134025893:

   Method 1

#. .. _en-us_topic_0112778364__li1558174719483:

   Obtain information about the NIC to be added.

   .. table:: **Table 1** NIC information

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                                       | Example Value         |
      +=======================+===================================================================================================================================+=======================+
      | VLAN and MAC address  | Specifies the VLAN information and MAC address of the NIC. To obtain them, perform the following operations:                      | 2838                  |
      |                       |                                                                                                                                   |                       |
      |                       | a. In the BMS list, click the name of the target BMS to enter the BMS details page.                                               | fa:16:3e:1a:fd:5d     |
      |                       |                                                                                                                                   |                       |
      |                       | b. .. _en-us_topic_0112778364__li58541779231:                                                                                     |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    Click the **NICs** tab, locate the row that contains the NIC to be added, and click |image2| to expand details.                |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Obtain the values of **VLAN** and **MAC Address**.                                                                             |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Gateway               | Specifies the gateway address of the NIC. To obtain them, perform the following operations:                                       | 192.168.1.1           |
      |                       |                                                                                                                                   |                       |
      |                       | a. .. _en-us_topic_0112778364__li32431027104614:                                                                                  |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    On the NIC details page in :ref:`2 <en-us_topic_0112778364__li58541779231>`, obtain the subnet information.                    |                       |
      |                       |                                                                                                                                   |                       |
      |                       | b. On the BMS details page, click the link following **VPC** to switch to the VPC list.                                           |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Click the name of the VPC to which the BMS belongs to go to the VPC details page.                                              |                       |
      |                       |                                                                                                                                   |                       |
      |                       | d. Click the **Subnets** tab and obtain the gateway address of the subnet in :ref:`1 <en-us_topic_0112778364__li32431027104614>`. |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Use a key or password to log in to the BMS as user **root**.

#. Run the following command to copy file **/etc/sysconfig/network-scripts/ifcfg-bond0** to generate file **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *vlan* (replace *vlan* with the VLAN obtained in step :ref:`1 <en-us_topic_0112778364__li1558174719483>`, such as **2838**):

   **cp** **-p** **/etc/sysconfig/network-scripts/ifcfg-bond0** **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *2838*

#. Run the following command to edit **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *vlan* and configure the network configuration file of the newly added NIC, such as **ifcfg-bond0.**\ *2838*:

   **vim** **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *2838*

   Edit the file as follows:

   .. code-block::

      MACADDR=fa:16:3e:1a:fd:5d
      USERCTL=no
      PERSISTENT_DHCLIENT=1
      PHYSDEV=bond0
      VLAN=yes
      NM_CONTROLLED=no
      BOOTPROTO=dhcp
      DEVICE=bond0.2838
      TYPE=Ethernet
      ONBOOT=yes

   Descriptions of the parameters are as follows:

   -  **MACADDR**: indicates the MAC address of the NIC to be added. For its value, see step :ref:`1 <en-us_topic_0112778364__li1558174719483>`.
   -  **DEVICE**: Set it to **bond0.**\ *vlan*. *vlan* is the value obtained from :ref:`1 <en-us_topic_0112778364__li1558174719483>`, such as **2838**.

   After the modification, press **Esc** and enter **:wq** to save the change and exit.

#. Run the following command to start the added NIC:

   **ifup** **bond0.**\ *vlan*

   For example, to start bond0.2838, run the command shown in the following figure.

   |image3|

#. Run the following command to check the status of the NIC device:

   |image4|

#. Ping the gateway from the new network device to check whether the network connectivity is normal.

   Use the gateway address obtained from :ref:`1 <en-us_topic_0112778364__li1558174719483>`.

   |image5|

-  .. _en-us_topic_0112778364__li1229716019264:

   Method 2

#. .. _en-us_topic_0112778364__li03837563258:

   Obtain information about the NIC to be added.

   .. table:: **Table 2** NIC information

      +-----------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                        | Example Value         |
      +=======================+====================================================================================================================+=======================+
      | MAC Address           | Specifies the MAC address of the NIC. To obtain them, perform the following operations:                            | fa:16:3e:4e:f7:ae     |
      |                       |                                                                                                                    |                       |
      |                       | a. In the BMS list, click the name of the target BMS.                                                              |                       |
      |                       |                                                                                                                    |                       |
      |                       | b. .. _en-us_topic_0112778364__li938215568256:                                                                     |                       |
      |                       |                                                                                                                    |                       |
      |                       |    Click the **NICs** tab, locate the row that contains the NIC to be added, and click |image6| to expand details. |                       |
      |                       |                                                                                                                    |                       |
      |                       | c. Obtain the MAC address.                                                                                         |                       |
      +-----------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Gateway               | Specifies the gateway address of the NIC. To obtain them, perform the following operations:                        | 192.168.0.1           |
      |                       |                                                                                                                    |                       |
      |                       | a. On the NIC details page in :ref:`2 <en-us_topic_0112778364__li938215568256>`, obtain the subnet information.    |                       |
      |                       | b. On the BMS details page, click the link following **VPC** to switch to the VPC list.                            |                       |
      |                       | c. Click the name of the VPC to which the BMS belongs to go to the VPC details page.                               |                       |
      |                       | d. Click the **Subnets** tab and obtain the gateway address of the subnet.                                         |                       |
      +-----------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------+

#. .. _en-us_topic_0112778364__li738475612259:

   Run the following command to query the name of the NIC whose MAC address is *MACADDR*:

   **ifconfig** **-a** **\|** **grep** *MACADDR* **-B** **1**

   **MACADDR**: indicates the MAC address of the NIC to be added. For its value, see step :ref:`1 <en-us_topic_0112778364__li03837563258>`.

   |image7|

   As shown in the preceding figure, the NIC name is **eth7**.

#. Run the following command to edit the **/etc/sysconfig/network-scripts/ifcfg-eth7** file and configure the network configuration file of the new NIC:

   **vim** **/etc/sysconfig/network-scripts/ifcfg-eth7**

   Edit the file as follows:

   .. code-block::

      DEVICE=eth7
      MACADDR=fa:16:3e:1a:fd:5d
      BOOTPROTO=dhcp
      ONBOOT=yes

   Where,

   -  **MACADDR**: indicates the MAC address of the NIC to be added. For its value, see step :ref:`1 <en-us_topic_0112778364__li03837563258>`.
   -  Set **DEVICE** to the name of the new NIC. For its value, see step :ref:`2 <en-us_topic_0112778364__li738475612259>`.

   After the modification, press **Esc** and enter **:wq** to save the change and exit.

#. Run the following command to start the added NIC:

   **ifup** **eth7**

   For example, to start eth7, run the following command:

   |image8|

#. Run the following command to check the status of the NIC device:

   |image9|

#. Ping the gateway from the new network device to check whether the network connectivity is normal.

   Use the gateway address obtained from :ref:`1 <en-us_topic_0112778364__li03837563258>`.

   |image10|

Delete a NIC
------------

Use a key or password to log in to the BMS as user **root**. Run the following command:

**blkid** **\|** **grep** **config-2**

If the command output is empty, use :ref:`Method 2 <en-us_topic_0112778364__li1861338338>`. If the command output shown in the following figure is displayed, use :ref:`Method 1 <en-us_topic_0112778364__li19639914123211>`.

|image11|

-  .. _en-us_topic_0112778364__li19639914123211:

   Method 1

#. Obtain the VLAN and MAC address of the NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the network device based on the VLAN information and run the following commands to stop and delete the device:

   .. code-block:: console

      [root@host-192-168-0-172 ~]# ip link | grep 2838
      8: bond0.2838@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP
      [root@host-192-168-0-172 ~]# ifconfig bond0.2838 down
      [root@host-192-168-0-172 ~]#
      [root@host-192-168-0-172 ~]# ip link delete bond0.2838
      [root@host-192-168-0-172 ~]#

#. Run the following command to delete network configuration file **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *vlan* (replace *vlan* with the VLAN obtained from :ref:`1 <en-us_topic_0112778364__li1558174719483>`, such as **2838**):

   **rm** **/etc/sysconfig/network-scripts/ifcfg-bond0.**\ *2838*

-  .. _en-us_topic_0112778364__li1861338338:

   Method 2

#. Obtain the VLAN and MAC address of the NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the network device based on the VLAN information and run the following commands to stop and delete the device:

   .. code-block:: console

      [root@bms-197-31 ~]# ip link | grep fa:16:3e:4e:f7:ae -B 1
      9: eth7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
          link/ether fa:16:3e:4e:f7:ae brd ff:ff:ff:ff:ff:ff
      [root@bms-197-31 ~]# ifconfig eth7 down
      [52574.065410] hinic 0000:89:00.0 eth7: [NIC]Netdev is down

#. Run the following command to delete network configuration file **/etc/sysconfig/network-scripts/ifcfg-eth7**:

   **rm** **/etc/sysconfig/network-scripts/ifcfg-eth7**

.. |image1| image:: /_static/images/en-us_image_0170933825.png
.. |image2| image:: /_static/images/en-us_image_0112846498.png
.. |image3| image:: /_static/images/en-us_image_0112853637.png
.. |image4| image:: /_static/images/en-us_image_0112915421.png
.. |image5| image:: /_static/images/en-us_image_0112915510.png
.. |image6| image:: /_static/images/en-us_image_0170933824.png
.. |image7| image:: /_static/images/en-us_image_0171002025.png
.. |image8| image:: /_static/images/en-us_image_0171005796.png
.. |image9| image:: /_static/images/en-us_image_0171006026.png
.. |image10| image:: /_static/images/en-us_image_0171006121.png
.. |image11| image:: /_static/images/en-us_image_0170933823.png
