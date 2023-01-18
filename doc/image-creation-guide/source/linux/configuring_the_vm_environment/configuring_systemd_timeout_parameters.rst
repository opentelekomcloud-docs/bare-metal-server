:original_name: en-us_topic_0000001239038181.html

.. _en-us_topic_0000001239038181:

Configuring systemd Timeout Parameters
======================================

Scenario
--------

Configure time parameters to prevent BMS provisioning timeout.

Procedure
---------

For Red Hat 7, EulerOS, CentOS 7, CentOS 8, Oracle Linux 7, Ubuntu 16.04, Ubuntu 18.04, SUSE 12 SP2, SUSE 12 SP3, SUSE 15, and Debian, run the following command:

**vi /etc/systemd/system.conf**

Delete the comment tags (#) before **DefaultTimeoutStartSec** and **DefaultTimeoutStopSec**, and change their values to **300s**.

.. code-block::

   #TimeSlackNSec=
   #DefaultTimerAccuracySec=1min
   #DefaultStandardOutput=journal
   #DefaultStandardError=inherit
   DefaultTimeoutStartSec=300s
   DefaultTimeoutStopSec=300s
   #DefaultRestartSec=100ms
   #DefaultStartLimitInterval=10s
   #DefaultStartLimitBurst=5
   #DefaultEnvironment=
   #DefaultCPUAccounting=no
   #DefaultBlockIOAccounting=no
