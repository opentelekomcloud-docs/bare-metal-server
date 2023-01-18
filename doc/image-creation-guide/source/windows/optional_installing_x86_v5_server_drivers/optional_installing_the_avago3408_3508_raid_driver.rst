:original_name: en-us_topic_0131700758.html

.. _en-us_topic_0131700758:

(Optional) Installing the Avago3408/3508 RAID Driver
====================================================

Scenario
--------

To provision BMSs with Avago3408/3508 RAID cards, you need to Install the Avago3408/3508 RAID driver in the ISO image. For other types of BMSs, skip this section.

.. note::

   Only Windows Server 2012 R2 and Windows Server 2016 support the Avago3408/3508 RAID driver. This document uses Windows Server 2016 as an example to describe how to install the 3408/3508 RAID driver. The procedure is also applicable to Windows Server 2012 R2.

Procedure
---------

#. Decompress the **onboard_driver_win2k16.iso** file in :ref:`Making Preparations <en-us_topic_0131700233>` to obtain the folder that contains **RAID** and **megasas**, for example, **RAID-3408iMR_3416iMR_3508_3516-Win2K16-megasas35-**\ *XXX*.
#. Mount the image from **boot.wim** to a local directory and inject the driver in the **RAID-3408iMR_3416iMR_3508_3516-Win2K16-megasas35-7.716.3.0-x86_64** folder into the image by referring to :ref:`4 <en-us_topic_0108486964__en-us_topic_0106538741_li1424714135269>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Save the added driver and unmount the image by referring to :ref:`5 <en-us_topic_0108486964__en-us_topic_0106538741_li1289027122520>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Mount the image from **install.wim** to a local directory and inject the 3408/3508 RAID driver into the image by referring to :ref:`6 <en-us_topic_0108486964__en-us_topic_0106538741_li025094718206>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
#. Save the added driver and unmount the image by referring to :ref:`7 <en-us_topic_0108486964__en-us_topic_0106538741_li142715295918>` in :ref:`Installing the chipset Driver <en-us_topic_0108486964>`.
