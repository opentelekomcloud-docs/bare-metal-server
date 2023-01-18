:original_name: en-us_topic_0081116797.html

.. _en-us_topic_0081116797:

(Optional) Installing the IB driver
===================================

Scenario
--------

CentOS 7.4 is used as an example.

.. note::

   #. The IB driver can be installed only for CentOS 7.3, CentOS 7.4, CentOS 7.6 ARM, RedHat 7.3, RedHat 7.4, SUSE 12 SP3 and Oracle Linux 7.4.
   #. You are advised to install the 4.2 or later version.

Prerequisites
-------------

-  You have logged in to the VM.
-  The required IB driver installation package has been uploaded to the VM.

Procedure
---------

#. Download the OFED package as instructed in :ref:`Software <en-us_topic_0081116771>`.

   Download the .tgz installation package based on the VM OS and verify the file integrity.

   Take CentOS 7.4 as an example.

   |image1|

#. Upload the downloaded OFED installation package to the VM. For details, see :ref:`Configuring the VM Environment <en-us_topic_0081116597>`.

#. Run the **tar -zxvf** *xxx* command (*xxx* indicates the OFED installation package name) to decompress the package.

#. After the decompression is complete, go to the **MLNX_OFED_LINUX-4.2-1.2.0.0-RHEL7.4-X86_64** folder to install the package.

   **./mlnxofedinstall**

   .. code-block:: console

      [root@localhost MLNX_OFED_LINUX-4.2-1.2.0.0-rhel7.4-x86_64]# ./mlnxofedinstall
      Logs dir: /tmp/MLNX_OFED_LINUX.1479.logs
      General log file: /tmp/MLNX_OFED_LINUX.1479.logs/general.log
      Verifying KMP rpms compatibility with target kernel...
      Error: One or more required packages for installing MLNX_OFED_LINUX are missing.
      Please install the missing packages using your Linux distribution Package Management tool.
      Run:
      yum install tcl tk

#. During the installation, if the dependency package is missing, run the following command to install it:

   **yum install tcl tk**

#. Run the **./mlnxofedinstall** installation script again.

   If the following information is displayed after a while, the installation is successful:

   .. code-block::

      Installation finished successfully.

      Preparing...                                    ############################### [100%]
      Updating / installing...
         1:mlnx-fw-updater-4.2-1.2.0.0                ############################### [100%]

      Added 'RUN_FW_UPDATER_ONBOOT=no to /etc/infiniband/openib.conf
      ...

#. After the installation is complete, run the **/etc/init.d/openibd restart** command to load the driver.

   .. code-block:: console

      [root@localhost MLNX_OFED_LINUX-4.2-1.2.0.0-rhel7.4-x86_64]# /etc/init.d/openibd restart
      Uploading HCA driver:                                      [ OK ]
      Loading HCA driver and Access Layer:                       [ OK ]

.. |image1| image:: /_static/images/en-us_image_0141931888.png
