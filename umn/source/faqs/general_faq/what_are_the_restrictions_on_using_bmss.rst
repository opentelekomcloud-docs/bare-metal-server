:original_name: en-us_topic_0053536930.html

.. _en-us_topic_0053536930:

What Are the Restrictions on Using BMSs?
========================================

-  External hardware devices (such as USB devices, bank U keys, external hard disks, and dongles) cannot be loaded.
-  Live migration is not supported. If a BMS is faulty, your services running on it may be affected. It is good practice to deploy your services in a cluster or in primary/standby mode to ensure high availability.
-  You cannot create a server without an OS, that is, a BMS must have an OS.
-  The OS of a BMS cannot be changed after it is created or during OS reinstallation.
-  After a BMS is created, you cannot change its VPC.
-  When you create a BMS, you can only select a flavor with specified CPU, memory, and local disks but cannot configure them separately. After a BMS is created, you can expand the capacity of attached EVS disks but cannot modify the BMS CPU, memory, or local disks.
-  You can only attach EVS disks whose device type is **SCSI** to a BMS.
-  You cannot attach EVS disks to BMSs of certain flavors or BMSs created from certain images because these BMSs do not have SDI iNICs or lack compatibility.
-  Do not delete or modify built-in plug-ins of an image, such as Cloud-Init and bms-network-config. Otherwise, basic BMS functions will be affected.
-  If you choose to assign an IP address automatically when you create a BMS, do not change the private IP address of the BMS after the BMS is provisioned. Otherwise, the IP address may conflict with that of another BMS.
-  BMSs do not support bridge NICs because they will cause network interruptions.
-  Do not upgrade the OS kernel. Otherwise, the hardware driver may become incompatible with the BMS and adversely affect the BMS reliability.
