:original_name: en-us_topic_0000001194356682.html

.. _en-us_topic_0000001194356682:

Hi1822 Offload Cards (for BMSs with SDI 2.2)
============================================

Scenario
--------

If the BMS uses SDI 2.2 cards, you need to install the Hi1822 driver on the VM. The following uses EulerOS 2.3 as an example.

Prerequisites
-------------

-  You have logged in to the VM.

-  You have obtained the Hi1822 driver installation package and management software and uploaded them to the VM.

   Perform the following operations to obtain the package.

   #. Download the .zip package as instructed in :ref:`Software <en-us_topic_0081116771>`.

   #. The following uses **Hi1822_BM_X86_1.19.3.B036.tar.gz** as an example to describe how to obtain the required installation package.

      Download and decompress the **Hi1822_BM_X86_1.19.3.B036.tar.gz** driver package, and obtain the .rpm package **kmod-hinic-1.8.3.16_3.10.0_514.41.4.28.h70.x86_64-1.x86_64.rpm** based on the OS type and kernel version.

      |image1|

Procedure
---------

#. Check whether the hinic driver exists.

   **rpm -qa \| grep hinic**

   -  If yes, go to :ref:`2 <en-us_topic_0000001194356682__en-us_topic_0285684648_li19735144125814>`.
   -  If no, go to :ref:`3 <en-us_topic_0000001194356682__en-us_topic_0285684648_li04412416588>`.

#. .. _en-us_topic_0000001194356682__en-us_topic_0285684648_li19735144125814:

   Uninstall the hinic driver.

   **rpm -e kmod-hinic**

   **rmmod hinic**

#. .. _en-us_topic_0000001194356682__en-us_topic_0285684648_li04412416588:

   Go to the directory where the .rpm installation package is stored and run the following command to install it:

   **rpm -ivh** **kmod-hinic-1.8.3.16_3.10.0_514.41.4.28.h70.x86_64-1.x86_64.rpm**

#. Run the **modprobe hinic** command to load the latest Hi1822 driver.

.. |image1| image:: /_static/images/en-us_image_0285803934.png
