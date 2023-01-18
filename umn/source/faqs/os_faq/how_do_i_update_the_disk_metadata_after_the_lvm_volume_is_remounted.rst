:original_name: en-us_topic_0000001170719651.html

.. _en-us_topic_0000001170719651:

How Do I Update the Disk Metadata After the LVM Volume Is Remounted?
====================================================================

Scenarios
---------

If the LVM volume is remounted when a BMS OS is reinstalled, you need to update the disk metadata in a timely manner. Otherwise, the OS will be unavailable after it is restarted.

Procedure
---------

If a BMS uses LVM partitioning and the LVM volume is remounted when the BMS OS is reinstalled, update the disk metadata in a timely manner after the remount is complete. In this way, the disk metadata will be consistent with the disk mounting information after the OS is restarted. To update disk metadata, run the following commands (*sysvg* is the volume group (VG) name of the LVM volume):

**lvm vgcfgrestore** *sysvg*

**lvm pvscan**

**lvm vgscan**

**lvm vgchange -ay**
