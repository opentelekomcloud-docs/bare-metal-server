:original_name: en-us_topic_0081116754.html

.. _en-us_topic_0081116754:

Overview
========

If you want to use a private BMS image, you can use an external image file to create one. This document describes the private image creation procedure (including creating a VM and installing the OS, software, and drivers on the VM) and uses multiple OSs as examples to provide instructions for you to create a private image. You can also install software as needed to customize your private image.

After you have created an image file, you need to register it on the cloud platform. For details, see "Creating a Private Image from an External Image File" in *Bare Metal Server User Guide*. After successful registration, you can select this private image when creating a BMS.

Image Creation Process
----------------------

The image creation process is as follows:


.. figure:: /_static/images/en-us_image_0164137586.png
   :alt: **Figure 1** Process of image creation

   **Figure 1** Process of image creation

.. table:: **Table 1** Creation process description

   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Procedure                               | Description                                                                                                                                      |
   +=========================================+==================================================================================================================================================+
   | Making preparations                     | Before you create an image, prepare:                                                                                                             |
   |                                         |                                                                                                                                                  |
   |                                         | -  A Linux physical server or VM to be used as a host                                                                                            |
   |                                         | -  Software packages, such as the OS ISO file package, SDI driver package, and bms-network-config package                                        |
   |                                         | -  Tools, such as the cross-platform remote access tool and file transfer tool                                                                   |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Creating a VM                           | Use virt-manager to create a VM.                                                                                                                 |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Installing an OS on the VM              | Install an OS on the VM as required.                                                                                                             |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Configuring the VM environment          | Software packages need to be uploaded to the VM. Therefore, you need to configure the VM environment so that the VM can connect to the Internet. |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Configuring the VM                      | Linux:                                                                                                                                           |
   |                                         |                                                                                                                                                  |
   |                                         | -  Install and configure Cloud-Init.                                                                                                             |
   |                                         | -  Modify the hardware device driver that boots the OS.                                                                                          |
   |                                         | -  Install bms-network-config.                                                                                                                   |
   |                                         | -  (Optional) Install the SDI driver.                                                                                                            |
   |                                         | -  (Optional) Install the Hi1822 driver.                                                                                                         |
   |                                         | -  (Optional) Install the IB driver.                                                                                                             |
   |                                         | -  (Optional) Install x86 V5/TaiShan server drivers.                                                                                             |
   |                                         | -  (Optional) Install multipath software.                                                                                                        |
   |                                         | -  Perform security configuration.                                                                                                               |
   |                                         | -  Configure remote login.                                                                                                                       |
   |                                         | -  Configuring automatic root partition expansion                                                                                                |
   |                                         |                                                                                                                                                  |
   |                                         | Windows:                                                                                                                                         |
   |                                         |                                                                                                                                                  |
   |                                         | -  Install x86 V5 server drivers.                                                                                                                |
   |                                         | -  Install Cloudbase-Init.                                                                                                                       |
   |                                         | -  Install bms-network-config.                                                                                                                   |
   |                                         | -  (Optional) Install the SDI driver.                                                                                                            |
   |                                         | -  Set the Windows time zone.                                                                                                                    |
   |                                         | -  Set the Windows virtual memory.                                                                                                               |
   |                                         | -  (Optional) Configure automatic windows update.                                                                                                |
   |                                         | -  Configure the SID.                                                                                                                            |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Stopping the VM and obtaining the image | Stop the VM and obtain the image file. If the generated image file is too large, you can compress it.                                            |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Converting the image format             | For BMS, the image format can only be ZVHD2. After obtaining an image file, convert its format to ZVHD2.                                         |
   +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Supported OSs
-------------

BMS images support the following OSs:

.. _en-us_topic_0081116754__table158691643112312:

.. table:: **Table 2** x86 OSs

   +--------------+-------------------------------------------+-------------------------------------------------------+
   | OS Type      | OS Version                                | Kernel Version                                        |
   +==============+===========================================+=======================================================+
   | RedHat       | Red Hat Linux Enterprise 6.5 64bit        | 2.6.32-431.el6.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 6.7 64bit        | 2.6.32-573.el6.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 6.8 64bit        | 2.6.32-642.el6.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 6.9 64bit        | 2.6.32-696.e16.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 7.2 64bit        | 3.10.0-327.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 7.3 64bit        | 3.10.0-514.el7.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 7.4 64bit        | 3.10.0-693.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Red Hat Linux Enterprise 7.5 64bit        | 3.10.0-862.el7.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | SUSE         | SUSE Linux Enterprise Server 11 SP4 64bit | 3.0.101-63-default                                    |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | SUSE Linux Enterprise Server 12 SP1 64bit | 3.12.49-11-default                                    |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | SUSE Linux Enterprise Server 12 SP2 64bit | 4.4.21-69-default                                     |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | SUSE Linux Enterprise Server 12 SP3 64bit | 4.4.73-5-default                                      |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | Oracle Linux | Oracle Linux Server release 6.8 64bit     | 4.1.12-37.4.1.e16uek.x86_64                           |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Oracle Linux Server release 6.9 64bit     | 4.1.12-61.1.28.e16uek.x86_64                          |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Oracle Linux Server release 7.2 64bit     | 3.10.0-327.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Oracle Linux Server release 7.3 64bit     | 3.10.0-327.el7.x86_64 or 4.1.12-61.1.18.e17uek.x86_64 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Oracle Linux Server release 7.4 64bit     | 4.1.12-94.3.9.e17uek.x86_64                           |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | EulerOS      | EulerOS 2.2 64bit                         | 3.10.0-327.44.58.35.x86_64                            |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | EulerOS 2.3 64bit                         | 3.10.0-514.44.5.10.h142.x86_64                        |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | CentOS       | CentOS 6.8 64bit                          | 2.6.32-642.e16.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | CentOS 6.9 64bit                          | 2.6.32-696.e16.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | CentOS 7.2 64bit                          | 3.10.0-327.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | CentOS 7.3 64bit                          | 3.10.0-514.el7.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | CentOS 7.4 64bit                          | 3.10.0-693.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | CentOS 7.5 64bit                          | 3.10.0-862.e17.x86_64                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | Ubuntu       | Ubuntu 16.04 LTS 64bit                    | 4.4.0-21-generic x86_64                               |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Ubuntu 14.04 LTS 64bit                    | 3.13.0-24-generic                                     |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | XenServer    | XenServer 7.1 64bit                       | 4.4.x86_64                                            |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | Debian       | Debian 8.6 64bit                          | 3.16.0-4-amd64                                        |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   | Windows      | Windows Server 2012 R2 Standard 64bit     | ``-``                                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Windows Server 1709 64bit                 | ``-``                                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+
   |              | Windows Server 2016 Standard 64bit        | ``-``                                                 |
   +--------------+-------------------------------------------+-------------------------------------------------------+

.. _en-us_topic_0081116754__table117819519233:

.. table:: **Table 3** Arm OSs

   ======= =============== ==============================================
   OS Type OS Version      Kernel Version
   ======= =============== ==============================================
   CentOS  CentOS 7.6 ARM  4.14.0-115.el7a.0.1.aarch64
   EulerOS EulerOS 2.8 ARM 4.19.36-vhulk1907.1.0.h475.eulerosv2r8.aarch64
   ======= =============== ==============================================

.. note::

   When you download an SDI driver, ensure that the driver matches your kernel version.

   You can run the **uname -r** command to query the OS kernel version.
