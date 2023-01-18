:original_name: en-us_topic_0083745256.html

.. _en-us_topic_0083745256:

What Is BMS?
============

Overview
--------

A Bare Metal Server (BMS) features both the scalability of Elastic Cloud Servers (ECSs) and high performance of physical servers. It provides dedicated servers on the cloud, delivering the performance and security required by core databases, critical applications, high-performance computing (HPC), and Big Data.

The BMS self-service feature allows you to apply for and use a BMS on demand. To apply for a BMS, you need to specify the server type, image, required network, and other configurations. You can obtain the BMS you require within 30 minutes.

System Architecture
-------------------

BMS works with other cloud services to provide computing, storage, network, and image functions.

-  BMSs are deployed in multiple availability zones (AZs) connected with each other through an internal network. If an AZ becomes faulty, other AZs in the same region will not be affected.
-  Virtual Private Cloud (VPC) allows you to create a dedicated network for BMSs and configure subnets and security groups. BMSs in a VPC can communicate with the external network through EIPs (bandwidth support required).
-  Image Management Service (IMS) allows you to install OSs on BMSs or create BMSs using private images for rapid service deployment.
-  Elastic Volume Service (EVS) provides storage and Volume Backup Service (VBS) provides data backup and restoration.
-  Cloud Eye is a key measure to monitor BMS performance, reliability, and availability. Using Cloud Eye, you can monitor BMS in real time.
-  Cloud Backup and Recovery (CBR) backs up data for EVS disks and BMSs, and uses snapshot backups to restore the EVS disks and BMSs.


.. figure:: /_static/images/en-us_image_0290913715.png
   :alt: **Figure 1** System architecture

   **Figure 1** System architecture

Access Methods
--------------

The public cloud provides a web-based service management system (management console). You can access BMS through the management console or HTTPS APIs. The two access methods differ as follows:

-  API

   If you want to integrate BMS into a third-party system for secondary development, use APIs to access the BMS service.

-  Management console

   For all other purposes, use the management console.
