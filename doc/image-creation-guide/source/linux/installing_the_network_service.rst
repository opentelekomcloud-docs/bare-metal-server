:original_name: en-us_topic_0000001239046729.html

.. _en-us_topic_0000001239046729:

Installing the Network Service
==============================

Scenario
--------

By default, the network service is not installed for CentOS 8, EulerOS 2.9, Red Hat 8, Ubuntu 20, or later. For BMSs with centralized BMGW, the network service and network scripts are required to configure the network. For BMSs with distributed BMGW (that is, BMSs with SDI 3.0 or SDI 2.2 cards), skip this section.

Procedure
---------

EulerOS 2.10 is used as an example.

#. Log in to the VM and query the network status.

   [root@euler210-arm-new ~]# systemctl status network

   Unit network.service could not be found.

#. Use the yum source to install network-scripts.

   [root@euler210-arm-new network-scripts]# yum install network-scripts

#. After the installation is complete, check whether the network service exists.

   [root@euler210-arm-new network-scripts]# systemctl status network

   ● network.service - LSB: Bring up/down networking

   Loaded: loaded (/etc/rc.d/init.d/network; generated)

   Active: inactive (dead)

   Docs: man:systemd-sysv-generator(8)
