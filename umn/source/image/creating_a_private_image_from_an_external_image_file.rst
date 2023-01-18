:original_name: en-us_topic_0078468105.html

.. _en-us_topic_0078468105:

Creating a Private Image from an External Image File
====================================================

Scenarios
---------

You can create and register a private image using an external image file. :ref:`Figure 1 <en-us_topic_0078468105__fig38131647453>` shows the procedure.

.. _en-us_topic_0078468105__fig38131647453:

.. figure:: /_static/images/en-us_image_0260591452.png
   :alt: **Figure 1** Creating a private image from an external image file

   **Figure 1** Creating a private image from an external image file

The procedure contains the following steps:

#. Prepare an image file. For details, see *Bare Metal Server Private Image Creation Guide*.
#. Upload the image file to your OBS bucket. For details, see :ref:`Upload an External Image File <en-us_topic_0078468105__section175082275342>`.
#. On the management console, select the uploaded image file and register it as a private image. For details, see :ref:`Register a Private Image <en-us_topic_0078468105__section17202836566>`.

.. _en-us_topic_0078468105__section175082275342:

Upload an External Image File
-----------------------------

You can import an image file in VHD, VMDK, QCOW2, RAW, VHDX, QCOW, VDI, QED, ZVHD, or ZVHD2 format to create a private image.

Use OBS Browser to upload external image files. For details, see *Object Storage Service User Guide*.

When uploading the external image file, you must select an OBS bucket with standard storage.

.. _en-us_topic_0078468105__section17202836566:

Register a Private Image
------------------------

#. Log in to the management console.

#. Under **Computing**, click **Image Management Service**.

   The IMS console is displayed.

#. Click **Create Image** in the upper right corner.

#. Configure the following information:

   **Image Type and Source**

   -  **Type**: Select **System disk image**.

   -  **Source**: Select **Image file**.

      In the bucket list, select the bucket that stores the image file and select the image file.

   **Image Information**

   -  **Function**: Select **BMS system disk image**.

      Ensure that you have completed initialization configuration on the image file by following the instructions in *Bare Metal Server Private Image Creation Guide*.

   -  **OS**: (Optional) Select the OS of the image file.

      To ensure that the image can be created and used properly, select the OS consistent with that of the image file.

   -  **System Disk (GB)**: Set the system disk size. You are advised to set the value to the image system disk size plus 2 GB.

   -  **Name**: Enter a name for the image to be created. The value can contain only letters, digits, spaces, hyphens (-), underscores (_), and periods (.), and cannot start or end with a space.

   -  **Tag**: (Optional) Add a tag to the image to identify and manage the image more easily.

   -  **Description**: (Optional) Enter description of the image.

#. Click **Create Now**.

   On the displayed **Details** page, confirm the configuration and click **Submit**.

#. Return to the image list. If the status of the private image changes to **Normal**, the private image is registered successfully.

   .. note::

      The time required for registering a private image varies depending on the size of the image file.

Follow-up Operations
--------------------

You can use the private image to create a BMS by following the instructions in :ref:`Creating a BMS Using a Private Image <en-us_topic_0140737793>`.
