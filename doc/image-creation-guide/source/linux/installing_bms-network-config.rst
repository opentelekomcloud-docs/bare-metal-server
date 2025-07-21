:original_name: en-us_topic_0081116559.html

.. _en-us_topic_0081116559:

Installing bms-network-config
=============================

Scenarios
---------

Install bms-network-config to work with Cloud-Init for the network configuration of the BMSs with centralized BMGW. For the BMSs with distributed BMGW (that is, BMSs with SDI 3.0 or SDI 2.2 cards), you do not need to perform operations in this section. :ref:`Table 1 <en-us_topic_0081116559__en-us_topic_0094568715_table929435081518>` describes the BMS flavors for which bms-network-config needs to be installed.

.. _en-us_topic_0081116559__en-us_topic_0094568715_table929435081518:

.. table:: **Table 1** BMS flavors

   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | BMS Type                   | Flavor                                                                                                                                                          |
   +============================+=================================================================================================================================================================+
   | General-purpose            | physical.s3.large, physical.s3.xlarge, physical.s3.2xlarge, physical.s4.medium, physical.s4.large, physical.s4.xlarge, physical.s4.2xlarge, physical.s4.3xlarge |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Disk-intensive             | physical.d1.large, physical.d2.tiny, physical.d2.large, physical.d2.xmedium                                                                                     |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Memory-optimized           | physical.m2.small, physical.m2.medium, physical.m2.large, physical.m2.xlarge                                                                                    |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | I/O-optimized              | physical.io1.large, physical.io2.xlarge                                                                                                                         |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | GPU-accelerated            | physical.p1.large, physical.p2.large, physical.g1.small, physical.p3.large, physical.pi6.3xlarge.6                                                              |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | High-performance computing | physical.h2.large, physical.hc2.xlarge                                                                                                                          |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Prerequisites
-------------

-  You have logged in to the VM.
-  Cloud-Init has been installed on the VM.
-  You have downloaded the bms-network-config software package by referring to :ref:`Software <en-us_topic_0081116771>`.

   .. note::

      Download the RPM package depending on the OS. Ubuntu and Debian use the .deb package, and CentOS and EulerOS (Arm) use the aarch .rpm package.

Procedure
---------

#. Enter the directory where the bms-network-config software package is stored and run the **rpm -ivh** *bms-network-config-1.0-7.centosRedhat7.x86_64.rpm* command.

   .. code-block:: console

      [root@localhost r74]# rpm -ivhbms-network-config-1.0-7.centosRedhat7.x86_64.rpm
      Preparing...                          ############################### [100%]
      Updating / installing...
         1:bms-network-config-1.0.7.centosRe############################### [100%]

   .. note::

      If the error shown in the following figure is displayed when you install bms-network-config for SUSE 12/SUSE 15, run the **rpm -ivh bms-network-config-1.0-9.suse12.x86_64.rpm --nodeps --force** command.

      |image1|

   For Ubuntu/Debian, run the **dpkg -i** *xxx* command (*xxx* indicates the .deb package name).

   .. code-block::

      root@ubuntu:~/file# dpkg -i bms-network-config-1.0.7.ubuntu1604-918.deb
      Selecting previously unselected package bms-network-config.
      (Reading database ... 97630 files and directories currently installed.)
      Preparing to unpack bms-network-config-1.0.7.ubuntu1604-918.deb ...
      Unpacking bms-network-config (1.0) ...
      Setting up bms-network-config (1.0) ...
      root@ubuntu:~/file# dpkg -s bms-network-config

   .. note::

      The names of the .rpm and .deb packages vary according to the actual situation.

#. After the installation is complete, run the **rpm -qa \| grep bms-network-config** command. The installation is successful if the following information is displayed:

   .. code-block:: console

      [root@localhost r74]# rpm -qa | grep bms
      bms-network-config-1.0.7.centosRedhat7.x86_64

   For Ubuntu/Debian, run the **dpkg -s bms-network-config** command.

#. Check the bms-network-config status.

   -  For Oracle Linux 7, Red Hat 7, CentOS 7, Ubuntu 16.04, Ubuntu 18.04, SUSE 12, SUSE 15, or EulerOS, run the **service bms-network-config status** command to check the service status. If the status is not **enabled**, run the **systemctl enable bms-network-config** command to enable the service.

      .. code-block:: console

         [root@localhost r74]# service bms-network-config status
         Redirecting to /bin/systemctl status bms-network-config.service
           bms-network-config.service - Network Config
           Loaded: loaded (/usr/lib/systemd/system/bms-network-config service; enabled vendor preset: disabled)
           Active: inactive (dead)

   -  For Red Hat 6, CentOS 6, SUSE 11 SP4, Oracle Linux 6.8, or Oracle Linux 6.9, run the **chkconfig --list \| grep bms-network-config** command to check the service status. If the status is not **on**, run the **chkconfig bms-network-config on** command to enable the service.

      .. code-block:: console

         [root@localhost r69]# chkconfig --list | grep bms
         bms-network-config   0:off   1:off   2:on   3:on   4:off   5:on   6:off

   -  For Ubuntu 14.04/Debian, run the **initctl status bms-network_config** command to check the service status.

      .. code-block::

         root@ubuntu:~# initctl status bms-network_config
         bms-network_config stop/waiting

#. Check the startup dependencies between bms-network-config and other services.

   Run the **systemctl cat bms-network-config** command to check the configuration file and ensure that the file content is as follows:

   .. code-block::

      [Unit]
      Description=NetworkConfig
      DefaultDependencies=no
      After=dbus.service
      Wants=dbus.service

      [Service]
      Type=oneshot
      ExecStart=/usr/bin/bms-network_config rhel
      RemainAfterExit=yes
      TimeoutSec=0

      [Install]
      WantedBy=multi-user.target

   If the startup sequence is incorrect, use the **vim /usr/lib/systemd/system/bms-network-config.service** command to correct it.

.. |image1| image:: /_static/images/en-us_image_0140670562.png
