:original_name: en-us_topic_0000001194038232.html

.. _en-us_topic_0000001194038232:

(Optional) Configuring the DNS Server
=====================================

Scenario
--------

For XenServer 7.1, you need to configure a DNS server. For other OSs, skip this section.

Procedure
---------

#. Run the **vi /etc/resolv.conf** command and change the IP address following **nameserver** to **8.8.8.8**. The value is an example only. Change it as needed.
#. Run the **systemctl status ntpd.service** command to check the ntpd status. If automatic startup is not enabled for ntpd, run the **systemctl enable ntpd.service** command to enable it.
