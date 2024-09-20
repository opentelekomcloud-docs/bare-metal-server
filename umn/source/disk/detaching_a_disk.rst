:original_name: en-us_topic_0102427988.html

.. _en-us_topic_0102427988:

Detaching a Disk
================

Scenarios
---------

A disk attached to a BMS can be detached.

-  A disk mounted to **/dev/sda** functions as the system disk. You can only detach the system disk from a stopped BMS.
-  Disks attached to a mount point other than **/dev/sda** function as data disks and can be detached from a running or stopped BMS.

.. note::

   After a BMS is restarted, the drive letter of an EVS disk attached to the BMS may change to the one different from that in the OS.

   So, you are advised to use a world wide name (WWN) instead of a driver letter when you perform operations on disks. For details about the mapping between a WWN and driver letter, see :ref:`How Do I Obtain the Drive Letter of an EVS Disk? <en-us_topic_0102493013>`

Constraints
-----------

-  Detaching the system disk is a mission-critical operation. A BMS without the system disk cannot start. Exercise caution when performing this operation.
-  Before detaching a data disk from a running Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

-  Before detaching a data disk from a running Linux BMS, you must log in to the BMS and run the **umount** command to cancel the association between the disk and the file system. In addition, ensure that no program is reading data from or writing data to the disk. Otherwise, detaching the disk will fail.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the BMS from which the disk is to be detached. The page showing details of the BMS is displayed.

#. Click the **Disks** tab. Locate the row containing the disk to be detached and click **Detach**.
