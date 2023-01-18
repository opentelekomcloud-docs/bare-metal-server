:original_name: en-us_topic_0000001117256554.html

.. _en-us_topic_0000001117256554:

Upgrading Ascend 910 NPU Firmware
=================================

You can upgrade the firmware of the Ascend 910 NPU for Atlas 800 (model 9000) training servers. This section uses the **A800-9000-npu-firmware\_**\ *x.x.x*\ **.run** package as an example to describe how to upgrade NPU firmware.

**Procedure**

#. Obtain the software package **A800-9000-npu-firmware\_**\ *x.x.x*\ **.run** by referring to :ref:`Preparing for Upgrade <en-us_topic_0000001117096650>`.
#. Log in to the Atlas 800 (model: 9000) training server as the **root** user.
#. Upload **A800-9000-npu-firmware\_**\ *x.x.x*\ **.run** to any directory in the OS, for example, **/opt**.
#. Go to the directory where **A800-9000-npu-firmware\_**\ *x.x.x*\ **.run** is stored.

**cd /**\ *opt*

5. Run the following command to change the permissions on **A800-9000-npu-firmware\_**\ *x.x.x*\ **.run**:

**chmod u+x** *A800-9000-npu-firmware_x.x.x.run*

6. Run the **./A800-9000-npu-firmware\_**\ *x.x.x*\ **.run --check** command to check the consistency and integrity of the software package.
7. Upgrade the firmware.

You can run the **./A800-9000-npu-firmware\_**\ *x.x.x*\ **.run --upgrade** command to perform the upgrade.

If information similar to the following is displayed, the upgrade is successful:

.. code-block::

   Firmware package install success! Reboot needed for installation/upgrade to take effect!

.. note::

   -  *x.x.x* indicates the firmware version.
   -  The logs generated during the upgrade are recorded in the **/var/log/ascend_seclog/ascend_install.log** file. You can run the **vim /var/log/ascend_seclog/ascend_install.log** command to open the log file.

8. .. _en-us_topic_0000001117256554__en-us_topic_0000001116414308_li156777301474:

   Reboot the system.

**reboot**

9. Check the firmware version.

In the installation directory, run the following command to check whether the firmware version is correct:

**cat version.info**

.. note::

   -  The default installation directory is **/usr/local/Ascend/firmware**.
