:original_name: en-us_topic_0081116728.html

.. _en-us_topic_0081116728:

What Can I Do If Packets from the VLAN Subinterface of bond0 of a Linux BMS Use the MAC Address of bond0 as the Source MAC Address?
===================================================================================================================================

This is a known Linux kernel issue that will result in ping failures from BMS extension NICs to the gateway. This issue is known in the OSs listed in :ref:`Table 1 <en-us_topic_0081116728__en-us_topic_0094568821_table25919128546>`. Obtain a patch based on the kernel version from the OS vendor to rectify this issue.

.. _en-us_topic_0081116728__en-us_topic_0094568821_table25919128546:

.. table:: **Table 1** OS type and kernel version

   ============ ==============
   OS           Kernel Version
   ============ ==============
   Red Hat 7.2  3.10.0-327
   Red Hat 7.3  3.10.0-514
   Red Hat 7.4  3.10.0-693
   CenOS 7.0    3.10.0-514
   CentOS 7.2   3.10.0-327
   CentOS 7.3   3.10.0-514
   CentOS 7.4   3.10..0-693
   EulerOS 2.2  3.10.0-327
   Ubuntu 14.04 3.13.0-24
   ============ ==============
