:original_name: en-us_topic_0157011196.html

.. _en-us_topic_0157011196:

Initializing a Linux Data Disk (parted)
=======================================

Scenarios
---------

This section uses CentOS 7.0 64-bit as an example to describe how to initialize a data disk attached to a BMS running Linux and use parted to partition the data disk.

The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Therefore, use the GPT partition style if your disk capacity is greater than 2 TB. In Linux OSs, if the GPT partition style is used, the fdisk partitioning tool cannot be used. The parted partitioning tool must be used. For details about disk partition styles, see :ref:`Introduction to Data Disk Initialization Scenarios and Partition Styles <en-us_topic_0157011194>`.

The method for initializing a disk varies depending on the OSs running on the BMS. This document is for reference only. For detailed operations and differences, see the product documents of the OSs running on the corresponding BMSs.

Prerequisites
-------------

-  You have logged in to the BMS.
-  A data disk has been attached to the BMS and has not been initialized.

Creating Partitions and Attaching a Disk
----------------------------------------

The following example shows how to use parted to create a partition on a new data disk that has been attached to the BMS. The default partitioning style is GPT and the default file system format is **ext4**. Mount the file system to **/mnt/sdc**, and configure automatic mounting upon system start.

#. Run the following command to query information about the added data disk:

   **lsblk**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-centos-70 linux]# lsblk
      NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
      sda    202:0    0   40G  0 disk
      ├─sda1 202:1    0    4G  0 part [SWAP]
      └─sda2 202:2    0   36G  0 part /
      sdb    202:16   0  10G  0 disk

   The command output shows that the BMS has two disks, system disk **/dev/sda** and data disk **/dev/sdb**.

#. Run the following command to enter parted to partition the added data disk:

   **parted** *Added data disk*

   For example, run the following command to use fdisk to perform the partitioning operations for the **/dev/sdb** data disk:

   **parted** **/dev/sdb**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-centos-70 linux]# parted /dev/sdb
      GNU Parted 3.1
      Using /dev/sdb
      Welcome to GNU Parted! Type 'help' to view a list of commands.

#. Enter **p** and press **Enter** to view the current disk partition style.

   Information similar to the following is displayed:

   .. code-block::

      (parted) p
      Error: /dev/sdb: unrecognised disk label
      Model: Xen Virtual Block Device (xvd)
      Disk /dev/sdb: 10.7GB
      Sector size (logical/physical): 512B/512B
      Partition Table: unknown
      Disk Flags:

   In the command output, the **Partition Table** value is **unknown**, indicating that the disk partition style is unknown.

#. Run the following command to set the disk partition style:

   **mklabel** *Disk partition style*

   For example, run the following command to set the partition style to GPT: (Disk partition styles include MBR and GPT.)

   **mklabel** **gpt**

   .. caution::

      The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Because a data disk currently supports up to 32 TB, use the GPT partition style if your disk capacity is larger than 2 TB.

      If you change the disk partition style after the disk has been used, the original data on the disk will be cleared. Therefore, select a proper disk partition style when initializing the disk.

#. Enter **p** and press **Enter** to view the disk partition style.

   Information similar to the following is displayed:

   .. code-block::

      (parted) mklabel gpt
      (parted) p
      Model: Xen Virtual Block Device (xvd)
      Disk /dev/sdb: 20971520s
      Sector size (logical/physical): 512B/512B
      Partition Table: gpt
      Disk Flags:

      Number  Start  End  Size  File system  Name  Flags

#. Enter **unit s** and press **Enter** to set the measurement unit of the disk to sector numbers.

#. Enter **mkpart opt** *2048s 100%* and press **Enter**.

   In this example, one partition is created for the added data disk. Variable *2048s* indicates the disk start capacity, and variable *100%* indicates the disk end capacity. The two values are used for reference only. You can determine the number of partitions and the partition capacity based on your service requirements.

   Information similar to the following is displayed:

   .. code-block::

      (parted) mkpart opt 2048s 100%
      Warning: The resulting partition is not properly aligned for best performance.
      Ignore/Cancel? Ignore

   If the preceding warning message is displayed, enter **Ignore** to ignore the performance warning.

#. Enter **p** and press **Enter** to view the details about the created partition.

   Information similar to the following is displayed:

   .. code-block::

      (parted) p
      Model: Xen Virtual Block Device (xvd)
      Disk /dev/sdb: 20971520s
      Sector size (logical/physical): 512B/512B
      Partition Table: gpt
      Disk Flags:

      Number  Start   End        Size       File system  Name  Flags
       1      2048s   20969471s  20967424s               opt

   Details about the **/dev/sdb1** partition are displayed.

#. Enter **q** and press **Enter** to exit parted.

#. Run the following command to view the disk partition information:

   **lsblk**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-centos-70 linux]# lsblk
      NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
      sda    202:0    0   40G  0 disk
      ├─sda1 202:1    0    4G  0 part [SWAP]
      └─sda2 202:2    0   36G  0 part /
      sdb    202:16   0  100G  0 disk
      └─sdb1 202:17   0  100G  0 part

   In the command output, **/dev/sdb1** is the partition you created.

#. Run the following command to set the format for the file system of the newly created partition:

   **mkfs** **-t** *File system format* **/dev/sdb1**

   For example, run the following command to set the **ext4** file system for the **/dev/xvdb1** partition:

   **mkfs** **-t** **ext4** **/dev/sdb1**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-centos-70 linux]# mkfs -t ext4 /dev/sdb1
      mke2fs 1.42.9 (28-Dec-2013)
      Filesystem label=
      OS type: Linux
      Block size=4096 (log=2)
      Fragment size=4096 (log=2)
      Stride=0 blocks, Stripe width=0 blocks
      655360 inodes, 2620928 blocks
      131046 blocks (5.00%) reserved for the super user
      First data block=0
      Maximum filesystem blocks=2151677925
      80 block groups
      32768 blocks per group, 32768 fragments per group
      8192 inodes per group
      Superblock backups stored on blocks:
      32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

      Allocating group tables: done
      Writing inode tables: done
      Creating journal (32768 blocks): done
      Writing superblocks and filesystem accounting information: done

   The formatting takes a period of time. Observe the system running status and do not exit.

   .. note::

      The partition sizes supported by file systems vary. Therefore, you are advised to choose an appropriate file system based on your service requirements.

#. Run the following command to create a mount point:

   **mkdir** *Mount point*

   For example, run the following command to create the **/mnt/sdc** mount point:

   **mkdir** **/mnt/sdc**

#. Run the following command to mount the new partition on the created mount point:

   **mount** **/dev/sdb1** *Mount point*

   For example, run the following command to mount the newly created partition on **/mnt/sdc**:

   **mount** **/dev/sdb1** **/mnt/sdc**

#. Run the following command to view the mount result:

   **df** **-TH**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-centos-70 linux]# df -TH
      Filesystem     Type      Size  Used Avail Use% Mounted on
      /dev/sda2     xfs        39G  4.0G   35G  11% /
      devtmpfs       devtmpfs  946M     0  946M   0% /dev
      tmpfs          tmpfs     954M     0  954M   0% /dev/shm
      tmpfs          tmpfs     954M  9.1M  945M   1% /run
      tmpfs          tmpfs     954M     0  954M   0% /sys/fs/cgroup
      /dev/sdb1     ext4      11G   38M  101G   1% /mnt/sdc

   The newly created **/dev/sdb1** is mounted on **/mnt/sdc**.

Set Automatic Disk Attachment Upon BMS Start
--------------------------------------------

To automatically attach a disk when a BMS starts, you should not specify its partition, for example **/dev/sdb1**, in **/etc/fstab**. This is because the sequence of cloud devices may change during the server start or stop process, for example, from **/dev/sdb** to **/dev/sdc**. You are advised to use the universally unique identifier (UUID) in **/etc/fstab** to automatically attach a disk at system start.

.. note::

   The universally unique identifier (UUID) is the unique character string for disk partitions in a Linux system.

#. Run the following command to query the partition UUID:

   **blkid** *Disk partition*

   For example, run the following command to query the UUID of **/dev/sdb1**:

   **blkid** **/dev/sdb1**

   Information similar to the following is displayed:

   .. code-block:: console

      [root@bms-b656 test]# blkid /dev/sdb1
      /dev/sdb1: UUID="1851e23f-1c57-40ab-86bb-5fc5fc606ffa" TYPE="ext4"

   The UUID of **/dev/sdb1** is displayed.

#. Run the following command to open the **fstab** file using the vi editor:

   **vi** **/etc/fstab**

#. Press **i** to enter the editing mode.

#. Move the cursor to the end of the file and press **Enter**. Then add the following information:

   .. code-block::

      UUID=1851e23f-1c57-40ab-86bb-5fc5fc606ffa /mnt/sdc      ext4 defaults     0   2

#. Press **Esc**, enter **:wq**, and press **Enter**.

   The system saves the configurations and exits the vi editor.
