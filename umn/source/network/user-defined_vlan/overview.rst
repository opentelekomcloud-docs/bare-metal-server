:original_name: en-us_topic_0085714156.html

.. _en-us_topic_0085714156:

Overview
========

User-defined VLAN
-----------------

You can use the 10GE Ethernet NICs that are not being used by the system to configure a user-defined VLAN. The QinQ technology is used to isolate networks and provide additional physical planes and bandwidths. You can create VLANs to isolate network traffic. User-defined VLAN NICs are in pairs. You can configure NIC bonding to achieve high availability. User-defined VLANs in different AZs cannot communicate with each other.

Ethernet NICs not used by the system by default do not have configuration files and are in **down** state during the system startup. You can run **ifconfig** **-a** to view the NIC name and run **ifconfig** *eth2* **up** to configure the NIC. The configuration method varies depending on the OS.

For example, on a Linux BMS, eth0 and eth1 are automatically bonded in a VPC network, and eth2 and eth3 are used in a user-defined VLAN. You can send packets with any VLAN tags through the two network interfaces. If you want to allocate a VLAN, configure eth2 and eth3 bonding and create the target VLAN network interface on the bond device. The method is similar to that of creating a bond device and a VLAN sub-interface in a VPC.

.. note::

   In a user-defined VLAN, ports can be bonded or not, and they can only be bonded in active/standby mode.

   For more information about NIC bond, visit https://www.kernel.org/doc/Documentation/networking/bonding.txt.

For details about how to configure a user-defined VLAN for BMSs running different OSs, see sections :ref:`Configuring a User-defined VLAN (SUSE Linux Enterprise Server 12) <en-us_topic_0095251843>` to :ref:`Configuring a User-defined VLAN (Windows Server) <en-us_topic_0095251848>`.

View User-defined VLANs
-----------------------

User-defined VLANs are presented to you through the BMS specifications. For example, if the extended configuration of a flavor is 2 x 2*10GE, a BMS created using this flavor provides one two-port 10GE NIC for connecting to the VPC as well as one two-port 10GE extension NIC for a high-speed interconnection between BMSs. You can configure VLANs on the extension NIC as needed.
