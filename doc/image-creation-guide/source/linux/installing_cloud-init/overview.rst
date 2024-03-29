:original_name: en-us_topic_0131700228.html

.. _en-us_topic_0131700228:

Overview
========

Scenario
--------

Cloud-Init is a tool developed to initiate VMs or BMSs in the cloud environment. It is used to customize the network configuration, host name, hosts configuration file, username, and password when a user uses images to create VMs or BMSs. Cloud-Init is also required if the password of a VM created by using images is to be generated by the system at random.

In other case, Cloud-Init is not required. The Cloud-Init installation file has requirements on Linux versions and can only be installed from the Internet. Therefore, ensure that the VM can access the Internet.

Prerequisites
-------------

-  You have logged in to the VM.
-  The host can connect to the Internet.
-  You have logged in to the host using VNC Viewer and installed an OS on the host using virt-manager.

Description
-----------

#. The Cloud-Init installation procedures in the following sections are for reference only. You are advised to download the Cloud-Init from the official website. The Cloud-init version is updated on the official website in real time. Install the latest version.
#. When you modify the **/etc/cloud/cloud.cfg** file, ensure that the file format (such as alignment and spaces) is consistent with the provided example that conforms to the yaml syntax.
