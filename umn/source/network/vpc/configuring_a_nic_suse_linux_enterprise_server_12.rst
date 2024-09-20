:original_name: en-us_topic_0112777566.html

.. _en-us_topic_0112777566:

Configuring a NIC (SUSE Linux Enterprise Server 12)
===================================================

This section uses SUSE Linux Enterprise Server 12 SP3 (x86_64) as an example to describe how to configure a NIC added to or deleted from a BMS.

.. note::

   If the network is disconnected after a NIC is added and the BMS is restarted, run the following command:

   **/usr/sbin/wicked** **ifup** **bond0.**\ *vlan*

   *vlan* indicates the VLAN used by the NIC.

   If the network is still disconnected, add the NIC again.

Add a NIC
---------

#. .. _en-us_topic_0112777566__li1558174719483:

   Obtain information about the NIC to be added.

   .. table:: **Table 1** NIC information

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                                       | Example Value         |
      +=======================+===================================================================================================================================+=======================+
      | VLAN and MAC address  | Specifies the VLAN information and MAC address of the NIC. To obtain them, perform the following operations:                      | 2835                  |
      |                       |                                                                                                                                   |                       |
      |                       | a. In the BMS list, click the name of the target BMS.                                                                             | fa:16:3e:01:c3:2e     |
      |                       |                                                                                                                                   |                       |
      |                       | b. .. _en-us_topic_0112777566__li58541779231:                                                                                     |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    Click the **NICs** tab, locate the row that contains the NIC to be added, and click |image1| to expand details.                |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Obtain the values of **VLAN** and **MAC Address**.                                                                             |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Gateway               | Specifies the gateway address of the NIC. To obtain them, perform the following operations:                                       | 192.168.1.1           |
      |                       |                                                                                                                                   |                       |
      |                       | a. .. _en-us_topic_0112777566__li32431027104614:                                                                                  |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    On the NIC details page in :ref:`2 <en-us_topic_0112777566__li58541779231>`, obtain the subnet information.                    |                       |
      |                       |                                                                                                                                   |                       |
      |                       | b. On the BMS details page, click the link following **VPC** to switch to the VPC list.                                           |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Click the name of the VPC to which the BMS belongs to go to the VPC details page.                                              |                       |
      |                       |                                                                                                                                   |                       |
      |                       | d. Click the **Subnets** tab and obtain the gateway address of the subnet in :ref:`1 <en-us_topic_0112777566__li32431027104614>`. |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Use a key or password to log in to the BMS as user **root**.

#. Run the following command to copy network configuration file **/etc/sysconfig/network/ifcfg-bond0** to generate file **/etc/sysconfig/network/ifcfg-bond0.**\ *vlan* (replace *vlan* with the VLAN obtained in step :ref:`1 <en-us_topic_0112777566__li1558174719483>`, such as **2835**):

   **cp** **-p** **/etc/sysconfig/network/ifcfg-bond0** **/etc/sysconfig/network/ifcfg-bond0.**\ *2835*

#. Run the following command to edit **/etc/sysconfig/network/ifcfg-bond0.**\ *vlan* and configure the network configuration file of the newly added NIC, such as **ifcfg-bond0.**\ *2835*:

   **vim** **/etc/sysconfig/network/ifcfg-bond0.**\ *2835*

   Edit the file as follows:

   .. code-block::

      STARTMODE=auto
      ETHERDEVICE=bond0
      LLADDR=fa:16:3e:01:c3:2e
      NM_CONTROLLED=no
      BOOTPROTO=dhcp
      DEVICE=bond0.2835
      USERCONTRL=auto
      TYPE=Ethernet
      VLAN_ID=2835

   Where,

   -  **LLADDR**: indicates the MAC address of the NIC to be added. For its value, see :ref:`1 <en-us_topic_0112777566__li1558174719483>`.
   -  **DEVICE**: Set it to **bond0.**\ *vlan*. *vlan* is the value obtained from :ref:`1 <en-us_topic_0112777566__li1558174719483>`, such as **2835**.
   -  **VLAN_ID**: indicates the VLAN ID, such as **2835**.

   After the modification, press **Esc** and enter **:wq** to save the change and exit.

#. Run the following command to start the added NIC:

   **/usr/sbin/wicked** **ifup** **bond0.**\ *vlan*

   For example, to start bond0.2835, run the command shown in the following figure.

   |image2|

#. Run the following command to check the status of the NIC device:

   |image3|

#. Ping the gateway from the new network device to check whether the network connectivity is normal.

   Use the gateway address obtained from :ref:`1 <en-us_topic_0112777566__li1558174719483>`.

   |image4|

Deleting NICs
-------------

#. .. _en-us_topic_0112777566__li960312341080:

   Obtain the VLAN and MAC address of the NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the network device based on the VLAN information and run the **/usr/sbin/wicked ifdown bond0.**\ *vlan* command to delete the device.

   .. code-block::

      serverc7fc560e-24d6-4ad4-9b1e-567a762532c3:~ # ip link | grep 2835
      12: bond0.2835@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default qlen 1000
      serverc7fc560e-24d6-4ad4-9b1e-567a762532c3:~ #
      serverc7fc560e-24d6-4ad4-9b1e-567a762532c3:~ # /usr/sbin/wicked ifdown bond0.2835
      serverc7fc560e-24d6-4ad4-9b1e-567a762532c3:~ #

#. Run the following command to delete network configuration file **/etc/sysconfig/network/ifcfg-bond0.**\ *vlan* (replace *vlan* with the VLAN obtained from :ref:`1 <en-us_topic_0112777566__li960312341080>`, such as **2835**):

   **rm** **/etc/sysconfig/network/ifcfg-bond0.**\ *2835*

#. Run the following command to delete network configuration file **/etc/wicked/ifconfig/bond0.**\ *vlan*\ **.xml** (replace *vlan* with the VLAN obtained from :ref:`1 <en-us_topic_0112777566__li960312341080>`, such as **2835**):

   **rm** **/etc/wicked/ifconfig/bond0.**\ *2835*\ **.xml**

.. |image1| image:: /_static/images/en-us_image_0140752580.png
.. |image2| image:: /_static/images/en-us_image_0140752823.png
.. |image3| image:: /_static/images/en-us_image_0140752825.png
.. |image4| image:: /_static/images/en-us_image_0140752827.png
