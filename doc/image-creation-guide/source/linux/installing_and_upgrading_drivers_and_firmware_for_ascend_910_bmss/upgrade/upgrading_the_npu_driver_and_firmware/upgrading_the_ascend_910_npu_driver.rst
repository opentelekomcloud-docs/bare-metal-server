:original_name: en-us_topic_0000001163456407.html

.. _en-us_topic_0000001163456407:

Upgrading the Ascend 910 NPU Driver
===================================

**Scenarios**

You can upgrade the driver of the Ascend 910 NPU for Atlas 800 (model 9000) training servers.

This section uses the **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run** package as an example to describe how to upgrade the NPU driver.

.. note::

   -  Driver upgrade does not change the system username or password.

**Impacts on the System**

The system will be reset during the driver upgrade of Atlas 800 (model 9000) training servers. This will cause service interruptions. To reduce impacts on services, switch services to other nodes before the upgrade.

**Procedure**

#. Obtain the driver package **A800-9000-npu-driver\_**\ *x.x.x*\ \_\ **euleros2.8-aarch64.run** by referring to :ref:`Preparing for Upgrade <en-us_topic_0000001117096650>`.
#. Log in to the Atlas 800 (model: 9000) training server as the **root** user.
#. Upload **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run** to any directory in the Linux OS, for example, **/opt**.
#. Go to the directory where **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run** is stored.

**cd /**\ *opt*

5. Run the following command to change the permissions on **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run**:

**chmod u+x** **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run**

6. Run the **./A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run** **--check** command to check the consistency and integrity of the software package.
7. Upgrade the driver.

You can run the **./A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run --upgrade** command to perform the upgrade.

If information similar to the following is displayed, the upgrade is successful:

.. code-block::

   Driver package install success! Reboot needed for installation/upgrade to take effect!

.. note::

   -  During the driver upgrade, the dynamic library **libdcmi.so** and header file **dcmi_interface_api.h** are copied to the **/usr/local/dcmi/** directory.
   -  The logs generated during the upgrade are recorded in the **/var/log/ascend_seclog/ascend_install.log** file.

8. .. _en-us_topic_0000001163456407__en-us_topic_0000001116254404_li856711712919:

   Reboot the system.

**reboot**

9. Check the driver version.

In the installation directory, run the following command to check whether the driver version is correct:

**cat version.info**

.. note::

   -  The default installation directory is **/usr/local/Ascend/driver**.

-  If you cannot log in to the OS after the upgrade, contact technical support.
-  If the upgrade failed or you have upgraded to an incorrect version, perform the upgrade again. If the issue persists, record the fault information and contact technical support.
