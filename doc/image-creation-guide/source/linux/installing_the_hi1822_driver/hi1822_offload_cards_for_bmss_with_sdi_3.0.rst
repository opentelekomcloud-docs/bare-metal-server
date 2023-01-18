:original_name: en-us_topic_0000001238836639.html

.. _en-us_topic_0000001238836639:

Hi1822 Offload Cards (for BMSs with SDI 3.0)
============================================

Scenario
--------

If the BMS uses SDI 3.0 cards, you need to install the Hi1822 driver on the VM. The following uses CentOS 7.6 as an example.

Prerequisites
-------------

-  You have logged in to the VM.

-  You have obtained the Hi1822 driver installation package and management software and uploaded them to the VM.

   Perform the following operations to obtain the package.

   #. Download the .zip package as instructed in :ref:`Software <en-us_topic_0081116771>`.

   #. The following uses **uNIC_GuestOS_Driver_BM_2.21.8.B070.tar.gz** as an example to describe how to obtain the required installation package.

      Download and decompress the **uNIC_GuestOS_Driver_BM_2.21.8.B070.tar.gz** driver package, and obtain the .rpm package **kmod-hinic-5.0.0.7_3.10.0_957-1.el7.x86_64.rpm** based on the OS type and kernel version.

Procedure
---------

#. Check whether the hinic driver exists.

   **rpm -qa \| grep hinic**

   -  If yes, go to :ref:`2 <en-us_topic_0000001238836639__en-us_topic_0285684649_li125230442252>`.
   -  If no, go to :ref:`3 <en-us_topic_0000001238836639__en-us_topic_0285684649_li752311444259>`.

#. .. _en-us_topic_0000001238836639__en-us_topic_0285684649_li125230442252:

   Uninstall the hinic driver.

   **rpm -e kmod-hinic**

   **rmmod hinic**

#. .. _en-us_topic_0000001238836639__en-us_topic_0285684649_li752311444259:

   Go to the directory where the .rpm installation package is stored and run the following command to install it:

   **rpm -ivh** **kmod-hinic-5.0.0.7_3.10.0_957-1.el7.x86_64.rpm**

#. Run the **modprobe hinic** command to load the latest Hi1822 driver.
