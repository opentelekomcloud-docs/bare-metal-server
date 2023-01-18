:original_name: en-us_topic_0102427987.html

.. _en-us_topic_0102427987:

Attaching Data Disks
====================

Scenarios
---------

If the existing disks of a BMS fail to meet service requirements, for example, due to insufficient disk space or poor disk performance, you can attach more available disks to the BMS, or create more disks and attach them to the BMS.

Constraints
-----------

-  The disk and the target BMS must be located in the same AZ.

-  The BMS must be in **Running** or **Stopped** state.

-  **Device Type** of the EVS disk must be **SCSI**.

-  A non-shared EVS disk must be in **Available** state.

   A shared EVS disk must be in **In-use** or **Available** state.

-  BMSs using some flavors or images cannot have EVS disks attached because the servers do not have SDI iNICs or for other reasons.

Prerequisites
-------------

Disks are available.

For details about how to create disks, see "Creating an EVS Disk" in *Elastic Volume Service User Guide*.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. In the upper right corner of the BMS list, enter the name, private IP address, ID, or flavor of a BMS and click |image1| to search for the desired BMS.

#. Click the name of the target BMS.

   The page showing details of the BMS is displayed.

#. Click the **Disks** tab. Then, click **Attach Disk**.

   The **Attach Disk** dialog box is displayed.

#. Select the disk type and target disk, and set the mount point as prompted.

   .. note::

      If no EVS disks are available, click **Create Disk** in the lower part of the list.

#. Click **OK**.

   After the disk is attached, you can view the information about it on the **Disks** tab.

Follow-up Operations
--------------------

If the attached disk is newly created, the disk can be used only after it is initialized (formatted). For details about how to initialize data disks, see :ref:`Initializing Data Disks <en-us_topic_0157011194>`.

.. note::

   After the BMS is restarted, the drive letter of the EVS disk may change. For the mapping between the EVS disk device and drive letter, see :ref:`How Do I Obtain the Drive Letter of an EVS Disk? <en-us_topic_0102493013>`

.. |image1| image:: /_static/images/en-us_image_0102459954.png
