:original_name: en-us_topic_0140737434.html

.. _en-us_topic_0140737434:

Step 1: Create a BMS
====================

Scenarios
---------

This section helps you quickly create a BMS that will be used as a web server. For details about all the parameters used for creating a BMS, see :ref:`Creating a Common BMS <en-us_topic_0053536933>`. To create a BMS by calling an API, see "Creating a BMS (Native OpenStack API)" in *Bare Metal Server API Reference*.

Procedure
---------

#. Log in to the Cloud Server Console.
#. In the navigation pane, choose **Bare Metal Server**.
#. In the upper right corner, click **Allocate BMS**.
#. Configure parameters.

   -  Specify **Region** and **AZ**.

      .. note::

         After the BMS is created, you cannot change its region or AZ.

   -  Set **Flavor**.

      Available :ref:`flavors <en-us_topic_0083745258>` vary depending on the region and AZ you select. Web servers are mainly used for web page access and do not require strong computing capabilities. In addition, only a small amount of storage is required for recording logs. Therefore, select **physical.i7n.28xlarge.4**.

   -  Set **Image**.

      Select **Public image** and then **CentOS 7.4 64bit for BareMetal**.

   -  Set **License Type**.

      Select **Use system license**. You will be billed for the license. If you have an OS license of your own, select **Bring your own license (BYOL)**.

   -  Specify **Disk**.

      An EVS disk can be attached to a BMS. However, whether an EVS disk can be attached is determined by the flavor and image you select.

   -  Set **VPC** and **NIC**.

      Retain the default values. When you use cloud services for the first time, the system automatically creates a VPC **default-vpc** and a subnet **default-subnet** for you. You can also create VPCs and subnets.

      .. note::

         The system creates a security group for you by default. The default security group rule allows all outgoing data packets and blocks incoming data packets. In this way, the default security group rule ensures the security of basic BMS communications.

   -  Set **EIP**.

      BMSs without an EIP cannot be connected to the Internet and are only used for deploying services in a private network or used in a cluster. Select **Automatically assign** and set **Bandwidth**.

   -  Set **Login Mode**.

      Select the key pair created in :ref:`Making Preparations <en-us_topic_0083737005>` from the drop-down list and select **I acknowledge that I have obtained private key file xxx.pem and that without this file I will not be able to log in to my BMS**.

   -  Configure **Advanced Settings**.

      Select **Do not configure**.

   -  Set **BMS Name**.

      The BMS name is in the format **bms-**\ *four random digits*. To easily identify it, you can add the function to its name, for example, **bms-7676-nginx**.

   -  Set **Quantity**.

      Set the value to **1**.

#. Click **Allocate Now**. Confirm the specifications and click **Submit**.

Result
------

The BMS creation process requires about 5 to 30 minutes to complete. Refresh the BMS list. After the BMS status changes from **Creating** to **Running**, the BMS is created successfully.

Follow-up Operations
--------------------

A BMS that functions as a web server must allow ICMP traffic on ports 80 and 443. These rules are not configured for the default security group. You need to add the rules after you create the BMS. For details, see *Virtual Private Cloud User Guide*.

======== ========= ========== =========
Protocol Direction Port Range Source
======== ========= ========== =========
TCP      Inbound   80         0.0.0.0/0
TCP      Inbound   443        0.0.0.0/0
ICMP     Inbound   All        0.0.0.0/0
======== ========= ========== =========
