:original_name: en-us_topic_0121593247.html

.. _en-us_topic_0121593247:

Configuring an Enhanced High-Speed NIC (SUSE Linux Enterprise Server 12)
========================================================================

This section uses SUSE Linux Enterprise Server 12 SP3 (x86_64) as an example to describe how to configure an enhanced high-speed NIC of a BMS, including the configuration for adding and deleting a NIC.

Add a NIC
---------

.. note::

   For details about how to add a NIC in other OSs, see:

   -  :ref:`Add a NIC in SUSE Linux Enterprise Server 11 <en-us_topic_0121593249__section9801122916212>`
   -  :ref:`Add a NIC in Red Hat, CentOS, Oracle Linux, and EulerOS <en-us_topic_0121593250__section16410175114208>`
   -  :ref:`Add a NIC in Ubuntu <en-us_topic_0121593251__section425191716477>`
   -  :ref:`Add a NIC in Windows Server <en-us_topic_0121593252__section136727354194>`

#. Use a key or password to log in to the BMS as user **root**.

#. .. _en-us_topic_0121593247__li14997248288:

   On the BMS CLI, run the following command to check the NIC information:

   **ip** **link**

   Information similar to the following is displayed:

   .. code-block::

      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff
      3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff
      4: eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
          link/ether 40:7d:0f:52:e3:a5 brd ff:ff:ff:ff:ff:ff
      5: eth3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
          link/ether 40:7d:0f:52:e3:a6 brd ff:ff:ff:ff:ff:ff
      6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff

   .. note::

      eth0 and eth1 bear the VPC, and eth2 and eth3 bear the enhanced high-speed network.

#. Configure the udev rules:

   Run the following command to create the **80-persistent-net.rules** file:

   **cp** **/etc/udev/rules.d/70-persistent-net.rules** **/etc/udev/rules.d/80-persistent-net.rules**

   Write the NIC MAC address and name that are queried in :ref:`2 <en-us_topic_0121593247__li14997248288>` and that are not displayed in **80-persistent-net.rules** to the file. In this way, after the BMS is restarted, the NIC name and sequence will not change.

   .. note::

      Ensure that the NIC MAC address and name are lowercase letters.

   **vim** **/etc/udev/rules.d/80-persistent-net.rules**

   The modification result is as follows:

   .. code-block::

      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="f4:4c:7f:5d:b7:2a", NAME="eth0"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="f4:4c:7f:5d:b7:2b", NAME="eth1"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e3:a5", NAME="eth2"
      SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="40:7d:0f:52:e3:a6", NAME="eth3"

#. Run the following commands to create configuration files for NICs eth2 and eth3 (you can quickly create the files by copying existing NIC configuration files):

   **cd** **/etc/sysconfig/network**

   **cp** **ifcfg-eth0** **ifcfg-eth2**

   **cp** **ifcfg-eth1** **ifcfg-eth3**

   Run the following commands to modify the configuration files of NICs eth2 and eth3:

   **vi** **ifcfg-eth2**

   Modified configuration file of NIC eth2 is as follows.

   .. code-block::

      STARTMODE=auto
      MTU=8888
      NM_CONTROLLED=no
      BOOTPROTO=STATIC
      DEVICE=eth2
      USERCONTRL=no
      LLADDR=40:7d:0f:52:e3:a5
      TYPE=Ethernet

   .. note::

      In this configuration file, set **MTU** to **8888**, **BOOTPROTO** to **STATIC**, and configure **DEVICE** and **LLADDR** as required.

   **vi** **ifcfg-eth3**

   Modified configuration file of NIC eth3 is as follows:

   .. code-block::

      STARTMODE=auto
      MTU=8888
      NM_CONTROLLED=no
      BOOTPROTO=STATIC
      DEVICE=eth3
      USERCONTRL=no
      LLADDR=40:7d:0f:52:e3:a6
      TYPE=Ethernet

   After the modification, save the change and exit.

#. Run the following command to bond NICs eth2 and eth3 to a NIC, for example, bond1:

   Run the following commands to create the **ifcfg-bond1** file and modify the configuration file:

   **cp** **ifcfg-bond0** **ifcfg-bond1**

   **vi** **ifcfg-bond1**

   Modified configuration file of NIC bond1 is as follows.

   .. code-block::

      BONDING_MASTER=yes
      TYPE=Bond
      MTU=8888
      STARTMODE=auto
      BONDING_MODULE_OPTS="mode=1 miimon=100"
      NM_CONTROLLED=no
      BOOTPROTO=STATIC
      DEVICE=bond1
      USERCONTRL=no
      LLADDR=40:7d:0f:52:e3:a5
      BONDING_SLAVE1=eth2
      BONDING_SLAVE0=eth3
      IPADDR=10.10.10.104
      NETMASK=255.255.255.0
      NETWORK=10.10.10.0

   .. note::

      In this configuration file, **MTU** is set to **8888**, **BONDING_MODULE_OPTS** is set to **mode=1 miimon=100**, **BOOTPROTO** is set to **STATIC**. **DEVICE**, **BONDING_SLAVE1**, **BONDING_SLAVE0**, **IPADDR**, **NETMASK**, and **NETWORK** are configured as required. **LLADDR** is set to the LLADDR value of the **BONDING_SLAVE1** NIC.

   After the modification, save the change and exit.

#. Run the following command to start the added bond1 NIC:

   **wicked** **ifup** **bond1**

#. Run the following command to query IP addresses:

   **ip** **addr** **show**

   An example is provided as follows:

   .. code-block::

      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
          inet 127.0.0.1/8 scope host lo
             valid_lft forever preferred_lft forever
          inet6 ::1/128 scope host
             valid_lft forever preferred_lft forever
      2: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff
      3: eth1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 8888 qdisc mq master bond0 state UP group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff
      4: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond1 state UP group default qlen 1000
          link/ether 40:7d:0f:52:e3:a5 brd ff:ff:ff:ff:ff:ff
      5: eth3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond1 state UP group default qlen 1000
          link/ether 40:7d:0f:52:e3:a5 brd ff:ff:ff:ff:ff:ff
      6: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP group default qlen 1000
          link/ether fa:16:00:57:90:c9 brd ff:ff:ff:ff:ff:ff
          inet 172.16.2.44/24 brd 172.16.2.255 scope global bond0
             valid_lft forever preferred_lft forever
          inet6 fe80::f816:ff:fe57:90c9/64 scope link
             valid_lft forever preferred_lft forever
      7: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
          link/ether 40:7d:0f:52:e3:a5 brd ff:ff:ff:ff:ff:ff
          inet 10.10.10.104/24 brd 10.10.10.255 scope global bond1
             valid_lft forever preferred_lft forever
          inet6 fe80::427d:fff:fe52:e3a5/64 scope link
             valid_lft forever preferred_lft forever

#. Repeat the preceding operations to configure other BMSs.

Delete a NIC
------------

.. note::

   For details about how to delete a NIC in other OSs, see:

   -  :ref:`Delete a NIC in SUSE Linux Enterprise Server 11 <en-us_topic_0121593249__section68171429202111>`
   -  :ref:`Delete a NIC in Red Hat, CentOS, Oracle Linux, and EulerOS <en-us_topic_0121593250__section17427175114209>`
   -  :ref:`Delete a NIC in Ubuntu <en-us_topic_0121593251__section17427175114209>`
   -  :ref:`Delete a NIC in Windows Server <en-us_topic_0121593252__section47181835181916>`

#. Obtain the IP address of the bonded enhanced high-speed NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the bond network device and run the following command to stop and delete the device:

   **wicked** **ifdown** **bond1**

#. Run the following commands to delete network configuration files **/etc/sysconfig/network-scripts/ifcfg-eth2**, **/etc/sysconfig/network-scripts/ifcfg-eth3**, and **/etc/sysconfig/network-scripts/ifcfg-bond1**:

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-eth2**

   **rm** **-f** **/etc/sysconfig/network-scripts/ifcfg-eth3**

   **rm** **/etc/sysconfig/network/ifcfg-bond1**
