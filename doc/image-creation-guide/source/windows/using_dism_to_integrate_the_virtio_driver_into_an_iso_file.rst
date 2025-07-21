:original_name: en-us_topic_0000001380021690.html

.. _en-us_topic_0000001380021690:

Using Dism++ to Integrate the VirtIO Driver into an ISO File
============================================================

Scenario
--------

Windows uses IDE disks and VirtIO NICs. Before registering an image on the cloud platform, integrate VirtIO drivers into the Windows ISO file. Typically, an ISO file contains all the files that would be included on an optical disc. Some software can be installed only from a CD-ROM drive. So, a virtual CD-ROM drive is required.

This section describes how to integrate the VirtIO driver into an ISO file using Dism++.

Prerequisites
-------------

You have obtained an ISO file.

.. note::

   The ISO file name can contain only letters, digits, hyphens (-), and underscores (_).

Procedure
---------

#. .. _en-us_topic_0000001380021690__en-us_topic_0000001408960221_li7344112816270:

   Download a VirtIO driver package.

   Other versions:

   https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/

#. Decompress **virtio-win.iso** downloaded in :ref:`1 <en-us_topic_0000001380021690__en-us_topic_0000001408960221_li7344112816270>` to obtain the **virtio-win-0.1.189** folder.


   .. figure:: /_static/images/en-us_image_0000001995402830.png
      :alt: **Figure 1** virtio-win-0.1.189 folder

      **Figure 1** virtio-win-0.1.189 folder

#. Decompress an ISO file and copy all files in the **virtio-win-0.1.189** folder to the parent node of the ISO file. The copied files will be at the same directory level as the **boot** folder.
