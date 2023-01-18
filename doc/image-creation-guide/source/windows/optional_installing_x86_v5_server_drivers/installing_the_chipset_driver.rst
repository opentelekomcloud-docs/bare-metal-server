:original_name: en-us_topic_0108486964.html

.. _en-us_topic_0108486964:

Installing the chipset Driver
=============================

Scenario
--------

chipset is a driver living on a Windows motherboard. If this driver is not installed, other hardware drivers may be undermined in performance or even fail to work properly.

.. note::

   chipset can only be installed in Windows Server 2012 R2 and Windows Server 2016. This document uses Windows Server 2016 as an example to describe how to install the chipset driver. The procedure is also applicable to Windows Server 2012 R2.

Procedure
---------

#. Decompress the **onboard_driver_win2k16.iso** file in :ref:`Making Preparations <en-us_topic_0131700233>` to obtain the **SetupChipset.exe** file from the folder that contains **chipset** (for example, **Chipset-Win2K16-**\ *XXX*).

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li1081816145255:

   Extract **SetupChipset.exe** to a new folder.

   a. Click **Start**, enter **cmd** in the **Type here to search** box to open the command-line interface (CLI).

   b. Go to the directory where **SetupChipset.exe** is stored, for example, **D:\\windows2016\\tmp**.

      .. code-block::

         D:\windows2016\tmp>dir
         2018/04/08    17:25    <DIR>          .
         2018/04/08    17:25    <DIR>          ..
         2018/03/08    15:14    <DIR>          drivers1
         2018/03/08    11:28         3,525,008 SetupChipset.exe

         D:\windows2016\tmp>

   c. Run the following command to extract **SetupChipset.exe** to a new folder named **driver**:

      **.\\SetupChipset.exe -extract driver**

      .. code-block::

         D:\windows2016\tmp>.\SetupChipset.exe -extract driver

         D:\windows2016\tmp>dir
         2018/04/08    17:32    <DIR>          .
         2018/04/08    17:32    <DIR>          ..
         2018/04/08    17:32    <DIR>          driver
         2018/03/08    15:14    <DIR>          drivers1
         2018/03/08    11:28         3,525,008 SetupChipset.exe

         D:\windows2016\tmp>

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li13296014152612:

   Decompress the Windows 2016 ISO file to a folder.

   |image1|

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li1424714135269:

   Mount the image from **boot.wim** to a local directory and inject the chipset driver into the images.

   a. Open Dism++ and choose **File** > **Mount Image**.

   b. In the **Mount Image** window, perform the operations in the following figure in sequence.

      |image2|

      1: Select the target image.

      2: Select **boot.wim** in the **sources** folder shown in :ref:`3 <en-us_topic_0108486964__en-us_topic_0106538741_li13296014152612>`.

      3: Select an empty folder, for example, **tmp1**.

      4: Click **OK**. A message is displayed indicating that the image is being mounted.

   c. When the image status changes to **Ready**, click **Open session**.

   d. .. _en-us_topic_0108486964__en-us_topic_0106538741_li1949712487312:

      Perform the operations shown in the following figure in sequence.

      |image3|

      1. In the navigation pane, choose **Drivers**.

      2. Select **Display in-box driver**.

      3: Select **System Equipment**.

      4. Click **Add**.

   e. .. _en-us_topic_0108486964__en-us_topic_0106538741_li1024418186448:

      Select the **drivers** folder generated in :ref:`2 <en-us_topic_0108486964__en-us_topic_0106538741_li1081816145255>`.

      The following dialog box is displayed.

      |image4|

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li1289027122520:

   Save the added driver and unmount the image.

   a. Choose **File** > **Save Image**. In the displayed dialog box, click **Save**.

   b. Wait for the image status to change from **Saving** to **Ready**.

   c. Choose **File** > **Unmount Image**.

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li025094718206:

   Mount the image from **install.wim** to a local directory and inject the chipset driver into the image.

   a. Open Dism++ and choose **File** > **Mount Image**.

   b. In the **Mount Image** window, perform the operations in the following figure in sequence.

      |image5|

      1: By default, **Windows Server 2016 SERVERSTANDARDCORE** is selected. You can also select other versions from the drop-down list as needed.

      2: Select **install.wim** in the **sources** folder shown in :ref:`3 <en-us_topic_0108486964__en-us_topic_0106538741_li13296014152612>`.

      3: Select an empty folder, for example, **tmp1**.

   c. When the image status changes to **Ready**, click **Open session**.

   d. Add the driver by performing :ref:`4.d <en-us_topic_0108486964__en-us_topic_0106538741_li1949712487312>` to :ref:`4.e <en-us_topic_0108486964__en-us_topic_0106538741_li1024418186448>`.

#. .. _en-us_topic_0108486964__en-us_topic_0106538741_li142715295918:

   Save the added driver and unmount the image by performing :ref:`5 <en-us_topic_0108486964__en-us_topic_0106538741_li1289027122520>`.

.. |image1| image:: /_static/images/en-us_image_0110257883.png
.. |image2| image:: /_static/images/en-us_image_0110257885.png
.. |image3| image:: /_static/images/en-us_image_0110258148.png
.. |image4| image:: /_static/images/en-us_image_0107231695.png
.. |image5| image:: /_static/images/en-us_image_0110258270.png
