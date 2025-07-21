:original_name: en-us_topic_0081250916.html

.. _en-us_topic_0081250916:

What Can I Do If Data Cannot Be Injected into BMSs Due to cloud-init-local Failures?
====================================================================================

Symptom
-------

For Red Hat 7 or CentOS 7, cloud-init-local may fail to start up. As a result, data cannot be injected into a BMS correctly. When you run **systemctl status cloud-init-local.service**, the message "OSError: [Errno 2] No such file or directory" is displayed.

Solution
--------

For Red Hat 7 and CentOS 7, if the libselinux version is earlier than 2.5.7, cloud-init-local may fail to start up. This is a known issue and has been fixed in libselinux 2.5.7. For details, see https://bugzilla.redhat.com/show_bug.cgi?id=1406520.

If you are creating a Red Hat 7 or CentOS 7 image, upgrade libselinux to 2.5.7 or later after you configure the yum source in section "Installing Cloud-Init > SUSE/Red Hat/CentOS/Oracle Linux/Ubuntu/Debian > CentOS".
