:original_name: en-us_topic_0053536894.html

.. _en-us_topic_0053536894:

Creating a BMS Supporting Quick Provisioning
============================================

Scenarios
---------

When you create a common BMS (that is, a BMS booted from a local disk), its OS needs to be downloaded from the cloud and it also takes some time to install the OS. When you create a BMS that uses an EVS as its system disk, the OS has been installed on the disk and does not need to be downloaded or installed. In this way, the BMS can be provisioned within a short time when you apply for it.

BMSs supporting quick provisioning have the following advantages over other BMSs:

-  BMSs booted from EVS disks can be provisioned within about 5 minutes.
-  BMSs support CSBS backups, ensuring data security.
-  BMS rebuilding upon faults is supported, enabling quick service recovery.
-  An image of a BMS can be exported to apply configurations of the BMS to other BMSs, eliminating the need to repeatedly configure BMSs.

On the page for creating a BMS, select a flavor that supports quick BMS provisioning, set the system disk type and capacity, and configure other required parameters.

Procedure
---------

You can create a BMS supporting quick provisioning by following the instructions in :ref:`Creating a Common BMS <en-us_topic_0053536933>`.

When creating the BMS, pay attention to the following parameters:

-  **Flavor**: Select **physical.h2.large**. For more information about flavors, see :ref:`Instance Family <en-us_topic_0083745258>`.
-  **Image**: Select a public image that supports quick provisioning.
-  **Disk**: Set the system disk type and size.
