:original_name: en-us_topic_0084945523.html

.. _en-us_topic_0084945523:

Converting the Image Format
===========================

For BMS, the image format can only be ZVHD2. After obtaining an image file, convert its format to ZVHD2.


.. figure:: /_static/images/en-us_image_0146602964.png
   :alt: **Figure 1** Converting the image format

   **Figure 1** Converting the image format

Step 1: Upload the image file (for example, **Redhat73.qcow2**) to an OBS bucket.

Step 2: Register the image file as a private image (for example, **Redhat73**). For details, see "Creating a Private Image from an External Image File" in *Bare Metal Server User Guide*.

Step 3: Export the private image to an OBS bucket in ZVHD2 format, for example, **Redhat73.zvhd2**. For details, see "Exporting Images" in *Image Management Service User Guide*.

Step 4: Register the image file in ZVHD2 format in the OBS bucket as a private image (for example, **Redhat73_new**).

.. note::

   The image format has been converted to ZVHD2 in Step 3. If you want to use the private image to create a BMS, you need to register the private image as instructed in Step 4.
