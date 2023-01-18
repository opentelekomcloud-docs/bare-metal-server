:original_name: en-us_topic_0081116725.html

.. _en-us_topic_0081116725:

Creating a Linux VM
===================

This section uses Oracle Linux 6.8 as an example to describe how to create a Linux VM. The procedure is also applicable to other Linux OSs. The screenshots in the following steps are for reference only.

#. Download the required ISO image to the host. Alternatively, you can also download the image to your local PC, use Xshell to remotely connect to the host, and upload the image to the host.

#. Log in to the host and run the **virt-manager** command to start virt-manager.

#. Click **Create a new virtual machine**. In the **New VM** dialog box, select **Local install media (ISO image or CDROM)**. Click **Forward**.

   |image1|

#. Select an ISO image, its OS type, and version. Click **Forward**.

#. Configure the VM memory and CPU. Click **Forward**.

   -  Memory (RAM): 4096 MiB
   -  CPUs: 4

#. Configure the VM storage by specifying the disk image size.

   .. note::

      -  The image cannot be too large. For Oracle Linux 7.3/Red Hat 7.3 Linux, you are advised to set the image size to a value no greater than 6 GB. For Ubuntu 16.04 ARM, you are advised to select **Select managed or other existing storage** and then select a 150 GB QCOW2 image.
      -  The total size of the disk image and memory (150 MB) cannot exceed the memory size of the BMS to be created. Otherwise, the BMS will fail to be created.

   |image2|

#. Click **Manage** and select a storage path, for example, **/home/h**.

   |image3|

   Click |image4| to create a storage volume. Set **Name** (suffix **.img** is recommended so that the image can be compressed if it is large) and select **raw** (recommended) for **Format**.

   |image5|

   Click **Finish**. In the displayed storage volume list, select the created storage volume and click **Choose Volume**.

   |image6|

#. Enter a name for the VM, for example, **oracle6.8** and select **Customize configuration before install**. For Ubuntu 16.04 ARM, you are advised to select NAT in **Advanced options**. Click **Finish**.

   |image7|

#. (Optional) For Ubuntu 16.04 ARM, skip this step. In the navigation pane on the left, choose **NIC**. In the right pane, select **e1000** (Gigabit network adapter) for **Device model**, and click **Apply**.

   |image8|

#. (Optional) This step is used to set the UEFI boot mode and is only necessary for SUSE 12 and KunLun servers for the HANA solution. In the navigation pane on the left, choose **Overview**. In the right pane, select a UEFI option for **Firmware**.

   |image9|

#. Click **Begin Installation**. virt-manager creates the VM as you configured.

#. Wait for the VM to start and install the OS. You need to configure the language, time zone, and other settings.

.. |image1| image:: /_static/images/en-us_image_0110197956.png
.. |image2| image:: /_static/images/en-us_image_0110199604.png
.. |image3| image:: /_static/images/en-us_image_0110202976.png
.. |image4| image:: /_static/images/en-us_image_0094568724.png
.. |image5| image:: /_static/images/en-us_image_0110200025.png
.. |image6| image:: /_static/images/en-us_image_0110202987.png
.. |image7| image:: /_static/images/en-us_image_0110920635.png
.. |image8| image:: /_static/images/en-us_image_0110203057.png
.. |image9| image:: /_static/images/en-us_image_0110203258.png
