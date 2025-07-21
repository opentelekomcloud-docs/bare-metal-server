:original_name: en-us_topic_0081116809.html

.. _en-us_topic_0081116809:

SUSE 12
=======

#. Click **Expert Partitioner** before you install the OS.

#. Right-click the default partition and choose **Delete** from the shortcut menu.

   |image1|

#. Partition the disk based on service requirements. The following is for reference only.

   a. In the navigation pane on the left, choose **Hard Disks** and click **Add Partition**.

   b. Select **Primary Partition** and click **Next**.

   c. Set **Size** to **500 MiB** (example) or set it based on service requirements.

   d. Select **Operating System** for **Role** and click **Next**.

   e. Select **File System** and **Mount Point**, and click **Finish**.

      |image2|

      The boot partition is created.

#. If both the swap and root volumes use LVM, perform the following operations to create volumes:

   a. In the navigation pane on the left, choose **Hard Disks** and click **Add Partition**.

   b. Select **Primary Partition** and click **Next**.

   c. Select **Custom Size**, set **Size** to **19.50 GB**, and click **Next**.

   d. Select **Operating System** for **Role** and click **Next**.

   e. Configure **Formatting Options** and click **Finish**.

      |image3|

   f. In the navigation pane on the left, choose **Volume Management**. Click **Add** and then select **Volume Group**.

   g. Configure parameters shown in the following figure and click **Add** to add available physical volumes to the **Selected Physical Volumes** area.

      Click **Finish**.

      |image4|

   h. In the navigation pane on the left, choose **Volume Management**. Click **Add** and then select **Logical Volume**.

   i. Set the logical volume name to **swap** and size to **5 GiB**.

   j. Select **Operating System** for **Role**.

   k. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

   l. Create the root volume in the similar way as the swap volume. Set the logical volume name to **root** and size to **14.50 GiB**.

      Configure **Formatting Options** and **Mounting Options** and click **Finish**.

      |image5|

      Check the partitions and volumes.

      |image6|

      The partitions and volumes are created successfully. Click **Next** and continue the OS installation as prompted.

.. |image1| image:: /_static/images/en-us_image_0111866716.png
.. |image2| image:: /_static/images/en-us_image_0110933081.png
.. |image3| image:: /_static/images/en-us_image_0110941812.png
.. |image4| image:: /_static/images/en-us_image_0110953788.png
.. |image5| image:: /_static/images/en-us_image_0110948741.png
.. |image6| image:: /_static/images/en-us_image_0110952357.png
