:original_name: en-us_topic_0053536890.html

.. _en-us_topic_0053536890:

Private Image Overview
======================

A private image is an image available only to the user who created it. It contains an OS, preinstalled public applications, and a user's private applications. You can create a private image in the following ways:

-  :ref:`Creating a Private Image from a BMS <en-us_topic_0084807532>`

   .. note::

      Currently, only a BMS that supports quick provisioning (the OS is installed on an EVS disk) can be used to create a private image.

-  :ref:`Creating a Private Image from an External Image File <en-us_topic_0078468105>`

   You can upload external image files to the cloud platform and register them as your private images. Supported external image formats include VMDK, VHD, QCOW2, RAW, VHDX, QED, VDI, QCOW, ZVHD2, and ZVHD.

   .. note::

      Images of other formats must be converted using the image conversion tool before they can be used on BMSs. For details about how to convert the image format, see Image Management Service User Guide.

After a private image is created successfully, the image status becomes **Normal**. You can use the image to create BMSs or share the image with other tenants. The following figure shows how to use private images.


.. figure:: /_static/images/en-us_image_0177240840.png
   :alt: **Figure 1** Using private images

   **Figure 1** Using private images
