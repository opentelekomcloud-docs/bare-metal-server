:original_name: en-us_topic_0053536933.html

.. _en-us_topic_0053536933:

Creating a Common BMS
=====================

Scenarios
---------

This section describes how to create a BMS to deploy your services.

Prerequisites
-------------

-  You have completed :ref:`Preparations <en-us_topic_0083737005>`.
-  To inject user data, you have prepared :ref:`user data scripts <en-us_topic_0083737011>`.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click **Allocate BMS**.

#. Select a region.

   BMSs in different regions cannot communicate with each other over an intranet. You are advised to select the region closest to your services to lower the network delay and improve the access speed. Note that after a BMS is created, its region cannot be changed.

#. Select an AZ.

   An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.

   -  It is recommended that you create BMSs in different AZs to ensure high availability of applications running on the BMSs.
   -  To lower the network delay, create BMSs in the same AZ.

#. Select a flavor.

   **Flavor** contains the CPU, memory, local disks, and extended configuration of the BMS. After you select a flavor, the name and use scenarios of the flavor are displayed under the flavor list.

   **Extended Configuration** provides the NIC information of the selected flavor. For example, 2 x 2*10GE indicates that the BMS has two 10GE NICs, each with two ports. One NIC is used for the BMS to connect to a VPC and the other is used for the BMS to communicate with other BMSs in a high-speed network.

   .. note::

      -  Configuration in the flavor, such as the CPU, memory, and local disks, cannot be changed.
      -  The bandwidth of different BMS flavors varies. Choose a flavor that meets your requirements.
      -  Some flavors support quick BMS provisioning. If you select a flavor of this type, parameter **System Disk** is displayed under **Disk**. The OS will be installed on the EVS disk attached to the BMS.

#. Set **Image**.

   -  Public Image

      A public image is a standard OS image provided by the system and is available to all users. It contains an OS and pre-installed public applications, such as the SDI iNIC driver, bms-network-config (a network configuration program), and Cloud-Init (an initialization tool). If you need other applications or software, configure them on the new BMSs.

   -  Private Image

      A private image is created from an external image file or a BMS and is available only to the user who created it. It contains an OS, preinstalled public applications, and the user's private applications.

   -  Shared Image

      A shared image is a private image shared by another public cloud user with you.

#. Set **License Type**.

   Set a license type for using an OS or software on the cloud platform. This parameter is available only if the public image you selected is charged.

   -  Use license from the system

      Allows you to use the license provided by the cloud platform. Obtaining the authorization of such a license is charged.

   -  Bring your own licenses (BYOL)

      Allows you to use your existing OS license. In such a case, you do not need to apply for a license again.

#. Set **Disk**.

   A BMS has one system disk and one or more data disks. You can add multiple data disks for a BMS and customize the system disk size.

   -  System disk

      If you select a flavor that supports quick provisioning, parameter **System Disk** is available. You can set the system disk type and size as needed.

   -  Data disk

      You can add multiple data disks for a BMS and enable sharing for each data disk.

      -  Currently, BMSs only support SCSI disks.
      -  **Share**: indicates that the EVS disk can be shared. A shared disk can be attached to multiple BMSs simultaneously.

#. Set network parameters, including **VPC**, **NIC**, and **Security Group**.

   When you use VPC for the first time, the system automatically creates a VPC for you, including the security group and NIC. The default subnet segment is 192.168.1.0/24 and the subnet gateway is 192.168.1.1. Dynamic Host Configuration Protocol (DHCP) is enabled for the subnet.

   .. table:: **Table 1** Network parameters

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                          |
      +===================================+======================================================================================================================================================================================================================+
      | VPC                               | You can select an existing VPC or create one.                                                                                                                                                                        |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | NIC                               | Includes primary and extension NICs. You can add an extension NIC for a BMS and specify IP addresses for the primary and extension NICs.                                                                             |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | .. caution::                                                                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    CAUTION:                                                                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    -  The primary NIC cannot be deleted because it is used to provide the default route.                                                                                                                             |
      |                                   |    -  If you choose to assign an IP address automatically, do not change the private IP address of the BMS after the BMS is provisioned. Otherwise, the IP address may conflict with that of another BMS.            |
      |                                   |    -  If a fixed IP address is assigned to a NIC, you cannot create BMSs in a batch.                                                                                                                                 |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | High-Speed NIC                    | A high-speed NIC provides high-speed network ports for communication between BMSs. It provides high bandwidth.                                                                                                       |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | Each high-speed NIC of a BMS must be in a different high-speed network.                                                                                                                                              |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Security Group                    | Security groups are used to control access to BMSs. You can define different access control rules for a security group, and these rules take effect for all BMSs added to this security group.                       |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | When creating a BMS, you can select only one security group. After a BMS is created, you can associate it with multiple security groups. For details, see :ref:`Changing a Security Group <en-us_topic_0120711875>`. |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | .. note::                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    Before initializing a BMS, ensure that security group rules in the outbound direction meet the following requirements:                                                                                            |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    -  Protocol: TCP                                                                                                                                                                                                  |
      |                                   |    -  Port Range: 80                                                                                                                                                                                                 |
      |                                   |    -  Remote End: 169.254.0.0/16                                                                                                                                                                                     |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    If you use the default outbound security group rule, the preceding requirements are met, and the BMS can be initialized. The default outbound security group rule is as follows:                                  |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    -  Protocol: Any                                                                                                                                                                                                  |
      |                                   |    -  Port Range: Any                                                                                                                                                                                                |
      |                                   |    -  Remote End: 0.0.0.0/16                                                                                                                                                                                         |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | EIP                               | An EIP is a static public IP address bound to a BMS in a VPC. Using the EIP, the BMS can access the Internet.                                                                                                        |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | You can select one of the following three options for **EIP** as needed:                                                                                                                                             |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | -  **Not required**: The BMS cannot communicate with the Internet and can be used only on a private network for deploying services or used to deploy a cluster.                                                      |
      |                                   | -  **Automatically assign**: The system automatically assigns an EIP with a dedicated bandwidth to the BMS. The bandwidth is configurable.                                                                           |
      |                                   | -  **Use existing**: An existing EIP is assigned to the BMS.                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | .. note::                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                      |
      |                                   |    If you select **Use existing**, you can create only one BMS at a time.                                                                                                                                            |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Bandwidth                         | This parameter is available when you select **Automatically assign** for **EIP**.                                                                                                                                    |
      |                                   |                                                                                                                                                                                                                      |
      |                                   | Specifies the bandwidth size in Mbit/s.                                                                                                                                                                              |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Set the BMS login mode.

   **Key pair**: A key pair is used for BMS login authentication. You can select an existing key pair, or click **View Key Pair** and create one.

   .. note::

      If you use an existing key pair, ensure that you have saved the key file locally. Otherwise, logging in to the BMS will fail.

#. (Optional) Configure **Advanced Settings**.

   To use functions listed in **Advanced Settings**, click **Configure now**. Otherwise, click **Do not configure**.

   -  **User Data Injection** enables the BMS to automatically inject user data when the BMS starts for the first time. After this function is enabled, the BMS automatically injects user data upon its first startup.

      This parameter is available only when **Key pair** is selected for **Login Mode**. For detailed operations, see :ref:`Injecting User Data <en-us_topic_0083737011>`.

   -  (Optional) **Tag**

      Tagging BMSs helps you better identify and manage your BMSs. You can add up to nine tags to a BMS.

      For detailed operations on tags, see :ref:`Adding Tags <en-us_topic_0110378367>`.

   -  **Agency**

      An agency provides BMSs with temporary security credentials for accessing other cloud services. The agency is created by the tenant administrator on the IAM console.

      If you have created an agency in IAM, you can select the agency from the drop-down list. Currently, agencies are mainly used for server monitoring.

#. Set **BMS Name**.

   The name can be customized but can contain only letters, digits, underscores (_), hyphens (-), and periods (.).

   If you create multiple BMSs at a time, suffixes will be added to the BMSs in sequence, such as **bms-0001**, **bms-0002**, ... If you create multiple BMSs again, the values in the new BMS names increase from the existing maximum value. For example, the existing BMS with the maximum number in name is **bms-0010**. If you enter **bms**, the names of the new BMSs will be **bms-0011**, **bms-0012**, .... When the value reaches 9999, it will start from 0001 again.

#. Set your desired number of BMSs, which is a maximum of all available BMSs.

   After the configuration, click **Price Calculator** to view the BMS configuration fee.

   .. note::

      If you manually set an IP address when configuring **NIC** or **High-Speed NIC** or select **Use existing** when configuring **EIP**, you can create only one BMS at a time.

#. Click **Allocate Now**.

#. On the displayed page, confirm the specifications and click **Submit**.

   The BMS status changes to **Running** after about 30 minutes. If you select a flavor that supports quick provisioning, you can obtain a BMS within about five minutes.

   .. note::

      You can view the BMS creation status. For details, see :ref:`Viewing BMS Creation Statuses <en-us_topic_0053536924>`.

Follow-up Operations
--------------------

-  After the BMS is created, you can view its details, such as name/ID, disks, and private IP address. For details, see :ref:`Viewing BMS Details <en-us_topic_0053536942>`.
-  After logging in to the BMS, you can install software or deploy services as needed. The login mode varies depending on the BMS OS. For details, see :ref:`Linux BMS Login Methods <en-us_topic_0053536931>` or :ref:`Windows BMS Login Methods <en-us_topic_0097289761>`.
-  If you have created data disks when creating the BMS, you must format partitions of the data disks. For details, see :ref:`Introduction to Data Disk Initialization Scenarios and Partition Styles <en-us_topic_0157011194>`.
-  Change the validity period of the password to prevent any inconvenience caused by password expiration. For detailed operations, see :ref:`How Do I Set the Password Validity Period? <en-us_topic_0079122353>`
-  Currently, Windows Server 2012 BMSs have the same security identifier (SID), which is used to identify users, groups, and computer accounts. In cluster deployment scenarios, change the SIDs of BMSs by following the instructions in :ref:`How Do I Change the SID of a Windows Server 2012 BMS? <en-us_topic_0104580828>` to ensure that each BMS has a unique SID.
