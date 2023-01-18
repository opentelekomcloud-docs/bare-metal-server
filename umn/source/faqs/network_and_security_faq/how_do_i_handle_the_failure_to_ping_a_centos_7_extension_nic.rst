:original_name: en-us_topic_0151554411.html

.. _en-us_topic_0151554411:

How Do I Handle the Failure to Ping a CentOS 7 Extension NIC?
=============================================================

Cause
-----

A known kernel issue of the OS

.. note::

   CentOS 7.4 and earlier CentOS 7 have this issue.

Solution
--------

This issue has been rectified in CentOS 7.5. To use extension NICs, you are advised to use CentOS 7.5 or upgrade the OS kernel version to 3.10.0-862. (In quick provisioning scenarios, you can only resolve this issue by changing the OS to CentOS 7.5.).

#. Upload the CentOS 7.5 kernel file downloaded from the official website to the BMS and run the following command to update the kernel:

   **yum install kernel-3.10.0-862.el7.x86_64.rpm**

   .. note::

      If you have configured automatic EVS disk attaching to the BMS in **/etc/fstab**, comment out the corresponding configuration item in **/etc/fstab**. Otherwise, you may fail to enter the BMS OS when restarting the BMS.

#. Restart the OS. After entering the OS, reinstall the SDI iNIC driver, RAID controller card driver, and IB driver for CentOS 7.5 by following the instructions in the *Bare Metal Server Private Image Creation Guide*.
