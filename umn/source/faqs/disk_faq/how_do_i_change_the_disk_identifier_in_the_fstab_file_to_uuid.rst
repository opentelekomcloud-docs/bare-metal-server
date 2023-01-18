:original_name: en-us_topic_0151841134.html

.. _en-us_topic_0151841134:

How Do I Change the Disk Identifier in the fstab file to UUID?
==============================================================

Scenarios
---------

After attaching disks to a Linux BMS, you must change the disk identifier in the **fstab** file to UUID. Otherwise, you cannot enter the BMS OS or the BMS becomes unavailable due to a mount point disorder after you stop and start the BMS, or restart the BMS.

.. note::

   Universally Unique Identifier (UUID) is a 128-bit number used to identify information in computer systems.

Procedure
---------

This section takes CentOS 7 as an example to describe how to change the disk identifier in the **fstab** file to UUID.

#. Log in to the BMS as user **root**. Run the **blkid** command to query all types of file systems that have been mounted to the BMS and UUIDs of the corresponding devices.

   .. code-block::

      /dev/sda2: UUID="4eb40294-4c6f-4384-bbb6-b8795bbb1130" TYPE="xfs"
      /dev/sda1: UUID="2de37c6b-2648-43b4-a4f5-40162154e135" TYPE="swap"

#. Run the **cat /etc/fstab** command to open the **fstab** file.

   .. code-block::

      /dev/sda2  /       xfs     defaults    0 0
      /dev/sda1  swap    swap    defaults    0 0

#. Check the disk identifier in the **fstab** file.

   -  If the disk identifier is UUID, no further action is required.
   -  If the disk identifier is the device name, go to :ref:`4 <en-us_topic_0151841134__li784575352211>`.

#. .. _en-us_topic_0151841134__li784575352211:

   Run the **vi /etc/fstab** command to open the **fstab** file, press **i** to enter editing mode, and change the disk identifier to UUID.

   .. code-block::

      UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130 /       xfs     defaults    0 0
      UUID=2de37c6b-2648-43b4-a4f5-40162154e135 swap    swap    defaults    0 0

   Press **Esc** and enter **:wq** to save and exit the file.
