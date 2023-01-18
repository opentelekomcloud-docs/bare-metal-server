:original_name: en-us_topic_0174865424.html

.. _en-us_topic_0174865424:

OS Partitioning Recommendations
===============================

Scenario 1: BIOS Boot
---------------------

If a BMS is booted in BIOS mode, BIOS needs to be configured for the image used to create the BMS and MBR partitioning is also required.

-  **If the primary partition meets your requirements:**

   A: If the boot and swap partitions are independent, use the following partitioning:

   boot-swap-root partition

   |image1|

   B: If the boot and swap partitions are not independent, use the following partitioning:

   swap-root partition

   |image2|

   root partition

   |image3|

-  **If an extended partition (for example, lvm) is required, use the following partitioning:**

   Extended partition (lvm)-swap-root partition

   |image4|

   Extended partition (lvm)-root partition

   |image5|

   boot-extended partition (lvm)-root partition

   |image6|

Scenario 2: UEFI Boot
---------------------

If a BMS is booted in UEFI mode, UEFI needs to be configured for the image used to create the BMS. For an x86 BMS with the UEFI boot mode, MBR partitioning is required and the boot_efi partition is mandatory.

-  **If the primary partition meets your requirements:**

   A: If the swap partition is independent, use the following partitioning:

   boot_efi-swap-root partition

   |image7|

   B: If the swap partition is not independent, use the following partitioning:

   boot_efi-root partition

   |image8|

-  **If an extended partition is required, use the following partitioning:**

   boot_efi-extended partition (lvm)-root partition

   |image9|

.. |image1| image:: /_static/images/en-us_image_0174667980.png
.. |image2| image:: /_static/images/en-us_image_0174668001.png
.. |image3| image:: /_static/images/en-us_image_0174668002.png
.. |image4| image:: /_static/images/en-us_image_0174668003.png
.. |image5| image:: /_static/images/en-us_image_0174668004.png
.. |image6| image:: /_static/images/en-us_image_0174668005.png
.. |image7| image:: /_static/images/en-us_image_0174668073.png
.. |image8| image:: /_static/images/en-us_image_0174668240.png
.. |image9| image:: /_static/images/en-us_image_0174668564.png
