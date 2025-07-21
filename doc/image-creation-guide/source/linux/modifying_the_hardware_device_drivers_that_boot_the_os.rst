:original_name: en-us_topic_0081116685.html

.. _en-us_topic_0081116685:

Modifying the Hardware Device Drivers That Boot the OS
======================================================

Scenario
--------

This section describes how to modify the hardware device drivers that are loaded during OS startup.

Prerequisites
-------------

You have logged in to the VM.

Procedure
---------

#. Add or modify the configuration file.

   -  For Red Hat/Oracle Linux/EulerOS/OpenEuler/SUSE 12/SUSE 15/CentOS, use the vi editor to open the **/etc/dracut.conf** file and change or add the value of **add_drivers**. In the following example, the value of **add_drivers** is a list of RAID drivers.

      .. code-block::

         logfile=/var/log/dracut.log
         # fileloglvl=7
         ...
         ...
         # additional kernel modules to the default
         add_drivers+=" ahci megaraid_sas mpt3sas mpt2sas virtio_blk virtio_scsi virtio_net "

      .. note::

         If an error is reported, add a space before and after the driver list in the quotation marks and try again.

   -  For Ubuntu 14.04 or Debian, use the vi editor to open the **/etc/initramfs-tools/modules** file and add ahci, megaraid_sas, mpt3sas, and mpt2sas drivers (the format depends on the OS).

      .. code-block::

         # List of modules that you want to include in your initramfs.
         # They will be loaded at boot time in the order below.
         #
         # Syntax:  module_name [args ...]
         #
         # You must run update-initramfs(8) to effect this change.
         #
         # Examples:
         #
         # raid1
         # sd_mod
         ahci
         megaraid_sas
         mpt3sas
         mpt2sas
         virtio_blk
         virtio_scsi
         virtio_net

   -  For Ubuntu 16.04/Ubuntu 18.04, add drivers to the **/etc/dracut.conf** and **/etc/initramfs-tools/modules** files. Before editing the files, install required software.

      a. Run the following command to install dracut:

         **apt-get install dracut**

         After the installation is complete, add **add_drivers+="ahci megaraid_sas mpt3sas mpt2sas virtio_blk virtio_scsi virtio_net"** to the end of the **/etc/dracut.conf** file by performing operations similar to those for Red Hat and Oracle Linux 7.3.

         .. note::

            If an error is reported, add a space before and after the driver list in the quotation marks and try again.

      b. Run the following command to install initramfs-tools:

         **apt-get install** **initramfs-tools**

         After the installation is complete, add the ahci, megaraid_sas, mpt3sas, mpt2sas, and virtio_blk virtio_scsi virtio_net drivers to the end of the **/etc/initramfs-tools/modules** file by performing operations similar to those for Ubuntu 14.04.

   -  For Ubuntu 16.04 ARM, run the following commands to update the kernel and drivers, and then restart the VM:

      **sudo apt-get update**

      **sudo apt-get dist-upgrade**

   -  For SUSE 11 SP4, use the vi editor to open the **/etc/sysconfig/kernel** file, and add or change the value of **INITRD_MODULES**. In the following example, the value of **INITRD_MODULES** is a list of RAID drivers.

      .. code-block::

         ...
         #
         INITRD_MODULES=" ahci megaraid_sas mpt3sas mpt2sas virtio_blk virtio_scsi virtio_net "
         ## Type:   string(yes)
         ...

   .. note::

      You can enter multiple RAID drivers and separate them with spaces. The RAID driver names can be obtained from the purchased hardware devices. Multiple types of drivers can be added at the same time, such as mpt3sas, mpt2sas, and megaraid_sas. If any hardware driver cannot be installed here, you can install it after the BMS is created.

#. Update the kernel. For Ubuntu 16.04 ARM and Ubuntu 18.04 ARM, skip this step.

   For Rad Hat/Oracle Linux/EulerOS/SUSE 12/SUSE 15/Ubuntu 16.04/Ubuntu 18.04/CentOS run the **dracut -f** command.

   -  For Rad Hat/Oracle Linux/EulerOS/OpenEuler/CentOS, run the **dracut -f** command. Wait for several seconds. If no command output is returned, the drivers have been loaded.

   -  For SUSE 12 SP1, run the **dracut -f** command. Check the command output in the last few lines. If message "Some kernel modules could not be included. This is not necessarily an error:" is displayed and drivers not loaded are displayed (excluding the RAID drivers), the RAID drivers are loaded successfully.

      .. code-block::

         ...
         Some kernel modules could not be included
         This is not necessarily an error:
         pcmcia
         sdhci_acpi
         swap

   -  For SUSE 12/SUSE 15, run the **dracut -f** command. The kernel is updated successfully if information similar to the following is displayed.

      |image1|

   -  For Ubuntu 14.04/Ubuntu 16.04/Ubuntu 18.04/Debian, run the following command to generate initrd:

      **update-initramfs -u**

      Run the following commands to check whether the ahci, megaraid_sas, mpt3sas, and mpt2sas drivers have been loaded:

      **lsinitramfs /boot/initrd.img-`uname -r\` \|grep ahci**

      **lsinitramfs /boot/initrd.img-`uname -r\` \|grep megaraid_sas**

      **lsinitramfs /boot/initrd.img-`uname -r\` \|grep mpt3sas**

      **lsinitramfs /boot/initrd.img-`uname -r\` \|grep mpt2sas**

   -  For SUSE 11 SP4, run the **mkinitrd** command to check whether the value of **Kernel Modules** contains the manually added drivers. If the following command output is displayed, the drivers are successfully loaded.

      |image2|

#. For SUSE 11 SP4, change the virtual disks in the VM file to physical disks. For other OSs, such as Rad Hat, CentOS, Oracle Linux, SUSE 12, and EulerOS, skip this step.

   .. note::

      If LVM is used, perform :ref:`3.a <en-us_topic_0081116685__en-us_topic_0094568813_li2038115376525>` to :ref:`3.e <en-us_topic_0081116685__en-us_topic_0094568813_li14313204215910>` to change the drive letter mode.

   a. In the **/boot/grub** directory of the VM, run the **blkid** command to check whether disk partitions are normal.

      .. code-block::

         linux-a5d6:/boot/grub # blkid
         /dev/sda1: UUID="c23d47f8-ef1b-4c4e-9a3b-5ae138ef7184" TYPE="swap"
         /dev/sda2: UUID="27644978-e244-4a8c-996a-03119fdaff71" TYPE="ext3"

      If some disk partitions do not have UUIDs, check whether the VM OS is properly installed. If it is not, install it again.

   b. Use the vi editor to open the **/boot/grub/menu.lst** file, modify the OS boot parameters, and save the configuration.

      Original **menu.lst** file

      |image3|

      Modified **menu.lst** file

      |image4|

   c. Use the vi editor to open the **/boot/grub/device.map** file.

      Original **device.map** file

      .. code-block::

         (hd0)   /dev/disk/by-id/ata-QEMU_HARDDISK_QM00001
         ~

      Modified **device.map** file

      .. code-block::

         (hd0)   /dev/sda

   d. Use the vi editor to open the **/etc/fstab** file.

      Original **fstab** file

      |image5|

      Modified **fstab** file

      |image6|

   e. Use the vi editor to open the **/etc/mtab** file, delete the line where CDROM of **/dev/sr0** is located, and save the configuration.

      Modified **mtab** file

      |image7|

      .. note::

         If the **/dev/sr0** configuration item does not exist, skip this step.

   f. Use the vi editor to open the **/etc/sysconfig/bootloader** file.

      Original **bootloader** file

      |image8|

      Modified **bootloader** file

      |image9|

   If SUSE 11 SP4 uses LVM, replace the virtual disks in the VM file with the actual physical disks.

   a. .. _en-us_topic_0081116685__en-us_topic_0094568813_li2038115376525:

      In the **/boot/grub** directory of the VM, run the **blkid** command to check whether disk partitions are normal.

      |image10|

      If some disk partitions do not have UUIDs, check whether the VM OS is properly installed. If it is not, install it again.

   b. Use the vi editor to open the **/boot/grub/menu.lst** file, modify the OS boot parameters, and save the configuration.

      Original **menu.lst** file

      |image11|

      Modified **menu.lst** file

      |image12|

   c. Use the vi editor to open the **/boot/grub/device.map** file.

      Original **device.map** file

      .. code-block::

         (hd0)    /dev/disk/by-id/ata-QEMU_HARDDISK_QM00001

      Modified **device.map** file

      .. code-block::

         (hd0)    /dev/sda
         ~

   d. Use the vi editor to open the **/etc/fstab** file.

      Original **fstab** file

      |image13|

      Modified **fstab** file

      |image14|

   e. .. _en-us_topic_0081116685__en-us_topic_0094568813_li14313204215910:

      Use the vi editor to open the **/etc/sysconfig/bootloader** file.

      Original **bootloader** file

      |image15|

      Modified **bootloader** file

      |image16|

   After the configuration is complete, run the **mkinitrd** command. If the value of **resume** is not **by-uuid**, run the **reboot** and then **mkinitrd** commands to ensure that the value of **resume** is **by-uuid**.

#. For Ubuntu 18.04 and Ubuntu 16.04 ARM, modify the **grub**, **fstab**, and **interfaces** files.

   a. Modify parameters in the **/etc/default/grub** configuration file.

      Set **GRUB_DISABLE_LINUX_UUID** to **true**.

      .. code-block::

         ...
         # Uncomment if you don't want GRUB to pass "root=UUID=xxx" parameter to linux
         GRUB_DISABLE_LINUX_UUID=true

         # Uncomment to disable generation of recovery mode menu entries
         ...

      Then, run the **sudo update-grub2** command.

   b. Change the UUID in the **/etc/fstab** file to that of **/dev/sdax**, which can be obtained by running the **sudo blkid** command.

      |image17|

   c. Delete all interface information except **lo interface** from the **/etc/network/interfaces** file.

      .. code-block::

         # This file describes the network interfaces available on your system
         # and how to activate them. For more information, see interfaces (5).

         source /etc/network/interfaces.d/*

         # The loopback network interface
         auto lo
         iface to inet loopback

         ~
         ~

.. |image1| image:: /_static/images/en-us_image_0110233456.png
.. |image2| image:: /_static/images/en-us_image_0110233690.png
.. |image3| image:: /_static/images/en-us_image_0110233949.png
.. |image4| image:: /_static/images/en-us_image_0110234663.png
.. |image5| image:: /_static/images/en-us_image_0110234765.png
.. |image6| image:: /_static/images/en-us_image_0110235417.png
.. |image7| image:: /_static/images/en-us_image_0110235547.png
.. |image8| image:: /_static/images/en-us_image_0110238210.png
.. |image9| image:: /_static/images/en-us_image_0110238020.png
.. |image10| image:: /_static/images/en-us_image_0110238387.png
.. |image11| image:: /_static/images/en-us_image_0110245733.png
.. |image12| image:: /_static/images/en-us_image_0110245739.png
.. |image13| image:: /_static/images/en-us_image_0110246321.png
.. |image14| image:: /_static/images/en-us_image_0110249107.png
.. |image15| image:: /_static/images/en-us_image_0110249358.png
.. |image16| image:: /_static/images/en-us_image_0110249249.png
.. |image17| image:: /_static/images/en-us_image_0110250240.png
