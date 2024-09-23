:original_name: en-us_topic_0000001117096646.html

.. _en-us_topic_0000001117096646:

Checking the OS and Kernel
==========================

:ref:`Table 1 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table0698102233514>` and :ref:`Table 2 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table107206229353>` list the OSs and kernels required by different driver and firmware packages.

.. _en-us_topic_0000001117096646__en-us_topic_0000001116251562_table0698102233514:

.. table:: **Table 1** OS and kernel versions required by binary driver packages

   +--------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
   | BMS                      | OS              | Kernel                                                                                                                                                                                                                                                                                                  | GCC Version     |
   +==========================+=================+=========================================================================================================================================================================================================================================================================================================+=================+
   | Atlas 800 9000 (AArch64) | Ubuntu 18.04    | 4.15.0-45-generic                                                                                                                                                                                                                                                                                       | 7.4.0           |
   |                          |                 |                                                                                                                                                                                                                                                                                                         |                 |
   |                          |                 | Note:                                                                                                                                                                                                                                                                                                   |                 |
   |                          |                 |                                                                                                                                                                                                                                                                                                         |                 |
   |                          |                 | If the kernel does not match the OS, install DKMS to compile the driver source code before you install the driver. For details about how to install DKMS, see `Driver Source Code Compilation <https://support.huawei.com/enterprise/en/doc/EDOC1100150910/9ce92ba0/driver-source-code-compilation>`__. |                 |
   +--------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | EulerOS 2.8     | 4.19.36-vhulk1907.1.0.h475                                                                                                                                                                                                                                                                              | 7.3.0           |
   +--------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | CentOS 7.6      | 4.14.0-115.el7a.0.1.aarch64                                                                                                                                                                                                                                                                             | ``-``           |
   +--------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | BC_Linux 7.6    | 4.19                                                                                                                                                                                                                                                                                                    | ``-``           |
   +--------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

.. _en-us_topic_0000001117096646__en-us_topic_0000001116251562_table107206229353:

.. table:: **Table 2** OS and kernel versions required by general driver packages

   +--------------------------+------------------------------------------------------------------------------+---------------------------------------+-----------------+
   | BMS                      | OS                                                                           | Kernel                                | GCC Version     |
   +==========================+==============================================================================+=======================================+=================+
   | Atlas 800 9000 (AArch64) | CentOS 8.2                                                                   | 4.18.X                                | 8.3.1           |
   |                          |                                                                              |                                       |                 |
   |                          |                                                                              | Note:                                 |                 |
   |                          |                                                                              |                                       |                 |
   |                          |                                                                              | The kernel can be upgraded to 5.6.14. |                 |
   +--------------------------+------------------------------------------------------------------------------+---------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | BC_Linux 7.6                                                                 | 4.19                                  | ``-``           |
   +--------------------------+------------------------------------------------------------------------------+---------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | Kylin OS V10SP1                                                              | 4.19.90-17.ky10.aarch64               | 8.3.1-4.5       |
   |                          |                                                                              |                                       |                 |
   |                          | Note:                                                                        |                                       |                 |
   |                          |                                                                              |                                       |                 |
   |                          | Kylin OS V10SP1 is only supported by NPU driver 21.0.rc1 and later versions. |                                       |                 |
   +--------------------------+------------------------------------------------------------------------------+---------------------------------------+-----------------+
   | Atlas 800 9000 (AArch64) | BC_Linux 7.7                                                                 | 4.19.25-203.e17.bclinux.aarch64       | 4.8.5           |
   |                          |                                                                              |                                       |                 |
   |                          | Note:                                                                        |                                       |                 |
   |                          |                                                                              |                                       |                 |
   |                          | BC_Linux 7.7 is only supported by NPU driver 21.0.rc1 and later versions.    |                                       |                 |
   +--------------------------+------------------------------------------------------------------------------+---------------------------------------+-----------------+

#. Check the OS version.

Run the **uname -m && cat /etc/*release** command to query the OS version and architecture.

The OS version and architecture must comply with :ref:`Table 1 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table0698102233514>` or :ref:`Table 2 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table107206229353>`.

2. Check general driver packages.

-  Check whether the **make** tool has been installed. Run the **make -v** command. If a **make** tool version is displayed, the **make** tool has been installed.
-  Ensure that at least either of the following conditions is met.

   -  Dependent tools such as DKMS have been installed. For details about how to install DKMS, see `Driver Source Code Compilation <https://support.huawei.com/enterprise/en/doc/EDOC1100150910/9ce92ba0/driver-source-code-compilation>`__.
   -  The default source code directory (**/lib/modules/`uname -r`/build**) of the kernel exists. Run the **ls /lib/modules/`uname -r`/build** command to check whether the directory exists.

      -  If it does, the kernel is automatically used to compile the driver.
      -  If it does not, you can provide it during driver installation. For details, see :ref:`5 <en-us_topic_0000001117096648__en-us_topic_0000001163414149_li1930420453516>`.

3. Check the OS kernel version.

Run the **uname -r** command to query the kernel version.

-  For a binary driver package, the kernel version must comply with :ref:`Table 1 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table0698102233514>`. If it does not, perform either of the following operations:

   -  Compile the source code again. For details, see `Driver Source Code Compilation <https://support.huawei.com/enterprise/en/doc/EDOC1100150910/9ce92ba0/driver-source-code-compilation>`__.
   -  Check whether the driver package has been installed as instructed in :ref:`Check whether the software package has been installed in the OS <en-us_topic_0000001117096646__en-us_topic_0000001116251562_li1831114154618>`. If it has not been installed, upgrade the kernel. If it has been installed, uninstall the driver package and then upgrade the kernel.

-  For a general driver package, the kernel version must comply with :ref:`Table 2 <en-us_topic_0000001117096646__en-us_topic_0000001116251562_table107206229353>`. Otherwise, the driver package may fail to be installed or driver functions may be affected.

4. .. _en-us_topic_0000001117096646__en-us_topic_0000001116251562_li1831114154618:

   Check whether NPU driver and firmware packages have ever been installed in the OS.

If you need to upgrade the kernel, ensure that NPU driver and firmware packages have never been installed in the OS. Otherwise, the packages to be used will fail to be started after the kernel is upgraded. You can rectify this issue by referring to `What Do I Do If the Software Package Is Unavailable Because It Is Not Uninstalled When Updating the OS Kernel? <https://support.huawei.com/enterprise/en/doc/EDOC1100150910/ebee1b36/what-do-i-do-if-the-software-package-is-unavailable-because-it-is-not-uninstalled-when-updating-the-os-kernel>`__ Run the **lsmod|grep drv** command to check whether the packages have been installed.

-  If no information is displayed, the packages have never been installed. You can upgrade the kernel without additional actions.
-  If driver information is displayed, the software packages have been installed. Uninstall them and then upgrade the kernel. For details, see :ref:`Uninstalling the NPU Driver and Firmware <en-us_topic_0000001163136431>`.
