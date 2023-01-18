:original_name: en-us_topic_0108486965.html

.. _en-us_topic_0108486965:

(Optional) Installing the LOM Driver of x86 V5 Servers
======================================================

Scenario
--------

To provision x86 V5 BMSs, you need to install the X722 LOM driver in the ISO image. For other types of BMSs, skip this section.

.. note::

   Only Windows Server 2012 R2 and Windows Server 2016 support the LOM driver. This document uses Windows Server 2016 as an example to describe how to install the LOM driver. The procedure is also applicable to Windows Server 2012 R2.

Procedure
---------

#. Decompress the **onboard_driver_win2k16.iso** file in :ref:`Making Preparations <en-us_topic_0131700233>` and find the Intel NIC package or folder. For an Intel NIC package, for example, **NIC-82599_I350_X540_X550_X710_X722_XL710_XXV710-Win2K16-**\ *XXX*, decompress it to obtain the **PRO40GB\\Winx64\\NDIS64** folder.
#. Mount the image from **boot.wim** to a local directory and inject the driver in the NDIS64 folder into the image by referring to :ref:`4 <en-us_topic_0108486964__en-us_topic_0106538741_li1424714135269>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Save the added driver and unmount the image by referring to :ref:`5 <en-us_topic_0108486964__en-us_topic_0106538741_li1289027122520>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Mount the image from **install.wim** to a local directory and inject the LOM driver into the image by referring to :ref:`6 <en-us_topic_0108486964__en-us_topic_0106538741_li025094718206>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Save the added driver and unmount the image by referring to :ref:`7 <en-us_topic_0108486964__en-us_topic_0106538741_li142715295918>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
