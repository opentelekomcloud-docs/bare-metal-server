:original_name: en-us_topic_0122234355.html

.. _en-us_topic_0122234355:

Overview
========

VPC
---

A VPC provides a logically isolated network environment for BMSs. You can configure EIPs, security groups, and VPNs in a VPC and use the VPC for communication between ECSs and BMSs.

View VPC NICs
-------------

You can view the network interfaces of the VPC on the **NICs** tab page of the BMS details page. For Linux images, you can also locate the VLAN sub-interface or bond interface in the OS based on the allocated IP address.

Take CentOS 7.4 64-bit as an example. Log in to the OS and view the NIC configuration files **ifcfg-eth0**, **ifcfg-eth1**, **ifcfg-bond0**, **ifcfg-bond0.3029**, **ifcfg-bond0.3187**, and **ifcfg-bond0.3189** in the **/etc/sysconfig/network-scripts** directory. You need to use IP mapping to match the network.

Run the **ifconfig** command. The private IP address and MAC address of VPC NIC 1 are 192.168.0.48 and fa:16:3e:04:5c:8c. The private IP address and MAC address of VPC NIC 2 are 192.168.0.14 and fa:16:3e:04:5c:6a. eth0 and eth1 automatically form bond0, and they have the same MAC address. In addition, it can be determined that **ifcfg-eth0**, **ifcfg-eth1**, **ifcfg-bond0**, **ifcfg-bond0.3029**, **ifcfg-bond0.3187**, and **ifcfg-bond0.3189** are VPC NIC configuration files.

|image1|

The following figures show the NIC and bond configuration information.

|image2|

|image3|

.. |image1| image:: /_static/images/en-us_image_0000001633847629.png
.. |image2| image:: /_static/images/en-us_image_0000001633910537.png
.. |image3| image:: /_static/images/en-us_image_0000001633561065.png
