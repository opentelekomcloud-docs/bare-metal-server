:original_name: en-us_topic_0140740386.html

.. _en-us_topic_0140740386:

Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 BMS
=============================================================

Scenarios
---------

After a GPU-accelerated P2 BMS (using the physical.p2.large flavor) is created, the NVIDIA GPU driver and CUDA Toolkit must be installed on it for computing acceleration.

Prerequisites
-------------

-  An EIP has been bound to the BMS.
-  You have obtained the required driver installation packages.

   .. table:: **Table 1** Download paths for the NVIDIA GPU driver and CUDA Toolkit

      +------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
      | OS         | Driver                                                                     | How to Obtain                                                                                     |
      +============+============================================================================+===================================================================================================+
      | CentOS 7.4 | NVIDIA GPU driver installation package: **NVIDIA-Linux-x86_64-384.81.run** | https://www.nvidia.com/download/driverResults.aspx/124722/en-us                                   |
      +------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
      |            | CUDA Toolkit installation package: **cuda_9.0.176_384.81_linux.run**       | https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run |
      +------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

CentOS 7.4
----------

#. Log in to the target BMS and run the following command to switch to user **root**:

   **su** **root**

#. (Optional) If the **gcc**, **gcc-c++**, **make**, and **kernel-devel** dependency packages do not exist, run the following commands to install the gcc, gcc-c++, make, and kernel-devel tools:

   **yum** **install** **gcc**

   **yum** **install** **gcc-c++**

   **yum** **install** **make**

   **yum** **install** **kernel-devel-`uname** **-r\`**

#. (Optional) Add the Nouveau driver to the blacklist.

   If the Nouveau driver has been installed and loaded, perform the following operations to add the Nouveau driver to the blacklist to avoid conflicts:

   a. Add **blacklist nouveau** to the end of the **/etc/modprobe.d/blacklist.conf** file.

   b. Run the following commands to back up and reconstruct initramfs:

      **mv** **/boot/initramfs-$(uname** **-r).img** **/boot/initramfs-$(uname** **-r).img.bak**

      **dracut** **-v** **/boot/initramfs-$(uname** **-r).img** **$(uname** **-r)**

   c. Run the **reboot** command to restart the BMS.

#. (Optional) If the X service is running, run the **systemctl** **set-default** **multi-user.target** command and restart the BMS to enter multi-user mode.

#. (Optional) Install the NVIDIA GPU driver.

   If you selected a specified version of NVIDIA GPU driver rather than a version contained in the CUDA Toolkit, perform this step.

   a. Download NVIDIA GPU driver installation package **NVIDIA-Linux-x86_64-**\ *xxx.yy*\ **.run** from https://www.nvidia.com/Download/index.aspx?lang=en, and upload this package to the **/tmp** directory on the BMS.


      .. figure:: /_static/images/en-us_image_0143426393.png
         :alt: **Figure 1** Searching for the NVIDIA GPU driver package (CentOS 7.4)

         **Figure 1** Searching for the NVIDIA GPU driver package (CentOS 7.4)

   b. Run the following command to install the NVIDIA GPU driver:

      **sh** **./NVIDIA-Linux-x86_64-**\ *xxx.yy*\ **.run**

   c. Run the following command to delete the installation package:

      **rm** **-f** **NVIDIA-Linux-x86_64-**\ *xxx.yy*\ **.run**

#. Install the CUDA Toolkit.

   a. Download CUDA Toolkit installation package **cuda\_**\ *a.b.cc_xxx.yy*\ **\_linux.run** from https://developer.nvidia.com/cuda-downloads, and upload this package to the **/tmp** directory on the BMS.

   b. Run the following command to change the permission to the installation package:

      **chmod** **+x** **cuda\_**\ *a.b.cc_xxx.yy*\ **\_linux.run**

   c. Run the following command to install the CUDA Toolkit:

      **./cuda\_**\ *a.b.cc_xxx.yy*\ **\_linux.run** **-toolkit** **-samples** **-silent** **-override** **--tmpdir=/tmp/**

   d. Run the following command to delete the installation package:

      **rm** **-f** **cuda**\ **\_**\ *\ a.b.cc_xxx.yy*\ **\_linux.run**

   e. Run the following commands to check whether the installation is successful:

      **cd** **/usr/local/cuda/samples/1_Utilities/deviceQueryDrv/**

      **make**

      **./deviceQueryDrv**

      If the command output contains "Result = PASS", the CUDA Toolkit and the NVIDIA GPU driver have been installed successfully.
