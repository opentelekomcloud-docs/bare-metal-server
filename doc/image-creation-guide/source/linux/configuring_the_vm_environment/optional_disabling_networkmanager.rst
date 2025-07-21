:original_name: en-us_topic_0000001238718197.html

.. _en-us_topic_0000001238718197:

(Optional) Disabling NetworkManager
===================================

Scenario
--------

A centralized BMS uses NetworkManager for network management. This tool needs to be disabled because it may conflict with **network-config**. For a distributed BMS, skip this section.

.. note::

   For SUSE 11 SP4, Ubuntu 16.04, and Ubuntu 14.04, skip this section. For BMSs with SDI 3.0 or 2.2 NIC cards, skip this section because NetworkManager is used for network management.

   Note:

   If NetworkManager is used for network management, you need to perform the following operations (only for Ubuntu):

   Take Ubuntu 1804.2 as an example.

   1. Run the **systemctl status NetworkManager** command to check whether the service is set to automatically start upon system startup.

   |image1|

   If the service does not exist, run the **apt-get install network-manager command** to install it.

   2. Add the network management service and NIC information to the **/etc/netplan/01*yaml** file.

   |image2|

   Enter **:wq!**. Then, run the **netplan try** command to update the network configuration.

Procedure
---------

-  For Red Hat 7, Oracle Linux 7, Debian, EulerOS, CentOS 7, or CentOS 8, run the following commands:

   **systemctl disable NetworkManager.service**

   **systemctl stop NetworkManager.service**

   Run the **service NetworkManager.service status** command to check the NetworkManager status.

   .. code-block:: console

      [root@localhost ~]# service NetworkManager.service status
      edirecting to /bin/systemctl status NetworkManager.service
       NetworkManager.service - Network Manager
        Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service disabled; vendor preset: enabled)
        Active: inactive (dead) since Mon 2017-11-13 19:06:18 CST; 1 min 17s ago

   For EulerOS, you also need to disable the following services:

   **systemctl disable euleros-security**

   **systemctl disable NetworkManager-wait-online**

-  For Red Hat 6.7/Red Hat 6.8/Red Hat 6.9/CentOS 6.8/CentOS 6.9/Oracle Linux 6.8/Oracle Linux 6.9, run the following commands:

   .. note::

      For Red Hat 6.7/Red Hat 6.8/Red Hat 6.9/CentOS 6.8/CentOS 6.9/Oracle Linux 6.8/Oracle Linux 6.9, if you choose **Server with GUI** when creating a VM, you need to disable NetworkManager; if you choose **Minimal Install**, you do not need to disable NetworkManager.

   **service NetworkManager stop**

   **chkconfig NetworkManager off**

-  For SUSE 12, run the following commands:

   **systemctl disable wicked**

   **systemctl stop wicked**

-  For Ubuntu18.04, run the following commands:

   **apt-get install ifupdown** --> Install ifupdown.

   **apt-get install ifenslave** --> Install ifenslave for bond management.

   **apt-get --assume-yes purge nplan netplan.io** --> Uninstall Netplan.

.. |image1| image:: /_static/images/en-us_image_0000001372998018.png
.. |image2| image:: /_static/images/en-us_image_0000001079569578.jpg
