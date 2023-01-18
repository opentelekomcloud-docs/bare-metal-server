:original_name: en-us_topic_0108600905.html

.. _en-us_topic_0108600905:

(Optional) Installing the SDI Driver
====================================

With the SDI driver, EVS disks can be attached to BMSs. The EVS disks can be used as system disks from which the BMSs are booted. This facilitates quick BMS provisioning. If you do not need to use EVS disks or your BMS does not have SD1 cards, skip this section.

Prerequisites
-------------

-  You have logged in to the VM.

-  You have downloaded the SDI driver (scsi_ep_front) as instructed in :ref:`Software <en-us_topic_0081116771>` and have uploaded it to the VM.

   .. note::

      The scsi_ep_front version must be 2.0.2.12 or later.

-  WDK has been installed.

   Download WDK from http://download.microsoft.com/download/4/E/0/4E07EAAD-E394-4EA8-B2B8-D46E46A409C5/wdk/wdksetup.exe.

Procedure
---------

#. Obtain the device management tool **devcon.exe** from the WDK directory **C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64**, and place **devcon.exe** in the same directory as the SDI driver.

   |image1|

#. Find the EpScsiAdpt installation file and view the PCI ID.

   |image2|

#. Open the CLI, go to the directory where the SDI driver and device management tool are located, and run the following command:

   **devcon install EpScsiAdpt.inf** "*PCI\\VEN_19E5&DEV_1610&SUBSYS_000119E5*"

   |image3|

   The PCI ID is an example only.

#. (Optional) Delete device nodes.

   a. If the environment where you create an image does not have SDI hardware, the storage controller in the device manager has exceptions.

      |image4|

   b. Open the CLI, go to the directory where the SDI driver and devcon installation tool are stored, and delete the abnormal device nodes.

      Run the **devcon.exe find "PCI\\VEN_19E5*"** command to locate abnormal device nodes.

      Run the **devcon.exe remove "@ROOT\\SCSIADAPTER\\0000"** command to delete the nodes.

      |image5|

   c. Restart the VM.

      |image6|

   d. Check whether the exceptions in the storage controller are cleared.

.. |image1| image:: /_static/images/en-us_image_0110264994.png
.. |image2| image:: /_static/images/en-us_image_0110264996.png
.. |image3| image:: /_static/images/en-us_image_0110265018.png
.. |image4| image:: /_static/images/en-us_image_0110265029.png
.. |image5| image:: /_static/images/en-us_image_0110265037.png
.. |image6| image:: /_static/images/en-us_image_0110266962.png
