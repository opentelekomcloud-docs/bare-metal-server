:original_name: en-us_topic_0151841137.html

.. _en-us_topic_0151841137:

How Do I Increase the Swap Partition Size?
==========================================

Scenarios
---------

When you install the Oracle database for a Linux OS, the swap partition size will be checked. If the swap partition cannot meet requirements, you can perform the operations in this section to increase the swap partition size.

.. note::

   The swap partition is similar to the virtual memory of the Windows OS. When the memory is insufficient, some hard disk space is virtualized into memory to improve the system running efficiency.

Procedure
---------

#. Log in to the BMS OS.

#. Run the **lsblk** command to check the size of the swap partition.

   |image1|

   The size of the swap partition is 3 GB.

#. Run the following command to increase the swap partition size by 5 GB (example):

   **dd if=/dev/zero of=/swapfile bs=1M count=5000**

   **chmod 600 /swapfile**

   **mkswap /swapfile swapon /swapfile echo** **"/swapfile swap swap defaults 0 0" >>/etc/fstab**

#. Run the **lsblk** command to check the size of the expanded swap partition.

   |image2|

   The size of the swap partition is 8 GB.

.. |image1| image:: /_static/images/en-us_image_0284616164.png
.. |image2| image:: /_static/images/en-us_image_0284616165.png
