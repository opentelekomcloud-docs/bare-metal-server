:original_name: en-us_topic_0131700232.html

.. _en-us_topic_0131700232:

Overview
========

You can install growpart to automatically extend the root partition. For SUSE, growpart is installed by default. However, for SUSE 11 SP4, you need to install growpart with an earlier version to replace the default one. For other SUSE distributions, you do not need to install growpart. For Ubuntu, growpart is installed by default and the version meets requirements. Therefore, you do not need to install growpart. For XenServer, partitions can be selected during the OS installation. Therefore, automatic root partition extension is not supported.

.. note::

   If the boot mode is UEFI (for example, it is UEFI for Arm), run the **yum install gdisk** command to install gdisk.
