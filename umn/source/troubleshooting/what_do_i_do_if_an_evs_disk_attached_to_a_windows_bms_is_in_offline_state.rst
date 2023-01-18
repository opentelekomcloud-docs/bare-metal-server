:original_name: en-us_topic_0103482177.html

.. _en-us_topic_0103482177:

What Do I Do If an EVS Disk Attached to a Windows BMS Is in Offline State?
==========================================================================

Symptom
-------

After an EVS disk is attached to a Windows BMS, start **Control Panel**, choose **System and Security** > **Administrative Tools**, and double-click **Computer Management**. On the **Computer Management** page, choose **Storage** > **Disk Management**. The EVS disk attached to the BMS is in **Offline** state.

Solution
--------

#. Log in to the Windows BMS.

#. Click **Start**, enter **cmd** in **Search programs and files**, and press **Enter** to open the command-line interface (CLI).

#. Type **diskpart**.

   .. code-block::

      C:\Users\Administrator>diskpart

#. Type **san**.

   .. code-block::

      DISKPART> san
      SAN Policy: Online All

#. Type **san policy=onlineall**.

   .. code-block::

      DISKPART> san policy=onlineall
      DiskPart successfully changed the SAN policy for the current operating system

#. Type **list disk** to display all disks of the BMS.

   .. code-block::

      DISKPART> list disk
      Disk ### Status    Size    Free     Dyn    Gpt
      Disk 0   Online   838 GB    0B
      Disk 1   Offline   838 GB    838 GB
      Disk 2   Offline   838 GB    838 GB
      Disk 3   Offline   838 GB    838 GB
      ...

#. Type **select disk** *num*. *num* indicates the disk number. Replace it with the specific disk number.

   .. code-block::

      DISKPART> select disk 4

#. Type **attributes disk clear readonly**.

   .. code-block::

      DISKPART> attributes disk clear readonly
      DiskPart succeed to clear disk attributes.

#. Type **online disk**.

   .. code-block::

      DISKPART> online disk
      DiskPart succeed to make the selected disk online.

#. After the modification, format the EVS disk.
