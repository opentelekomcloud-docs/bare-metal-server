:original_name: en-us_topic_0000001238958151.html

.. _en-us_topic_0000001238958151:

Disabling the Firewall
======================

Scenario
--------

Disable the firewall on the VM. The firewall prevents the remote login in SSH mode.

Procedure
---------

-  For Red Hat 7.0, Red Hat 7.2, Red Hat 7.3, Red Hat 7.4, Oracle Linux 7, EulerOS, CentOS 7, CentOS 8, or SUSE15, run the following commands:

   **systemctl disable firewalld.service**

   **systemctl stop firewalld.service**

   Run the **systemctl status firewalld.service** command to check the firewall status.

-  For Red Hat 6.7, Red Hat 6.8, Red Hat 6.9, CentOS 6.8, CentOS 6.9, Oracle Linux 6.8, or Oracle Linux 6.9, run the following commands:

   **chkconfig iptables off**

   **service iptables stop**

   Run the **service iptables status** command to check the firewall status.

   .. code-block:: console

      [root@localhost ~]# service iptables status
      iptables: Firewall is not running.

-  For SUSE 12, run the following commands:

   **systemctl disable SuSEfirewall2.service**

   **systemctl stop SuSEfirewall2.service**

   Run the **service SuSEfirewall2 status** command to check the firewall status.

-  For SUSE 11, run the following command:

   **rcSuSEfirewall2 stop**

   Then, run the following command:

   #. **yast**
   #. Choose **Security and Users** > **Firewall** > **Disable Firewall Automatic Starting**.
   #. Check whether automatic firewall starting is disabled.

      -  If yes, click **Cancel** and then **Quit**.
      -  If no, click **Next**, **Finish**, and then **Quit**.

-  For Ubuntu 18.04, Ubuntu 16.04, Ubuntu 14.04, or Debian, run the following command:

   **ufw disable**

   If **ufw** is unavailable, download it from the official website (for example, https://packages.ubuntu.com/) and install it.

   The .deb installation package is as follows (the version number is for reference only):

   **ufw_0.35-0ubuntu2_all.deb**

   Alternatively, after configuring apt sources in :ref:`SUSE/Red Hat/CentOS/Oracle Linux/Ubuntu/Debian <en-us_topic_0218670457>`, run the **apt-get install ufw** command to install it and then run the **ufw disable** command to disable the firewall.
