:original_name: en-us_topic_0000001341779861.html

.. _en-us_topic_0000001341779861:

Registering an ISO File (Windows)
=================================

Scenarios
---------

This section describes how to register an external ISO file as a private image (ISO image) on the cloud platform. Before registering an image, upload the ISO image file to an OBS bucket.

Prerequisite
------------

-  The file to be registered must be in ISO format.
-  The ISO image file has been uploaded to an OBS bucket.

   .. note::

      The name of the ISO image file can contain only letters, digits, hyphens (-), and underscores (_). If the name does not meet requirements, change it.

Procedure
---------

#. Access the IMS console.

   a. Log in to the management console.

   b. Under **Compute**, click **Image Management Service**.

      The IMS console is displayed.

#. Register an ISO file as an ISO image.

   a. Click **Create Image** in the upper right corner.
   b. In the **Image Type and Source** area, select **ISO image** for **Type**.
   c. In the image file list, select the bucket and then the image file.
   d. In the **Image Information** area, set the following parameters.

      -  **Boot Mode**: Select **BIOS** or **UEFI**. Ensure that the selected boot mode is the same as that in the image file, or the ECSs created from this image will not be able to boot up.
      -  **OS**: Select the OS specified in the ISO file. To ensure that the image can be created and used properly, select an OS consistent with that in the image file.
      -  **System Disk**: Set the system disk capacity (value range: 40 GB to 1024 GB), which must be no less than the size of the system disk in the image file.
      -  **Name**: Enter a name for the image to be created.
      -  **Description**: (Optional) Enter image description as needed.

   e. Click **Create Now**.
   f. Confirm the settings and click **Submit**.

#. Switch back to the **Image Management Service** page to monitor the image status.

   When the image status changes to **Normal**, the image is registered successfully.
