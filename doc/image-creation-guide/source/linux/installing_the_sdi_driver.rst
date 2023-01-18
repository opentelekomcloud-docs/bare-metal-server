:original_name: en-us_topic_0081116736.html

.. _en-us_topic_0081116736:

Installing the SDI Driver
=========================

Scenario
--------

Currently, there are three types of SDI cards: SDI storage cards, SDI 2.2 (network cards), and SDI 3.0 (integrated storage and network cards). If the BMS uses SDI storage cards (neither SDI 2.2 nor SDI 3.0), the SDI driver needs to be installed on the VM so that EVS disks can be attached to the BMS. In other cases, skip this section. Currently, ARM 64, XenServer, and ESXi VMs do not support SDI cards. You do not need to install the SDI driver on such VMs.

Prerequisites
-------------

-  You have logged in to the VM.
-  You have downloaded the SDI driver (scsi_ep_front) as instructed in :ref:`Software <en-us_topic_0081116771>` and have uploaded it to the VM.

   .. note::

      The scsi_ep_front version must be 1.0.13 or later.

Procedure
---------

The following steps are for reference only.

#. Go to the directory storing the SDI driver installation package and run the following command:

   **rpm -ivh** kmod-scsi_ep_front-centos_7.6_1.0.18-3.10.0_957.el7.centos.x86_64.rpm

   .. note::

      The Ubuntu and Debian SDI driver uses the .deb installation package. Run the **dpkg -i**\ *xxx* (*xxx* indicates the name of the SDI installation package) command to install the SDI driver.

#. After the installation is complete, run the **rpm -qa \| grep scsi** command. The installation is successful if information similar to the following is displayed:

   .. code-block:: console

      [root@localhost ~] rpm -qa | grep scsi
      lsscsi-0.27-6.el7.x86_64
      kmod-scsi_ep_front-centos_7.6_1.0.18-3.10.0_957.el7.centos.x86_64

   For Ubuntu 18.04, Ubuntu 16.04, Ubuntu 14.04, and Debian, run the **dkms status** command. If **installed** is displayed, the installation is successful. Run the **update-initramfs -u** command to update the driver in the kernel.

   .. code-block::

      ...
      root@ubuntu:~/file# dkms status
      scsi_ep_front, 1.0.13, 4.4.0-21-generic, x86_64: installed
      scsi_ep_front, 1.0.13, 4.4.0-59-generic, x86_64: built
      scsi_ep_front, 1.0.13, 4.4.0-96-generic, x86_64: installed

#. Run the following commands to check whether the SDI driver matches the kernel version:

   a. Run the **uname -r** command to obtain the OS kernel version.

      .. code-block:: console

         [root@localhost r74]# uname -r
         3.10.0-957.el7.x86_64

   b. Run the **find / -name "*front*.ko"** command to check the SDI card driver matching the kernel version.

      .. code-block:: console

         [root@localhost r74]# find / -name "*front*.ko"
         /usr/lib/modules/3.10.0-957.el7.x86_64/extra/scsi_ep_front/scsi_ep_front.ko
