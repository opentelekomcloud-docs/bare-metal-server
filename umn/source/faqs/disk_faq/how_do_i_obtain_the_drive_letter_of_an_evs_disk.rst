:original_name: en-us_topic_0102493013.html

.. _en-us_topic_0102493013:

How Do I Obtain the Drive Letter of an EVS Disk?
================================================

After a BMS is restarted, the drive letter of an EVS disk attached to the BMS may change. This section describes how to find the mapping between an EVS disk and its drive letter.

#. Record **Device Identifier** of the EVS disk on the BMS details page.

#. Log in to the BMS OS, switch to the **/dev/disk/by-id** directory, and run the **ll** command to check the mapping between the WWN and drive letter. In Linux, WWN is in the format **wwn-0x** + *Device identifier*, for example, **wwn-0x50000397c80b685d -> ../../sdc**.


   .. figure:: /_static/images/en-us_image_0143429915.png
      :alt: **Figure 1** Checking the mapping between the WWN and drive letter

      **Figure 1** Checking the mapping between the WWN and drive letter

.. note::

   You are advised to use the WWN to perform operations on disks. For example, run the **mount** *wwn-0x50000397c80b685d Folder name* command to attach a disk. You are not advised to use the drive letter directly because drive letter drift may cause the failure to find the disk.

   Obtaining the drive letter of a disk by using the WWN is only supported by Linux.
