:original_name: en-us_topic_0000001238956345.html

.. _en-us_topic_0000001238956345:

Hi1822 Standard Cards (for BMSs with Centralized BMGW)
======================================================

Scenario
--------

If the BMS with centralized BMGW uses Hi1822 NICs, you need to install the Hi1822 driver on the VM. The following uses CentOS 7.6 as an example.

Prerequisites
-------------

-  You have logged in to the VM.

-  You have obtained the Hi1822 driver installation package and management software and uploaded them to the VM.

   For details about how to obtain the packages (.rpm), see :ref:`Software <en-us_topic_0081116771>`.

   The downloaded Hi1822 driver installation package and management software must match the OS.

Procedure
---------

#. Check whether the hinic driver exists.

   **rpm -qa \| grep hinic**

   -  If yes, go to :ref:`2 <en-us_topic_0000001238956345__en-us_topic_0285684646_li19735144125814>`.
   -  If no, go to :ref:`3 <en-us_topic_0000001238956345__en-us_topic_0285684646_li04412416588>`.

#. .. _en-us_topic_0000001238956345__en-us_topic_0285684646_li19735144125814:

   Uninstall the hinic driver.

   **rpm -e kmod-hinic**

   **rmmod hinic**

#. .. _en-us_topic_0000001238956345__en-us_topic_0285684646_li04412416588:

   Go to the directory where the .rpm installation package is stored and run the following command to install it:

   **rpm -ivh NIC-Hi1822-CentOS7.6-hinic-3.9.0.8-1-x86_64.rpm**

#. Run the **modprobe hinic** command to load the latest Hi1822 driver.

#. Install Hi1822 management software (hinicadm package).

   **rpm -ivh NIC-Hi1822-CentOS7.6-hinicadm-3.9.0.8-1-x86_64.rpm**
