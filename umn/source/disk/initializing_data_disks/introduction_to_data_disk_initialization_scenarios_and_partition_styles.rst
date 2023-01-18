:original_name: en-us_topic_0157011194.html

.. _en-us_topic_0157011194:

Introduction to Data Disk Initialization Scenarios and Partition Styles
=======================================================================

Scenarios
---------

After a disk is attached to a BMS, you need to log in to the BMS to initialize (format) the disk before you can use the disk properly.

-  System disk

   A system disk does not need to be initialized because it is automatically created and initialized during the BMS creation. The default disk partition style is master boot record (MBR).

-  Data disk

   -  If a data disk is created during the BMS creation, it will be automatically attached to the BMS.
   -  If a data disk is created explicitly, you need to manually attach the data disk to the BMS.

   In both cases, the data disk can only be used after it is initialized. Choose a proper disk partition style based on your service plans.

Disk Partition Style
--------------------

:ref:`Table 1 <en-us_topic_0157011194__en-us_topic_0085245975_table2729705994129>` lists the common disk partition styles. For Linux OSs, different disk partition styles require different partitioning tools.

.. _en-us_topic_0157011194__en-us_topic_0085245975_table2729705994129:

.. table:: **Table 1** Disk partition styles

   +----------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
   | Disk Partition Style       | Maximum Disk Capacity Supported | Maximum Number of Partitions Supported                                                                                                                                                                                                                                     | Linux Partitioning Tool |
   +============================+=================================+============================================================================================================================================================================================================================================================================+=========================+
   | Master Boot Record (MBR)   | 2 TB                            | -  4 primary partitions                                                                                                                                                                                                                                                    | -  fdisk                |
   |                            |                                 | -  3 primary partitions and 1 extended partition                                                                                                                                                                                                                           | -  parted               |
   |                            |                                 |                                                                                                                                                                                                                                                                            |                         |
   |                            |                                 | With the MBR partition style, primary partitions and an extended partition can be included, where the extended partition can contain several logical partitions. For example, if 6 partitions need to be created, you can create the partitions in the following two ways: |                         |
   |                            |                                 |                                                                                                                                                                                                                                                                            |                         |
   |                            |                                 | -  3 primary partitions and 1 extended partition, with the extended partition containing 3 logical partitions                                                                                                                                                              |                         |
   |                            |                                 | -  1 primary partition and 1 extended partition, with the extended partition containing 5 logical partitions                                                                                                                                                               |                         |
   +----------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
   | GUID Partition Table (GPT) | 18 EB                           | Unlimited                                                                                                                                                                                                                                                                  | parted                  |
   |                            |                                 |                                                                                                                                                                                                                                                                            |                         |
   |                            | 1 EB = 1048576 TB               | Disk partitions allocated using GPT are not categorized.                                                                                                                                                                                                                   |                         |
   +----------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+

.. caution::

   The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Currently, an EVS data disk supports up to 32 TB. Therefore, use the GPT partition style if your disk capacity is greater than 2 TB.

   If you change the disk partition style after the disk has been used, the original data on the disk will be cleared. Therefore, select a proper disk partition style when initializing the disk.
