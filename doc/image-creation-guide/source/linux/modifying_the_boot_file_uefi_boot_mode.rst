:original_name: en-us_topic_0186973743.html

.. _en-us_topic_0186973743:

Modifying the Boot File (UEFI Boot Mode)
========================================

In the UEFI boot mode, you must modify the boot file. Otherwise, BMSs provisioned using the VM image may fail to start after they are forcibly restarted.

After the OS is installed, do not restart the VM immediately. Press **Ctrl + Alt + F2** to enter the CLI and perform the operations in this section to modify the boot file.

.. note::

   -  Startup failure cause and solution: When an image is created from a VM, the boot file in the image may encounter an error due to file format inconsistency. As a result, the BMS created from the image will fail to be forcibly restarted. You need to optimize the GRUB file to rectify this issue.
   -  Relevant to OS or not: The startup failure is irrelevant to the OS. You are advised to optimize the GRUB file for the VMs booted in UEFI mode.
   -  Impact: If no action is taken, it is possible that the BMS startup will fail. As a result, services cannot run on the BMS properly.

Arm
---

Run the **find / -name "boot/efi/EFI"** command to locate the boot file. Replace **boot/efi/EFI/BOOT/BOOTAA64.EFI** with **boot/efi/EFI/**\ *$os_version*\ **/grubaa64.efi**.

For example, *$os_version* for CentOS 7.4 is **centos**. Replace **boot/efi/EFI/BOOT/BOOTAA64.EFI** with **boot/efi/EFI/centos/grubaa64.efi**.

|image1|

The location of **grubaa64.efi** varies depending on the OS. For details, see :ref:`Table 1 <en-us_topic_0186973743__en-us_topic_0185141089_table12143132163717>`.

.. _en-us_topic_0186973743__en-us_topic_0185141089_table12143132163717:

.. table:: **Table 1** Location of **grubaa64.efi**

   ======= ==================================
   OS      grubaa64.efi Location
   ======= ==================================
   CentOS  /boot/efi/EFI/centos/grubaa64.efi
   EulerOS /boot/efi/EFI/euleros/grubaa64.efi
   SUSE    /boot/efi/EFI/sles/grubaa64.efi
   Ubuntu  /boot/efi/EFI/ubuntu/grubaa64.efi
   Red Hat /boot/efi/EFI/redhat/grubaa64.efi
   ======= ==================================

x86
---

Run the **find / -name "boot/efi/EFI"** command to locate the boot file. For example, the boot file of EulerOS 2.5 is located in **/boot/efi/EFI**. Replace **/boot/efi/EFI/BOOT/BOOTX64.EFI** with **/boot/efi/EFI/**\ *$os_version*\ **/grubx64.efi**.

For example, *$os_version* for EulerOS 2.5 is **euleros**. Replace **/boot/efi/EFI/BOOT/BOOTX64.EFI** with **/boot/efi/EFI/euleros/grubx64.efi**.

|image2|

The location of **grubx64.efi** varies depending on the OS. For details, see :ref:`Table 2 <en-us_topic_0186973743__en-us_topic_0185141089_table188516111711>`.

.. _en-us_topic_0186973743__en-us_topic_0185141089_table188516111711:

.. table:: **Table 2** Location of **grubx64.efi**

   ======= =================================
   OS      grubx64.efi Location
   ======= =================================
   CentOS  /boot/efi/EFI/centos/grubx64.efi
   EulerOS /boot/efi/EFI/euleros/grubx64.efi
   SUSE    /boot/efi/EFI/sles/grubx64.efi
   Ubuntu  /boot/efi/EFI/ubuntu/grubx64.efi
   Red Hat /boot/efi/EFI/redhat/grubx64.efi
   ======= =================================

.. |image1| image:: /_static/images/en-us_image_0185149593.jpg
.. |image2| image:: /_static/images/en-us_image_0185156699.png
