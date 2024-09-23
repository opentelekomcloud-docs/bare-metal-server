:original_name: en-us_topic_0000001117256548.html

.. _en-us_topic_0000001117256548:

Obtaining Software Packages
===========================

Before the installation, obtain driver and firmware packages based on the OS. :ref:`Obtaining Software Packages <en-us_topic_0000001117256548>` describes the details.

.. table:: **Table 1** Software packages

   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Component       | OS                                                                                             | Software Package                                           | Execution User  |
   +=================+================================================================================================+============================================================+=================+
   | Firmware        | EulerOS 2.8/Ubuntu 18.04/CentOS 7.6/CentOS 8.2/BC_Linux 7.6/Kylin OS V10SP1/BC_Linux 7.7       | A800-9000-npu-firmware_x.x.x.run                           | root            |
   |                 |                                                                                                |                                                            |                 |
   |                 | Note:                                                                                          |                                                            |                 |
   |                 |                                                                                                |                                                            |                 |
   |                 | Kylin OS V10SP1 and BC_Linux 7.7 are only supported by NPU driver 21.0.rc1 and later versions. |                                                            |                 |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | EulerOS 2.8 (AArch64)                                                                          | A800-9000-npu-driver\_\ *x.x.x*\ \_euleros2.8-aarch64.run  | root            |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | Ubuntu 18.04 (AArch64)                                                                         | A800-9000-npu-driver\_\ *x.x.x*\ \_ubuntu18.04-aarch64.run | root            |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | CentOS 7.6 (AArch64)                                                                           | A800-9000-npu-driver\_\ *x.x.x*\ \_centos7.6-aarch64-.run  | root            |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | CentOS 8.2 (AArch64)                                                                           | A800-9000-npu-driver\_\ *x.x.x*\ \_linux-aarch64.run       | root            |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | BC_Linux 7.6 (AArch64)                                                                         | A800-9000-npu-driver\_\ *x.x.x*\ \_centos7.6-aarch64-.run  | root            |
   |                 |                                                                                                |                                                            |                 |
   |                 |                                                                                                | A800-9000-npu-driver_x.x.x_linux-aarch64.run               |                 |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | Kylin OS V10SP1 (AArch64)                                                                      | A800-9000-npu-driver\_\ *x.x.x*\ \_linux-aarch64.run       | root            |
   |                 |                                                                                                |                                                            |                 |
   |                 | Note:                                                                                          |                                                            |                 |
   |                 |                                                                                                |                                                            |                 |
   |                 | Kylin OS V10SP1 and BC_Linux 7.7 are only supported by NPU driver 21.0.rc1 and later versions. |                                                            |                 |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+
   | Driver          | BC_Linux 7.7 (AArch64)                                                                         | A800-9000-npu-driver\_\ *x.x.x*\ \_linux-aarch64.run       | root            |
   |                 |                                                                                                |                                                            |                 |
   |                 | Note:                                                                                          |                                                            |                 |
   |                 |                                                                                                |                                                            |                 |
   |                 | Kylin OS V10SP1 and BC_Linux 7.7 are only supported by NPU driver 21.0.rc1 and later versions. |                                                            |                 |
   +-----------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------+

.. note::

   -  *x.x.x* indicates the version number.
   -  The **A800-9000-npu-driver\_**\ *x.x.x*\ **\_linux-aarch64.run** package is compatible with all OSs.

Procedure

1. Visit https://support.huawei.com/enterprise/en/ascend-computing/a800-9000-pid-250702818/software.

2. Choose a BMS version **A800-9000** *x.x.x*.

Determine the driver/firmware version by referring to `CANN Version Mapping <https://support.huawei.com/enterprise/en/ascend-computing/cann-pid-251168373/software>`__.

3. Click **Download** next to a software package (for example, **A800-9000-npu-driver\_**\ *x.x.x*\ **\_euleros2.8-aarch64.run**) to download the software package and digital signature file.
