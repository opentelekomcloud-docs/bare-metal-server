:original_name: en-us_topic_0121593250.html

.. _en-us_topic_0121593250:

Configuring an Enhanced High-Speed NIC (Red Hat, CentOS, Oracle Linux, and EulerOS)
===================================================================================

This section uses CentOS 6.9 (x86_64) as an example to describe how to configure an enhanced high-speed NIC of a BMS.

.. note::

   The configuration methods of Red Hat, Oracle Linux, EulerOS, and CentOS are similar.

.. _en-us_topic_0121593250__section16410175114208:

Add a NIC
---------

Use a key or password to log in to the BMS as user **root**. Run the following command:

**blkid** **\|** **grep** **config-2**

If the command output is empty, use :ref:`Method 2 <en-us_topic_0121593250__li20529112891117>`. If the command output shown in the following figure is displayed, use :ref:`Method 1 <en-us_topic_0121593250__li1134025893>`.

|image1|

-  .. _en-us_topic_0121593250__li1134025893:

   Method 1

#. Use a key or password to log in to the BMS as user **root**.

#. .. _en-us_topic_0121593250__li0616194735713:

   On the BMS CLI, run the following command to check the NIC information:

   **ip** **link**

   Information similar to the following is displayed.

   |image2|

   .. note::

      eth0 and eth1 bear the VPC, and eth2 and eth3 bear the enhanced high-speed network.

#. Run the following command to check whether the **/etc/udev/rules.d/** directory contains the **80-persistent-net.rules** file:

   **ll** **/etc/udev/rules.d/** **\|** **grep** **80-persistent-net.rules**

   -  If yes, and the file contains all NICs except **bond0** and **lo** obtained in step :ref:`2 <en-us_topic_0121593250__li0616194735713>` and their MAC addresses, go to step :ref:`6 <en-us_topic_0121593250__li1437634425719>`.
   -  If no, go to step :ref:`4 <en-us_topic_0121593250__li116366367312>`.

#. .. _en-us_topic_0121593250__li116366367312:

   Run the following command to copy the **/etc/udev/rules.d/70-persistent-net.rules** file and name the copy as **/etc/udev/rules.d/80-persistent-net.rules**.

   **cp** **-p** **/etc/udev/rules.d/70-persistent-net.rules** **/etc/udev/rules.d/80-persistent-net.rules**

   .. note::

      If the **/etc/udev/rules.d/70-persistent-net.rules** file does not exist, create it with the content in the following format:

      .. code-block::

         SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="4c:f9:5d:d9:e8:ac", NAME="eth0"
         SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="4c:f9:5d:d9:e8:ad", NAME="eth1"

#. Configure the udev rules:

   Write the MAC addresses and names of NICs except eth0 and eth1 obtained in step :ref:`2 <en-us_topic_0121593250__li0616194735713>` (those not contained in the **/etc/udev/rules.d/70-persistent-net.rules** file) to the **/etc/udev/rules.d/80-persistent-net.rules** file so that the names and sequence of NICs do not change after the BMS is restarted.

   .. note::

      Ensure that NIC MAC address and name are lowercase letters.

   **vi** **/etc/udev/rules.d/80-persistent-net.rules**

   The modification result is as follows:

   |image3|

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. .. _en-us_topic_0121593250__li1437634425719:

   Run the following commands to copy the network configuration file **/etc/sysconfig/network-scripts/ifcfg-bond0** to generate the **/etc/sysconfig/network-scripts/ifcfg-bond1** file, and copy the **/etc/sysconfig/network-scripts/ifcfg-eth0** file to generate the **/etc/sysconfig/network-scripts/ifcfg-eth2** and **/etc/sysconfig/network/ ifcfg-eth3** files:

   **cp** **-p** **/etc/sysconfig/network-scripts/ifcfg-bond0** **/etc/sysconfig/network-scripts/ifcfg-bond1**

   **cp** **-p** **/etc/sysconfig/network-scripts/ifcfg-eth0** **/etc/sysconfig/network-scripts/ifcfg-eth2**

   **cp** **-p** **/etc/sysconfig/network-scripts/ifcfg-eth0** **/etc/sysconfig/network-scripts/ifcfg-eth3**

#. Run the following commands to edit the **/etc/sysconfig/network-scripts/ifcfg-eth2** and **/etc/sysconfig/network-scripts/ifcfg-eth3** files:

   -  **vi** **/etc/sysconfig/network-scripts/ifcfg-eth2**

      Edit the eth2 network configuration file as follows:

      .. code-block::

         USERCTL=no
         MTU=8888
         NM_CONTROLLED=no
         BOOTPROTO=static
         DEVICE=eth2
         TYPE=Ethernet
         ONBOOT=yes
         MASTER=bond1
         SLAVE=yes

      Change the value of **BOOTPROTO** to **static**, that of **DEVICE** to the network device name **eth2**, and that of **MASTER** to the port name of the enhanced high-speed NIC bond (**bond1**). Retain values of other parameters.

   -  **vi** **/etc/sysconfig/network-scripts/ifcfg-eth3**

      Edit the eth3 network configuration file as follows (similar to eth2):

      .. code-block::

         USERCTL=no
         MTU=8888
         NM_CONTROLLED=no
         BOOTPROTO=static
         DEVICE=eth3
         TYPE=Ethernet
         ONBOOT=yes
         MASTER=bond1
         SLAVE=yes

#. Run the following command to edit the **/etc/sysconfig/network-scripts/ifcfg-bond1** file:

   **vi** **/etc/sysconfig/network-scripts/ifcfg-bond1**

   Edit the file as follows:

   .. code-block::

      MACADDR=40:7d:0f:52:e3:a5
      BONDING_MASTER=yes
      USERCTL=no
      ONBOOT=yes
      NM_CONTROLLED=no
      BOOTPROTO=static
      BONDING_OPTS="mode=1 miimon=100"
      DEVICE=bond1
      TYPE=Bond
      IPADDR=10.10.10.101
      NETMASK=255.255.255.0
      MTU=8888

   Where,

   -  Change the value of **MACADDR** to the MAC address of eth2 or eth3.
   -  Change the value of **BOOTPROTO** to **static**.
   -  Change the value of **DEVICE** to **bond1**.
   -  Change the value of **IPADDR** to the IP address to be allocated to bond1. If the IP address planned for the enhanced high-speed network does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that BMSs communicating through the enhanced high-speed network are in the same network segment as the enhanced high-speed network. An example value is **10.10.10.101**.
   -  Set the value of **NETMASK** to the subnet mask of the IP address configured for enhanced high-speed network bond1.

   Retain values of other parameters.

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. Run the following commands to enable port group bond1 of the enhanced high-speed network:

   Run the following commands to start enhanced high-speed NICs eth2 and eth3:

   **ifup** *eth2*

   **ifup** *eth3*

   **ifup** *bond1*

   |image4|

#. Perform the preceding operations to configure other BMSs.

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network of other BMSs from each BMS.

   |image5|

-  .. _en-us_topic_0121593250__li20529112891117:

   Method 2

#. Use a key or password to log in to the BMS as user **root**.

#. On the BMS CLI, run the following command to check the NIC information:

   **ip** **link**

   Information similar to the following is displayed.

   |image6|

   .. note::

      The NIC whose MAC address starts with **fa:16** is a network device that carries the VPC network, for example, eth0 and eth1. The NIC whose MAC address is that displayed in :ref:`View Enhanced High-Speed NICs <en-us_topic_0170795327__section362012041417>` is a network device that carries the enhanced high-speed network, such as eth6 and eth7.

#. Run the following commands to edit the **/etc/sysconfig/network-scripts/ifcfg-eth6** and **/etc/sysconfig/network-scripts/ifcfg-eth7** files:

   -  **vi** **/etc/sysconfig/network-scripts/ifcfg-eth6**

      Edit the eth6 network configuration file as follows:

      .. code-block::

         USERCTL=no
         MTU=8888
         NM_CONTROLLED=no
         BOOTPROTO=static
         DEVICE=eth6
         TYPE=Ethernet
         ONBOOT=yes
         MASTER=bond1
         SLAVE=yes

      Change the value of **BOOTPROTO** to **static**, that of **DEVICE** to the network device name **eth6**, and that of **MASTER** to the port name of the enhanced high-speed NIC bond (**bond1**). Retain values of other parameters.

   -  **vi** **/etc/sysconfig/network-scripts/ifcfg-eth7**

      Edit the eth7 network configuration file as follows (similar to eth6):

      .. code-block::

         USERCTL=no
         MTU=8888
         NM_CONTROLLED=no
         BOOTPROTO=static
         DEVICE=eth7
         TYPE=Ethernet
         ONBOOT=yes
         MASTER=bond1
         SLAVE=yes

#. Run the following command to edit the **/etc/sysconfig/network-scripts/ifcfg-bond1** file:

   **vi** **/etc/sysconfig/network-scripts/ifcfg-bond1**

   Edit the file as follows:

   .. code-block::

      MACADDR=00:2e:c7:e0:b2:37
      BONDING_MASTER=yes
      USERCTL=no
      ONBOOT=yes
      NM_CONTROLLED=no
      BOOTPROTO=static
      BONDING_OPTS="mode=1 miimon=100"
      DEVICE=bond1
      TYPE=Bond
      IPADDR=10.10.10.101
      NETMASK=255.255.255.0
      MTU=8888

   Where,

   -  Change the value of **MACADDR** to the MAC address of eth6 or eth7.
   -  Change the value of **BOOTPROTO** to **static**.
   -  Change the value of **DEVICE** to **bond1**.
   -  Change the value of **IPADDR** to the IP address to be allocated to bond1. If the IP address planned for the enhanced high-speed network does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that BMSs communicating through the enhanced high-speed network are in the same network segment as the enhanced high-speed network. An example value is **10.10.10.101**.
   -  Set the value of **NETMASK** to the subnet mask of the IP address configured for enhanced high-speed network bond1.

   Retain values of other parameters.

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. Run the following commands to enable port group bond1 of the enhanced high-speed network:

   Run the following commands to start enhanced high-speed NICs eth6 and eth7:

   **ifup** *eth6*

   **ifup** *eth7*

   **ifup** *bond1*

   |image7|

#. Perform the preceding operations to configure other BMSs.

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network of other BMSs from each BMS.

   |image8|

**To configure a VLAN, perform the following steps:**

#. Configure the corresponding VLAN sub-interfaces based on the VLAN to be configured. Assuming that the VLAN ID is 316, run the following command to edit the **/etc/sysconfig/network-scripts/ifcfg-bond1.316** file:

   **vi** **/etc/sysconfig/network-scripts/ifcfg-bond1.316**

   Edit the file as follows:

   .. code-block::

      USERCTL=no
      ONBOOT=yes
      NM_CONTROLLED=no
      BOOTPROTO=static
      DEVICE=bond1.316
      TYPE=Ethernet
      IPADDR=10.10.0.101
      NETMASK=255.255.255.0
      VLAN=yes
      PHYSDEV=bond1

   Where,

   -  Change the value of **DEVICE** to the name of the new bond sub-interface.
   -  Change the value of **IPADDR** to the IP address to be allocated to bond1.316. If the IP address planned for the VLAN sub-interface of the enhanced high-speed NIC does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that the BMSs communicating with each other through the VLAN sub-interface of the enhanced high-speed NIC are in the same network segment as the VLAN sub-interface of the enhanced high-speed NIC. An example value is **10.10.0.101**.
   -  Set the value of **NETMASK** to the subnet mask of the IP address configured for enhanced high-speed NIC bond1.316.

   Retain values of other parameters.

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network VLAN sub-interface of other BMSs from each BMS.

   |image9|

.. _en-us_topic_0121593250__section17427175114209:

Delete a NIC
------------

#. Obtain the IP address of the bonded enhanced high-speed NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the bond network device and run the following command to stop and delete the device: If the bond has VLAN sub-interfaces, they will be automatically deleted.

   .. code-block:: console

      [root@bms-centos ~]# ifdown eth2
      [root@bms-centos ~]# ifdown eth3
      [root@bms-centos ~]# ifdown bond1
      [root@bms-centos ~]# ip link delete bond1
      [root@bms-centos ~]# ip link
      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP qlen 1000
          link/ether fa:16:00:6d:80:29 brd ff:ff:ff:ff:ff:ff
      3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP qlen 1000
          link/ether fa:16:00:6d:80:29 brd ff:ff:ff:ff:ff:ff
      4: eth2: <BROADCAST,MULTICAST> mtu 8888 qdisc mq state DOWN qlen 1000
          link/ether 40:7d:0f:52:e3:a5 brd ff:ff:ff:ff:ff:ff
      5: eth3: <BROADCAST,MULTICAST> mtu 8888 qdisc mq state DOWN qlen 1000
          link/ether 40:7d:0f:52:e3:a6 brd ff:ff:ff:ff:ff:ff
      6: bond0: <BROADCAST,MULTICAST,PROMISC,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP
          link/ether fa:16:00:6d:80:29 brd ff:ff:ff:ff:ff:ff

#. Run the following commands to delete network configuration files **/etc/sysconfig/network-scripts/ifcfg-eth2**, **/etc/sysconfig/network-scripts/ifcfg-eth3**, and **/etc/sysconfig/network-scripts/ifcfg-bond1**:

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-eth2**

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-eth3**

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-bond1**

   If a VLAN sub-interface exists, delete network configuration file **/etc/sysconfig/network-scripts/ifcfg-bond1.**\ *vlan*, where *vlan* indicates the VLAN ID of the VLAN sub-interface, for example, **316**.

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-bond1.**\ *316*

.. |image1| image:: /_static/images/en-us_image_0163473278.png
.. |image2| image:: /_static/images/en-us_image_0131401776.png
.. |image3| image:: /_static/images/en-us_image_0131401809.png
.. |image4| image:: /_static/images/en-us_image_0131402211.png
.. |image5| image:: /_static/images/en-us_image_0131402230.png
.. |image6| image:: /_static/images/en-us_image_0163473355.png
.. |image7| image:: /_static/images/en-us_image_0163357540.png
.. |image8| image:: /_static/images/en-us_image_0163357561.png
.. |image9| image:: /_static/images/en-us_image_0131402253.png
