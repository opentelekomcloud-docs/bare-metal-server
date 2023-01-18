:original_name: en-us_topic_0131700227.html

.. _en-us_topic_0131700227:

Overview
========

Install a Linux OS based on the OS type of the BMS image to be created. This section describes how to install SUSE 11 SP4, Ubuntu 18.04, Ubuntu 16.04, Ubuntu 14.04, Debian 8.6, and SUSE 12 because installing these types of OSs requires some special configuration.

The installation procedure varies depending on the image file. Configure the time zone, KMS address, patch server, repo source update address, input method, and language based on service requirements.

.. important::

   -  Creating a BMS image with the BIOS boot mode requires MBR partitioning, and a primary partition needs to be reserved for provisioning the BMS. After the BMS is provisioned, a 64 MB config drive partition is automatically generated. MBR supports a maximum of four partitions, including both the primary and extended ones. Therefore, a maximum of three image primary partitions are allowed. Otherwise, the BMS provisioning will fail.
   -  If automatic partition extension is required, the root partition must be the last and primary partition.
   -  If your services require a large number of partitions, you need to configure LVM partitions based on extended partitions.
   -  For a VM with the UEFI boot mode, do not restart it immediately after its OS is installed. You need to perform the operations in :ref:`Modifying the Boot File (UEFI Boot Mode) <en-us_topic_0186973743>` to modify the boot file before restarting the VM.
