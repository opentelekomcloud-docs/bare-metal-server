:original_name: en-us_topic_0081116779.html

.. _en-us_topic_0081116779:

Creating a VM and Installing an OS (Windows)
============================================

This section uses Windows Server 2012 R2 as an example to describe how to create a Windows VM. The procedure is also applicable to other Windows OSs. The screenshots in the following steps are for reference only.

#. Log in to the host, upload the ISO file generated in :ref:`Generating a New ISO File <en-us_topic_0131700759>` to it, and start virt-manager.

   .. code-block:: console

      [root@localhost Desktop]# virt-manager
      [root@localhost Desktop]#

#. Click **Create a new virtual machine**. In the **New VM** dialog box, select **Local install media (ISO image or CDROM)** and click **Forward**.

#. Select the ISO image stored on the host, and select its OS type and version. In this example, the OS type and version are automatically detected by the system.

   |image1|

#. Configure the VM memory and CPU.

   -  Memory (RAM): 4096 MiB
   -  CPUs: 4

#. Configure the VM storage by specifying the disk image size. (The image cannot be too large.)

   |image2|

#. Click **Manage** and select a storage path, for example, **/var/lib/libvirt/images**.

   |image3|

   Click |image4| to create a storage volume. Set **Name** (suffix **.img** is recommended so that the image can be compressed if it is large) and select **raw** (recommended) for **Format**.

   |image5|

   Click **Finish**. In the displayed storage volume list, select the created storage volume and click **Choose Volume**.

   |image6|

#. Enter a name for the VM and select **Customize configuration before install**.

   |image7|

#. In the navigation pane on the left, choose **NIC**. In the right pane, select **e1000** for **Device model**, and click **Apply**.

   |image8|

#. Click **Begin Installation**. virt-manager creates the VM as you configured.

#. Install Windows on the VM.

   Configure the language, time zone, currency, and other settings by referring to :ref:`Installing a Windows OS and the VirtIO Driver <en-us_topic_0000001289583000>`. Activate the OS using the Windows Server 2012 R2 product key.

.. |image1| image:: /_static/images/en-us_image_0110260257.png
.. |image2| image:: /_static/images/en-us_image_0110260335.png
.. |image3| image:: /_static/images/en-us_image_0110260417.png
.. |image4| image:: /_static/images/en-us_image_0094568906.png
.. |image5| image:: /_static/images/en-us_image_0110260609.png
.. |image6| image:: /_static/images/en-us_image_0110260621.png
.. |image7| image:: /_static/images/en-us_image_0110260645.png
.. |image8| image:: /_static/images/en-us_image_0110260774.png
