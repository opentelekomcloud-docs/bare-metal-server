:original_name: en-us_topic_0102462512.html

.. _en-us_topic_0102462512:

What Are the Restrictions for Attaching a Disk to a BMS?
========================================================

-  The disk and the target BMS must be located in the same AZ.

-  The BMS must be in **Running** or **Stopped** state.

-  **Device Type** of the EVS disk must be **SCSI**.

-  A non-shared EVS disk must be in **Available** state.

   A shared EVS disk must be in **In-use** or **Available** state.

-  BMSs using some flavors or images cannot have EVS disks attached because the servers do not have SDI iNICs or for other reasons.
