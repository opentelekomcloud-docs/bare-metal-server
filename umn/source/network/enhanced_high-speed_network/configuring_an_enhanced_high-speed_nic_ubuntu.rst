:original_name: en-us_topic_0121593251.html

.. _en-us_topic_0121593251:

Configuring an Enhanced High-Speed NIC (Ubuntu)
===============================================

This section uses Ubuntu 16.04 LTS (Xenial Xerus x86_64) as an example to describe how to bond enhanced high-speed NICs of a BMS.

.. note::

   The configuration methods of other Ubuntu OSs are similar to that of Ubuntu 16.04 LTS (Xenial Xerus x86_64).

.. _en-us_topic_0121593251__section425191716477:

Add a NIC
---------

#. Use a key or password to log in to the BMS as user **root**.

#. .. _en-us_topic_0121593251__li0616194735713:

   On the BMS CLI, run the following command to check the NIC information:

   **ip** **link**

   Information similar to the following is displayed:

   .. code-block::

      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
          inet 127.0.0.1/8 scope host lo
             valid_lft forever preferred_lft forever
          inet6 ::1/128 scope host
             valid_lft forever preferred_lft forever
      2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
          link/ether fa:16:00:9b:91:c3 brd ff:ff:ff:ff:ff:ff
      3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
          link/ether fa:16:00:9b:91:c3 brd ff:ff:ff:ff:ff:ff
      4: p5p1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
          link/ether 40:7d:0f:52:e4:1d brd ff:ff:ff:ff:ff:ff
      5: p5p2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
          link/ether 40:7d:0f:52:e4:1e brd ff:ff:ff:ff:ff:ff
      6: p4p1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
          link/ether 40:7d:0f:52:e3:a9 brd ff:ff:ff:ff:ff:ff
      7: p4p2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
          link/ether 40:7d:0f:52:e3:aa brd ff:ff:ff:ff:ff:ff
      8: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default qlen 1000
          link/ether fa:16:00:9b:91:c3 brd ff:ff:ff:ff:ff:ff
          inet 192.168.254.85/24 brd 192.168.254.255 scope global bond0
             valid_lft forever preferred_lft forever
          inet6 fe80::f816:ff:fe9b:91c3/64 scope link
             valid_lft forever preferred_lft forever
      9: bond0.3157@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default qlen 1000
          link/ether fa:16:00:9c:1e:79 brd ff:ff:ff:ff:ff:ff
          inet 192.168.100.14/24 brd 192.168.100.255 scope global bond0.3157
             valid_lft forever preferred_lft forever
          inet6 fe80::f816:ff:fe9c:1e79/64 scope link
             valid_lft forever preferred_lft forever
      10: bond0.3159@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default qlen 1000
          link/ether fa:16:00:0a:2e:8e brd ff:ff:ff:ff:ff:ff
          inet 192.168.101.153/24 brd 192.168.101.255 scope global bond0.3159
             valid_lft forever preferred_lft forever
          inet6 fe80::f816:ff:fe0a:2e8e/64 scope link
             valid_lft forever preferred_lft forever

   .. note::

      eth0 and eth1 bear the VPC, and p5p1, p5p2, p4p1, and p4p2 bear the enhanced high-speed network. The following operations describe how to bond enhanced high-speed NICs p4p1 and p4p2.

#. Run the following command to check whether the **/etc/udev/rules.d/** directory contains the **80-persistent-net.rules** file:

   **ll** **/etc/udev/rules.d/** **\|** **grep** **80-persistent-net.rules**

   -  If yes, and the file contains all NICs except **bond0** and **lo** obtained in step :ref:`2 <en-us_topic_0121593251__li0616194735713>` and their MAC addresses, go to step :ref:`6 <en-us_topic_0121593251__li283725272415>`.
   -  If no, go to step :ref:`4 <en-us_topic_0121593251__li116366367312>`.

#. .. _en-us_topic_0121593251__li116366367312:

   Run the following command to copy the **/etc/udev/rules.d/70-persistent-net.rules** file and name the copy as **/etc/udev/rules.d/80-persistent-net.rules**.

   **cp** **-p** **/etc/udev/rules.d/70-persistent-net.rules** **/etc/udev/rules.d/80-persistent-net.rules**

#. Configure the udev rules:

   Add the NICs and their MAC addresses obtained in step :ref:`2 <en-us_topic_0121593251__li0616194735713>`, except **lo**, **eth0**, **eth1**, and **bond0**, to the **/etc/udev/rules.d/80-persistent-net.rules** file. This ensures that the names and sequence of NICs will not change after the BMS is restarted.

   .. note::

      Ensure that NIC MAC address and name are lowercase letters.

   **vim** **/etc/udev/rules.d/80-persistent-net.rules**

   The modification result is as follows:

   .. code-block::

      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="f4:4c:7f:5d:b6:fc", NAME="eth0"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="f4:4c:7f:5d:b6:fd", NAME="eth1"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e4:1d", NAME="p5p1"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e4:1e", NAME="p5p2"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e3:a9", NAME="p4p1"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e3:aa", NAME="p4p2"

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. .. _en-us_topic_0121593251__li283725272415:

   Run the following command to copy the **/etc/network/interfaces.d/50-cloud-init.cfg** file to generate the **/etc/network/interfaces.d/60-cloud-init.cfg** file:

   **cp** **-p** **/etc/network/interfaces.d/50-cloud-init.cfg** **/etc/network/interfaces.d/60-cloud-init.cfg**

   .. note::

      If the **/etc/network/interfaces.d/50-cloud-init.cfg** file does not exist, copy the **/etc/network/interfaces** file and run the following commands:

      **mkdir** **/etc/network/interfaces.d**

      **cp** **-p** **/etc/network/interfaces** **/etc/network/interfaces.d/60-cloud-init.cfg**

#. Run the following command to edit the **/etc/network/interfaces.d/60-cloud-init.cfg** file of devices **p4p1** and **p4p2**:

   **vim** **/etc/network/interfaces.d/60-cloud-init.cfg**

   Edit the file as follows:

   .. code-block::

      auto p4p1
      iface p4p1 inet manual
      bond_mode 1
      bond-master bond1
      bond_miimon 100
      mtu 8888

      auto p4p2
      iface p4p2 inet manual
      bond_mode 1
      bond-master bond1
      bond_miimon 100
      mtu 8888

      auto bond1
      iface bond1 inet static
      bond_miimon 100
      bond-slaves none
      bond_mode 1
      address 10.10.10.103
      netmask 255.255.255.0
      hwaddress 40:7d:0f:52:e3:a9
      mtu 8888

   Parameters are as follows:

   -  **p4p1** and **p4p2** are the names of the NICs that carry the enhanced high-speed network.
   -  **hwaddress** is the MAC address of p4p1.
   -  Change the value of **address** to the IP address allocated to enhanced high-speed network bond1. If the IP address planned for the enhanced high-speed network does not conflict with the VPC network segment, you can plan the IP address as needed, only to ensure that BMSs communicating through the enhanced high-speed network are in the same network segment as the enhanced high-speed network.
   -  Set the value of **netmask** to the subnet mask of the IP address configured for enhanced high-speed network bond1.

   Set values of other parameters. For example, set **mtu** to **8888**, **bond_miimon** to **100**, and **bond_mode** to **1**.

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. Run the following command to enable the bond NIC:

   **ifup** *p4p1*

   **ifup** *p4p2*

   .. note::

      **p4p1** and **p4p2** are the NICs bearing the enhanced high-speed network.

#. Run the following commands to check the NIC device status and whether the **bond1** configuration file takes effect:

   **ip** **link**

   |image1|

   **ifconfig**

   |image2|

#. Perform the preceding operations to configure other BMSs.

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network of other BMSs from each BMS.

   For example, run the **ping** **10.10.10.102** command. The command output is as follows:

   .. code-block:: console

      [root@bms-ubuntu ~]# ping 10.10.10.102 -I bond1
      PING 10.10.10.102 (10.10.10.102) from 10.10.10.103 bond1: 56(84) bytes of data.
      64 bytes from 10.10.10.102: icmp_seq=1 ttl=64 time=0.681 ms
      64 bytes from 10.10.10.102: icmp_seq=2 ttl=64 time=0.035 ms
      64 bytes from 10.10.10.102: icmp_seq=3 ttl=64 time=0.031 ms
      64 bytes from 10.10.10.102: icmp_seq=4 ttl=64 time=0.030 ms
      ^C
      --- 10.10.10.102 ping statistics ---
      4 packets transmitted, 4 received, 0% packet loss, time 3342ms

**To configure a VLAN, perform the following steps:**

#. Configure the corresponding VLAN sub-interfaces based on the VLAN to be configured. Assuming that the VLAN ID is 316, run the following command to edit the **/etc/network/interfaces.d/60-cloud-init.cfg** file:

   **vim** **/etc/network/interfaces.d/60-cloud-init.cfg**

   Edit the file as follows:

   .. code-block::

      auto p4p1
      iface p4p1 inet manual
      bond_mode 1
      bond-master bond1
      bond_miimon 100
      mtu 8888

      auto p4p2
      iface p4p2 inet manual
      bond_mode 1
      bond-master bond1
      bond_miimon 100
      mtu 8888

      auto bond1
      iface bond1 inet static
      bond_miimon 100
      bond-slaves none
      bond_mode 1
      address 10.10.10.103
      netmask 255.255.255.0
      hwaddress 40:7d:0f:52:e3:a9
      mtu 8888

      auto bond1.316
      iface bond1.316 inet static
      bond_miimon 100
      bond-slaves none
      bond_mode 1
      address 10.10.0.103
      netmask 255.255.255.0
      hwaddress 40:7d:0f:52:e3:a9
      mtu 8888

#. Run the following command to enable the VLAN sub-interface of the bond NIC:

   **ifup** *bond1.316*

#. After all BMSs are configured, ping the IP address in the same network segment as the enhanced high-speed network VLAN sub-interface of other BMSs from each BMS.

   |image3|

.. _en-us_topic_0121593251__section17427175114209:

Delete a NIC
------------

#. Obtain the IP address of the bonded enhanced high-speed NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the bond network device and run the following command to stop and delete the device: If the bond has VLAN sub-interfaces, they will be automatically deleted.

   .. code-block:: console

      [root@bms-ubuntu ~]# ifdown p4p1
      [root@bms-ubuntu ~]# ifdown p4p2
      [root@bms-ubuntu ~]# ifdown bond1

#. Run the following command to delete network configuration file **/etc/network/interfaces.d/60-cloud-init.cfg**:

   **rm** **-f** **/etc/network/interfaces.d/60-cloud-init.cfg**

.. |image1| image:: /_static/images/en-us_image_0131402408.png
.. |image2| image:: /_static/images/en-us_image_0131402410.png
.. |image3| image:: /_static/images/en-us_image_0131402379.png
