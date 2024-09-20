:original_name: en-us_topic_0084807532.html

.. _en-us_topic_0084807532:

Creating a Private Image from a BMS
===================================

Scenarios
---------

You can create a private image from a BMS and copy the system disk data of the BMS to the private image. The system disk contains an OS and pre-installed applications for running services.

Constraints
-----------

-  Currently, only a BMS that supports quick provisioning (the OS is installed on an EVS disk) can be used to create a private image.
-  Data disks of a BMS cannot be exported as images.
-  The BMS must be stopped.
-  This operation depends on the bms-network-config and Cloud-Init plug-ins in the BMS image.

   -  If the BMS is created using a public image, the image has the bms-network-config and Cloud-Init plug-ins by default.
   -  If the BMS is created using a private image, check whether bms-network-config and Cloud-Init are installed by following the instructions in *Bare Metal Server Private Image Creation Guide*.

Precautions
-----------

-  Delete sensitive data from the BMS before using it to creating a private image to prevent data leak.
-  Delete residual files from the OS. For details, see "Deleting Files" in *Bare Metal Server Private Image Creation Guide*.
-  During the image creation process, do not change the BMS status. Otherwise, the image will fail to be created.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Locate the row that contains the target BMS, click **More** in the **Operation** column, and select **Stop** from the drop-down list.

   Only a BMS in stopped state can be used to create a private image.

#. After the BMS status changes to **Stopped**, click **More** in the **Operation** column and select **Create Image**.

   The page for creating an image is displayed.

#. Enter the image name, set a tag, and enter description as needed.

   Click **Create Now**.

#. On the displayed **Details** page, confirm the configuration and click **Submit**.

#. Return to the image list. If the status of the private image changes to **Normal**, the private image is created successfully.

Follow-up Operations
--------------------

If you want to create BMSs using the private image, see :ref:`Creating a BMS Using a Private Image <en-us_topic_0140737793>`. On the page for creating BMSs, select the private image you have created.
