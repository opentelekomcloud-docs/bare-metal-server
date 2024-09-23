:original_name: en-us_topic_0000001163136431.html

.. _en-us_topic_0000001163136431:

Uninstalling the NPU Driver and Firmware
========================================

**Procedure**

You can uninstall the driver and firmware in any sequence. Replace the asterisk (``*``) with an actual package name in commands.

#. Log in to the OS as the **root** user.
#. You can use either of the following methods to uninstall the driver and firmware.

   -  Run the following command in the directory where the \*\ **.run** package is stored, for example, **/opt**:

      **./*.run --uninstall**

   -  Run the following command in any directory:

      **bash** *{install_path}*/*{package_name}*\ **/script/uninstall.sh**

      .. note::

         -  **npu-smi** indicates the tool version, and **Version** indicates the NPU driver version.
         -  For details about other **npu-smi** commands, see `Atlas 800 AI Training Server npu-smi Command Reference (Model 9000) <https://support.huawei.com/enterprise/en/doc/EDOC1100150911>`__.

      3. If no error information is displayed, the uninstallation is successful. You can determine whether to restart the OS based on the prompt information.
