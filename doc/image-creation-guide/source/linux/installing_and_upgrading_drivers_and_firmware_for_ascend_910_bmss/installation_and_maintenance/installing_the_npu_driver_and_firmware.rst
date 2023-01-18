:original_name: en-us_topic_0000001117096648.html

.. _en-us_topic_0000001117096648:

Installing the NPU Driver and Firmware
======================================

**Prerequisites**

Preparations for the installation have been made by referring to :ref:`Preparations for Installation <en-us_topic_0000001163136427>`.

**Procedure**

Install a driver and then the firmware. The procedures for installing a driver and firmware are the same. Replace the asterisk (``*``) with an actual package name in commands.

#. Log in to the OS as the **root** user and upload the \*\ **.run** package to any directory, for example, **/opt**.

#. Grant the execute permission on the package to the installation user.

   You can run the **ls -l** command in the directory where the package is stored to check whether the installation user has the permission to execute the file. If it does not, run the following command to grant the permission:

   **chmod +x \*.run**

3. Run the following command to check the consistency and integrity of the package:

   **./*.run --check**

4. Install the software package.

If you want to install the software package in a specified directory, for example, **/test/HiAI/**, run the **./*.run --full --install-path=**\ */test/HiAI/* command.

If you want to install the software package in the default directory, run the **./*.run -full** command.

The following uses EulerOS 2.8 as an example to describe how to install a driver. (The method for installing firmware package is the same.) Go to the directory where the software package is stored and run the **./A800-9000-npu-driver\_**\ *xxx*\ **\_euleros2.8-aarch64.run --full --install-for-all** command. (If the command does not contain **--install-for-all**, a certificate error may be reported when a non-root user uses the driver.)

.. note::

   -  Drivers can be installed on VMs. Firmware can only be installed on BMSs.

   -  If the **root** user is specified as an execution user, **--install-for-all** must be contained in the command.
   -  Default installation directory: **/usr/local/Ascend**
   -  Installation log directory: **/var/log/ascend_seclog/ascend_install.log**
   -  The installation directory, installation command, and user information are stored in **/etc/ascend_install.info** after the installation complete.

5. .. _en-us_topic_0000001117096648__en-us_topic_0000001163414149_li1930420453516:

   For a general driver package, if the following information is displayed, DKMS is not installed and the default kernel source code directory **/lib/modules/`uname -r`/build** does not exist.

.. code-block::

   [WARNING]rebuild ko has something wrong, detail in /var/log/ascend_seclog/ascend_rebuild.log Do you want to try build driver after input kernel absolute path? [y/n]:

If you want to continue the installation, enter **y**.

When the following information is displayed, enter the path of the kernel source code, for example, **/lib/modules/`uname -r`/build-bak**.

.. code-block::

   Please input your kernel absolute path:

Press **Enter** to continue with the installation.

.. note::

   -  If DKMS and related components such as kernel-header and kernel-devel have been installed, the system will automatically compile driver source code and install the driver.
   -  If DKMS is not installed but the default kernel source code directory **/lib/modules/`uname -r`/build** exists, the kernel will be automatically used for driver compilation.

6. If information similar to the following is displayed, the installation is successful:

   -  Driver: **Driver package install success!** **Reboot needed for installation/upgrade to take effect!**
   -  Firmware: **Firmware package install success!** **Reboot needed for installation/upgrade to take effect!**

7. Restart the OS.
8. Check the driver version.

In the software package installation directory, for example, the default directory of the **root** user **/usr/local/Ascend/$**\ {*package_name*}, run the following command to check the driver version:

**cat version.info**

.. code-block::

   Version=1.73.T105.0.B050

9. Check the firmware version.

**/usr/local/Ascend/driver/tools/upgrade-tool --device_index -1 --component -1 --version**

.. code-block::

   Get component version(1.73.5.0.b050) succeed for deviceId(0), componentType(0).          {"device_id":0, "component":nve, "version":1.73.5.0.b050}  Get component version(1.73.5.0.b050) succeed for deviceId(0), componentType(3).          {"device_id":0, "component":uefi, "version":1.73.5.0.b050}  Get component version(1.73.5.0.b050) succeed for deviceId(0), componentType(8).          {"device_id":0, "component":imu, "version":1.73.5.0.b050}  Get component version(1.73.105.0.b050) succeed for deviceId(0), componentType(9).          {"device_id":0, "component":imp, "version":1.73.105.0.b050}

10. Run the **npu-smi info** command to check whether the **npu-smi** tool is successfully installed.

The tool is installed successfully if the following information is displayed. Otherwise, the installation fails. Contact technical support.

|image1|

.. note::

   -  **npu-smi** indicates the tool version, and **Version** indicates the NPU driver version.
   -  For details about other **npu-smi** commands, see `Atlas 800 AI Training Server npu-smi Command Reference (Model 9000) <https://support.huawei.com/enterprise/en/doc/EDOC1100150911>`__.

**Important Notes**

-  Logs are recorded based on the system time. NPU synchronizes the system time. To change the system time, run the **date** command.

   For example, to set the system time to **17:55:55**, run the **date -s 17:55:55** command.

.. |image1| image:: /_static/images/en-us_image_0000001163418777.png
