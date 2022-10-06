:original_name: en-us_topic_0113605684.html

.. _en-us_topic_0113605684:

Overview
========

This document describes how to call the APIs of Bare Metal Server (BMS) to use the functions of the service. This chapter describes the concepts related to BMS to help you quickly understand the service.

BMS
---

A Bare Metal Server (BMS) is a physical server that is dedicated for you on the cloud. It provides the excellent computing performance and data security needed for core databases, key application systems, high-performance computing (HPC), and Big Data services. With the high scalability offered by cloud resources, you can apply for and use BMSs flexibly.

Basic Concepts
--------------

-  Availability zone

   An availability zone (AZ) is a physical location where power and networks are physically isolated within a region. Each AZ provides cost-effective and low-latency network connections that are unaffected by faults that may occur in other AZs. A region can contain multiple AZs, which are physically isolated but interconnected through internal networks. This ensures the independence of AZs and provides low-cost and low-latency network connections.

-  Elastic Volume Service (EVS)

   The EVS service offers scalable block storage for BMSs. With high reliability, high performance, and rich specifications, EVS disks can be used for distributed file systems, development and test environments, data warehouse applications, and high-performance computing (HPC) scenarios to meet diverse service requirements.

-  Virtual Private Cloud (VPC)

   A VPC is a logically isolated, configurable, and manageable virtual network. It helps improve the security of cloud resources and simplifies network deployment. You can create security groups and VPNs, configure IP address ranges, and specify bandwidth sizes in your VPC. With a VPC, you can easily manage and configure internal networks and change network configurations. You can also customize access rules to control BMS access within a security group and across different security groups to enhance BMS security.

-  User-defined VLAN

   You can use the 10GE Ethernet NICs that are not being used by the system to configure a user-defined VLAN. The QinQ technology is used to isolate networks and provide additional physical planes and bandwidths. You can create VLANs to isolate network traffic. User-defined VLAN NICs are in pairs. You can configure NIC bonding to achieve high availability. User-defined VLANs in different AZs cannot communicate with each other.

-  IB network

   An IB network features low latency and high bandwidth and is used in a number of High Performance Computing (HPC) projects. It uses the 100 Gbit/s Mellanox IB NIC, dedicated IB switch, and controller software UFM to ensure network communication and management, and uses the Partition Key to isolate IB networks of different tenants (similar to VLANs in an Ethernet).

-  Image

   An image is a template of the BMS running environment. It contains an OS and runtime environment, and some pre-installed applications. An image file is equivalent to a copy file that contains all data in the system disk.
