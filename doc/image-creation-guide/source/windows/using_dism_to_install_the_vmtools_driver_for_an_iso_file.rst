:original_name: en-us_topic_0000001380021690.html

.. _en-us_topic_0000001380021690:

Using Dism++ to Install the VMTools Driver for an ISO File
==========================================================

Scenario
--------

Windows uses IDE disks and VirtIO NICs. Before registering an image on the cloud platform, integrate VirtIO drivers into the Windows ISO file. Typically, an ISO file contains all the files that would be included on an optical disc. Some software can be installed only from a CD-ROM drive. So, a virtual CD-ROM drive is required.

This section describes how to install the VMTools driver for an ISO file using Dism++.

Prerequisites
-------------

You have obtained an ISO file.

.. note::

   The ISO file name can contain only letters, digits, hyphens (-), and underscores (_). If the name does not meet the requirements, change it.

Procedure
---------

#. .. _en-us_topic_0000001380021690__en-us_topic_0000001408960221_li7344112816270:

   Download VMTools matching the OS and decompress it on the local PC.

#. .. _en-us_topic_0000001380021690__en-us_topic_0000001408960221_li159314251271:

   Decompress the **vmtools-windows.zip** file downloaded in :ref:`1 <en-us_topic_0000001380021690__en-us_topic_0000001408960221_li7344112816270>` to obtain **vmtools-windows.iso**, and then decompress **vmtools-windows.iso** to obtain the **vmtools-windows** folder.


   .. figure:: /_static/images/en-us_image_0000001361103768.png
      :alt: **Figure 1** vmtools-windows folder

      **Figure 1** vmtools-windows folder

#. Decompress the ISO image file, and copy the **vmtools-windows** folder obtained in :ref:`2 <en-us_topic_0000001380021690__en-us_topic_0000001408960221_li159314251271>` to the same directory as the **boot** folder in the ISO image file.


   .. figure:: /_static/images/en-us_image_0000001411143773.png
      :alt: **Figure 2** ISO image file

      **Figure 2** ISO image file
