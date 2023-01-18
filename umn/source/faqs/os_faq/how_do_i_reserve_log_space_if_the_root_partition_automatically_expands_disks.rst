:original_name: en-us_topic_0151841135.html

.. _en-us_topic_0151841135:

How Do I Reserve Log Space If the Root Partition Automatically Expands Disks?
=============================================================================

Scenarios
---------

In the scenario where the root partition automatically expands disks, the initial root partition may occupy all space of the system disk. This section describes how to reserve log space.

Procedure
---------

#. Run the **lsblk** command. The following command output indicates that the initial root partition has occupied all space of the system disk.

   |image1|

#. Run the following command to create a directory for storing logs:

   **mkdir log**

   |image2|

#. Run the following command to create a 200 GB image file for storing logs.

   **dd if=/dev/zero of=disk.img bs=1M count=200000**

   |image3|

#. Run the following commands to virtualize the generated file into a block device and format it:

   **losetup /dev/loop0 disk.img**

   **mkfs.ext4 /dev/loop0**

   |image4|

#. Run the following command to mount the image file to the log directory:

   **mount disk.img log**

   |image5|

#. Create a file in the log directory.

   |image6|

#. Run the following command to add the mount command to **/etc/rc.local**:

   **mount /root/disk.img /root/log**

   |image7|

#. Run the following command to restart the OS:

   **reboot**

   |image8|

#. Run the **lsblk** command. The command output indicates that the image file has been mounted.

   |image9|

.. |image1| image:: /_static/images/en-us_image_0284616152.png
.. |image2| image:: /_static/images/en-us_image_0284616153.png
.. |image3| image:: /_static/images/en-us_image_0284616154.png
.. |image4| image:: /_static/images/en-us_image_0284616155.png
.. |image5| image:: /_static/images/en-us_image_0284616156.png
.. |image6| image:: /_static/images/en-us_image_0284616157.png
.. |image7| image:: /_static/images/en-us_image_0284616158.png
.. |image8| image:: /_static/images/en-us_image_0284616159.png
.. |image9| image:: /_static/images/en-us_image_0284616161.png
