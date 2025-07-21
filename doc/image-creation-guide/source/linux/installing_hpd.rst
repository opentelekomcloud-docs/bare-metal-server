:original_name: en-us_topic_0000002351903932.html

.. _en-us_topic_0000002351903932:

Installing HPD
==============

Hotplug Daemon (HPD) is customer software installed in a BMS OS in the cloud environment.

An Hi1823 NIC provides a Hot Plug Controller Emulator PF for a BMS. The PF is used as a message channel for hot swap events. HPD takes over the PF and uses the native VFIO driver to present it to users.

Obtaining the Software Package
------------------------------

Download the software package at `Support > Software > Huawei Cloud > Huawei Public Cloud > Computing Infrastructure <https://support.huawei.com/carrier/idpRedirect?redirect=https%253A%252F%252Fsupport.huawei.com%252Fcarrier%252Fnavi%253Fcoltype%253Dsoftware%2523col%253Dsoftware%2526detailId%253DPBI1-263196404%2526path%253DPBI1-253383977%252FPBI1-23710112%252FPBI1-23710137%252FPBI1-255213015>`__.

The software package contains the following packages:

-  HPD package (AArch64): hotplug-daemon-*xx.xx.xx.xx*.aarch64.rpm
-  HPD package (x86): hotplug-daemon-*xx.xx.xx.xx*.x86.rpm

Prerequisite
------------

#. The HPD package has been downloaded to the client.

   The installation package name is hotplug-daemon-<version>-<release>.<arch>.rpm.

#. The installation package has been uploaded to the BMS OS.

#. The BMS OS must support VFIO.


Installing HPD
--------------

#. Log in to the BMS OS.

#. Install HPD.

   Run **rpm -ivh hotplug-daemon-**\ *xxxx-xxxx.xxx*\ **.rpm**.

   .. code-block:: console

      [root@localhost debug]# rpm -ivh hotplug-daemon-16.1.8.1-1.aarch64.rpm
      Verifying...                          ################################# [100%]
      Preparing...                          ################################# [100%]
      Updating / installing...
         1:hotplug-daemon-16.1.8.1-1        ################################# [100%]

#. Restart the BMS.

Upgrading HPD
-------------

#. Log in to the BMS OS.

#. Upgrade HPD.

   Run **rpm -Uvh hotplug-daemon-**\ *xxxx-xxxx.xxx*\ **.rpm**.

   .. code-block:: console

      [root@localhost debug]# rpm -Uvh hotplug-daemon-16.1.8.1-1.aarch64.rpm
      Verifying...                          ################################# [100%]
      Preparing...                          ################################# [100%]
      Updating / installing...
         1:hotplug-daemon-16.1.8.1-1        ################################# [ 50%]
      Cleaning up / removing...
         2:hotplug-daemon-16.1.1.1-1       ################################# [100%]

#. Restart HPD.

   Run **service hpd restart**.

   .. code-block:: console

      [root@localhost ~]# service hpd restart
      Redirecting to /bin/systemctl restart hpd.service
