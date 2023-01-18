:original_name: en-us_topic_0084951049.html

.. _en-us_topic_0084951049:

SUSE 11 SP4
===========

#. In the **Installation Settings** phase, switch to the **Expert** tab and choose **Change** > **Partitioning**.

   **Creating a swap partition**

   a. On the **Preparing Hard Disk** page, select **Custom Partitioning (for experts)** and click **Next**.

   b. In the navigation pane on the left, choose **Hard Disks** and click **Add Partition**.

   c. On the **Add Partition on /dev/sda** page, select **Primary Partition** and click **Next**.

   d. Select **Custom Size**, set **Size** to **10GB**, and click **Next**.

   e. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

      |image1|

   **Creating a boot partition**

   a. In the navigation pane on the left, choose **Hard Disks** and click **Add Partition**.

   b. On the **Add Partition on /dev/sda** page, select **Primary Partition** and click **Next**.

   c. Select **Custom Size**, set **Size** to **5.00GB**, and click **Next**.

   d. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

      |image2|

   The swap and boot partitions are created.

#. (Optional) Create volumes.

   If both the swap and root volumes use LVM, perform the following operations to create volumes:

   a. In the navigation pane on the left, choose **Hard Disks** and click **Add Partition**.

   b. On the **Add Partition on /dev/sda** page, select **Primary Partition** and click **Next**.

   c. Select **Custom Size**, set **Size** to **14.99GB**, and click **Next**.

   d. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

      |image3|

   e. In the navigation pane on the left, choose **Volume Management**. Click **Add** and then select **Volume Group**.

   f. Configure required parameters and click **Finish**.

      |image4|

   g. In the navigation pane on the left, choose **Volume Management**. Click **Add** and then select **Logical Volume**.

   h. Set **Name** to **root** and **Type** to **Normal Volume**, and click **Next**.

   i. Set **Custom Size** to **10.00 GB** and click **Next**.

   j. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

      |image5|

      The root volume is created. The following steps describe how to create the swap volume.

   k. In the navigation pane on the left, choose **Volume Management**. Click **Add** and then select **Logical Volume**.

   l. Set **Name** to **swap** and **Type** to **Normal Volume**, and click **Next**.

   m. Set **Size** to **Maximum Size (4.99 GB)** and click **Next**.

   n. Configure **Formatting Options** and **Mounting Options**, and click **Finish**.

      |image6|

      Click **Accept**.

      The root and swap volumes are created.

#. Return to the **Installation Settings** page and check the current **Partitioning** and **Booting** configurations. Confirm the configurations and click **Install**.

#. Click **I Agree** and then **Install**.

#. Set the password of user **root**. Click **Next**.

#. Configure **Hostname** and **Domain Name**, and click **Next**.

#. On the **Network Configuration** page, select **Use Following Configuration** and click **Next**.

   On the **Test Internet Connection** page, select **No, Skip This Test** to skip the network connectivity test.

#. On the **Network Services Configuration** page, select **Use Following Configuration** and click **Next**.

#. Retain the default settings on the **User Authentication Method** page and click **Next**.

#. Create a local user, for example, **suse**. Click **Next**.

   .. note::

      When installing SUSE 11 SP4, you must create a local user. After the installation is complete, you can delete it if you do not need it. For details about how to delete it, see :ref:`Configuring the VM Environment <en-us_topic_0081116597>`.

#. On the **Hardware Configuration** page, select **Use Following Configuration** and click **Next**.

#. Click **Finish**.

.. |image1| image:: /_static/images/en-us_image_0111790014.png
.. |image2| image:: /_static/images/en-us_image_0111790956.png
.. |image3| image:: /_static/images/en-us_image_0111797467.png
.. |image4| image:: /_static/images/en-us_image_0111797592.png
.. |image5| image:: /_static/images/en-us_image_0111797692.png
.. |image6| image:: /_static/images/en-us_image_0111797843.png
