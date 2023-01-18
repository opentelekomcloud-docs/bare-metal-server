:original_name: en-us_topic_0131700233.html

.. _en-us_topic_0131700233:

Making Preparations
===================

You can use Dism++ to inject drivers into an ISO file. Then, install software such as Cloudbase-Init and bms-network-config to the VM created from the ISO image.

Before installing server drivers, you need to:

#. Prepare a Windows ISO image file of the required version on the local Windows jump server.

#. Install Dism++ on the local Windows jump server.

#. Download FusionServer server drivers to the local Windows jump server by referring to :ref:`Preparing Hardware and Software <en-us_topic_0081116571>`.

   Examples:

   -  Windows Server 2012 R2: **FusionServer iDriver-Win2K12R2-Driver-V113.zip**
   -  Windows Server 2016: **FusionServer iDriver-Win2K16-Driver-V115.zip**

#. Decompress the .zip driver package to obtain the .iso driver file.

   -  Windows Server 2012 R2: Decompress **FusionServer iDriver-Win2K12R2-Driver-V113.zip** to obtain the **onboard_driver_win2k12r2.iso** file.
   -  Windows Server 2016: Decompress **FusionServer iDriver-Win2K16-Driver-V115.zip** to obtain the **onboard_driver_win2k16.iso** file.
