:original_name: en-us_topic_0106040941.html

.. _en-us_topic_0106040941:

Creating BMSs
=============

Function
--------

This API is used to create one or multiple BMSs.

Background for Setting the Login Authentication Mode
----------------------------------------------------

Logging in to a BMS can be authenticated using either a key pair or password. For security purposes, you are advised to use key pair authentication.

-  Key pair

   A key pair is used for BMS login authentication.

   Method of calling APIs: Use the **key_name** field to specify the key file used for authentication of login to a BMS. For details about how to use the **key_name** field, see :ref:`Table 2 <en-us_topic_0106040941__table114451828162019>`.

-  Password

   If you choose the initial password for authentication in a BMS, you can log in to the BMS using the username and its initial password. The initial password of user **root** is used for authentication in Linux.

   Methods of calling APIs:

   -  Method 1 (recommended): Use the **adminPass** field to specify the initial login password of the specified administrator account. For details about how to use the **adminPass** field, see :ref:`Table 2 <en-us_topic_0106040941__table114451828162019>`.

      .. note::

         For a Linux BMS with Cloud-Init installed, if field **user_data** is specified, field **adminPass** is invalid.

   -  Method 2:

      -  For a Linux BMS with Cloud-Init installed, use the **user_data** field to inject data. For details, see :ref:`Table 2 <en-us_topic_0106040941__table114451828162019>`.

   .. note::

      Public images contain Cloud-Init or Cloudbase-Init by default. For private images, you need to check whether Cloud-Init or Cloudbase-Init is installed.

Constraints
-----------

-  File injection is not supported.

URI
---

POST /v1/{project_id}/baremetalservers

:ref:`Table 1 <en-us_topic_0106040941__table1878518571>` lists the parameters.

.. _en-us_topic_0106040941__table1878518571:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                   |
   |                       |                       |                                                                                                             |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

+-----------+-----------+--------+------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                |
+===========+===========+========+============================================================================================================+
| server    | Yes       | Object | Specifies BMS information. For details, see :ref:`Table 2 <en-us_topic_0106040941__table114451828162019>`. |
+-----------+-----------+--------+------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table114451828162019:

.. table:: **Table 2** **server** data structure

   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter         | Mandatory       | Type                | Description                                                                                                                                                                                                                                                                    |
   +===================+=================+=====================+================================================================================================================================================================================================================================================================================+
   | imageRef          | Yes             | String              | Specifies the image ID or image resource URL used for creating the BMS. The ID is in the format of a Universally Unique Identifier (UUID).                                                                                                                                     |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | You can obtain the image ID from the IMS console or by following the instructions in "Querying Images" in *Image Management Service API Reference*.                                                                                                                            |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | When using an API to query images, you can add the field **?virtual_env_type=Ironic** to filter BMS images.                                                                                                                                                                    |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flavorRef         | Yes             | String              | Specifies the flavor ID of the BMS. The format is **physical.**\ *x*\ **.**\ *x*.                                                                                                                                                                                              |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | You can obtain the flavor ID from the BMS console or using the :ref:`Querying Flavor Details and Extended Flavor Information <en-us_topic_0131326852>` API.                                                                                                                    |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name              | Yes             | String              | Specifies the BMS name.                                                                                                                                                                                                                                                        |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Value range:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  The value can contain a maximum of 63 characters consisting of letters (case-insensitive), digits, underscores (_), hyphens (-), and periods (.).                                                                                                                           |
   |                   |                 |                     | -  If more than one BMS is to be created, suffixes similar to **-0000** will be automatically added to the end of the BMS names during the BMS creation. In this case, the BMS name contains 1 to 58 characters.                                                               |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | metadata          | Yes             | Object              | Specifies the BMS metadata. The maximum size for both the metadata **key** and **value** is 255 characters. For details, see :ref:`Table 3 <en-us_topic_0106040941__table187761842111012>`.                                                                                    |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | user_data         | No              | String              | Specifies the user data to be injected during the BMS creation. Text can be injected.                                                                                                                                                                                          |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB.                                                                                                                                          |
   |                   |                 |                     | -  If **key_name** is not specified, the password of user **root** for logging in to the BMS will be injected by default.                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Password complexity requirements:                                                                                                                                                                                                                                              |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  Contains 8 to 26 characters.                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters ``!@$%^-_=+[{}]:,./?``                                                                                                                       |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | An example is as follows:                                                                                                                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | ::                                                                                                                                                                                                                                                                             |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |    #!/bin/bash                                                                                                                                                                                                                                                                 |
   |                   |                 |                     |    echo 'root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig' | chpasswd -e                                                                                                                                                                                                |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | where, **$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig** is the ciphertext password, which can be generated as follows:                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | #. Generate an encrypted salt value.                                                                                                                                                                                                                                           |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |    .. code:: console                                                                                                                                                                                                                                                           |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |       [root@test linux]# python -c "import crypt, getpass, pwd;print crypt.mksalt()"                                                                                                                                                                                           |
   |                   |                 |                     |       $6$V6azyeLwcD3CHlpY                                                                                                                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | #. Generate a ciphertext password based on the salt value.                                                                                                                                                                                                                     |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |    .. code:: console                                                                                                                                                                                                                                                           |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |       [root@test linux]# python -c "import crypt, getpass, pwd;print crypt.crypt('Cloud.1234','\$6\$V6azyeLwcD3CHlpY')"                                                                                                                                                        |
   |                   |                 |                     |        $6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig                                                                                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | .. note::                                                                                                                                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |    Data injection is not supported for BMSs that use a Linux image and the password login mode.                                                                                                                                                                                |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | adminPass         | No              | String              | Specifies the initial login password of the administrator account for logging in to a BMS. The Linux administrator is **root**.                                                                                                                                                |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Password complexity requirements:                                                                                                                                                                                                                                              |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  Contains 8 to 26 characters.                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters ``!@$%^-_=+[{}]:,./?``                                                                                                                       |
   |                   |                 |                     | -  (Linux OSs) Cannot contain the username or the username in reverse.                                                                                                                                                                                                         |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | key_name          | No              | String              | Specifies the name of a key pair. This is an extended attribute. To log in to a BMS using an SSH key pair, set the value to the name of an existing private key.                                                                                                               |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | You can create a key pair using the :ref:`Creating or Importing an SSH Key Pair (Native OpenStack API) <en-us_topic_0000002340222820>` API, or query existing key pairs using the :ref:`Querying SSH Key Pairs (Native OpenStack API) <en-us_topic_0000002374101041>` API.     |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  If both **key_name** and **user_data** are specified, **user_data** only injects user data.                                                                                                                                                                                 |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | security_groups   | No              | Array of objects    | Specifies security groups of the BMS. For details, see :ref:`Table 4 <en-us_topic_0106040941__table3900132719153>`.                                                                                                                                                            |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nics              | Yes             | Array of objects    | Specifies NICs of the BMS. For details, see :ref:`Table 5 <en-us_topic_0106040941__table117050392164>`.                                                                                                                                                                        |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | A maximum of two NICs can be attached to a BMS. The first will be used as the primary NIC. If multiple NICs are specified, ensure that all NICs belong to the same VPC.                                                                                                        |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | availability_zone | Yes             | String              | Specifies the name of the AZ where the BMS is.                                                                                                                                                                                                                                 |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vpcid             | Yes             | String              | Specifies the ID of the VPC where the BMS is. The value is in UUID format. You can obtain the VPC ID from the network console or by following the instructions in "Querying VPC Details" of *Virtual Private Cloud API* *Reference*.                                           |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | publicip          | No              | Object              | Specifies the EIP information of the BMS. Possible values include:                                                                                                                                                                                                             |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  **Do not use** (This parameter is unavailable.)                                                                                                                                                                                                                             |
   |                   |                 |                     | -  **Automatically assign**: Assign a new EIP.                                                                                                                                                                                                                                 |
   |                   |                 |                     | -  **Specify**: Specify an EIP that has been created.                                                                                                                                                                                                                          |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | For details, see :ref:`Table 6 <en-us_topic_0106040941__table5440825153610>`.                                                                                                                                                                                                  |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | count             | No              | Integer             | Specifies the number of BMSs to be created.                                                                                                                                                                                                                                    |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | -  If this parameter is not specified, the default value is **1**.                                                                                                                                                                                                             |
   |                   |                 |                     | -  If the quota is sufficient, the maximum value is **24**.                                                                                                                                                                                                                    |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | root_volume       | No              | Object              | Specifies system disk details of the BMS. For details, see :ref:`Table 7 <en-us_topic_0106040941__table338522873815>`.                                                                                                                                                         |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | If the flavor supports quick provisioning, this parameter is mandatory. Otherwise, this parameter is not required. For how to check whether a flavor supports quick provisioning, see :ref:`Querying Flavor Details and Extended Flavor Information <en-us_topic_0131326852>`. |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | data_volumes      | No              | Array of objects    | Specifies data disk details of the BMS. Each data structure represents a data disk to be created. For details, see :ref:`Table 8 <en-us_topic_0106040941__table16541153834413>`.                                                                                               |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | Constraints:                                                                                                                                                                                                                                                                   |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | A maximum of 40 EVS disks (including the system disk and data disks) can be attached to a BMS.                                                                                                                                                                                 |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | extendparam       | Yes             | Object              | Specifies the supplementary for creating the BMS. For details, see :ref:`Table 9 <en-us_topic_0106040941__table12971921194613>`.                                                                                                                                               |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | schedulerHints    | No              | Object              | Specifies scheduling information of the BMS. This parameter is mandatory for creating a BMS in a DeC.                                                                                                                                                                          |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | For details, see :ref:`Table 10 <en-us_topic_0106040941__table615418218465>`.                                                                                                                                                                                                  |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_tags       | No              | List <resource_tag> | Specifies tags of the BMS. For details, see :ref:`Table 11 <en-us_topic_0106040941__table106007521267>`.                                                                                                                                                                       |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     | .. note::                                                                                                                                                                                                                                                                      |
   |                   |                 |                     |                                                                                                                                                                                                                                                                                |
   |                   |                 |                     |    A maximum of 10 tags can be added for a BMS. There has been a system tag **\__type_baremetal** by default. So, you can add a maximum of nine tags.                                                                                                                          |
   +-------------------+-----------------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table187761842111012:

.. table:: **Table 3** **metadata** data structure

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                              |
   +=================+=================+=================+==========================================================================================================================================================+
   | op_svc_userid   | Yes             | String          | Specifies the user ID. You can obtain the user ID from **My Credential** on the management console.                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | BYOL            | No              | String          | Specifies whether a license is provided. The value can be **true** or **false**.                                                                         |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | admin_pass      | No              | String          | Specifies the initial password of the administrator account for logging in to a BMS. For Linux, the administrator account is **root**.                   |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | Password complexity requirements:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | -  Contains 8 to 26 characters.                                                                                                                          |
   |                 |                 |                 | -  Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters ``!@$%^-_=+[{}]:,./?`` |
   |                 |                 |                 | -  Cannot contain the username, the username in reverse, or more than two consecutive characters in the username.                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String          | Specifies the IAM agency name.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | An agency provides a temporary security credential for accessing a BMS. The agency is created by the tenant administrator on the IAM console.            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table3900132719153:

.. table:: **Table 4** **security_groups** data structure

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================================================================================================================+
   | id              | No              | String          | Specifies a security group ID, which takes effect for all NICs configured for the BMS.                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                     |
   |                 |                 |                 | -  If this parameter is not specified, the default security group is bound to the BMS.                                                                                                                                              |
   |                 |                 |                 | -  If this parameter is required (in UUID format), use the ID of an existing security group. For details about how to obtain existing security groups, see "Querying Security Groups" in *Virtual Private Cloud* *API* *Reference*. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table117050392164:

.. table:: **Table 5** **nics** data structure

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================================================================================================================================================================================+
   | subnet_id       | Yes             | String          | Specifies the subnet information of a BMS NIC.                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 | The value must be the ID of the subnet (**network_id**) created in the VPC specified by **vpcid** and in the format of UUID. You can obtain the subnet ID (**network_id**) from the VPC console or by following the instructions in "Querying Subnets" in *Virtual Private Cloud API Reference*. |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ip_address      | No              | String          | Specifies the IPv4 address of a BMS NIC.                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 | Constraints:                                                                                                                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 | -  If this parameter is left blank or set to **""**, an unused IP address in the subnet of this network is automatically assigned as the IP address of the NIC.                                                                                                                                  |
   |                 |                 |                 | -  If this parameter is specified, its value must be an unused IP address in the network segment of the subnet.                                                                                                                                                                                  |
   |                 |                 |                 | -  The IP address cannot be specified when you create BMSs in a batch.                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table5440825153610:

.. table:: **Table 6** **publicip** data structure

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================================================================================+
   | id              | No              | String          | Specifies the ID of an existing EIP assigned to the BMS. The value is in UUID format. You can obtain the EIP ID from the network console or by following the instructions in "Querying EIPs" in *Elastic IP API Reference*. |
   |                 |                 |                 |                                                                                                                                                                                                                             |
   |                 |                 |                 | Constraints:                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                             |
   |                 |                 |                 | -  Only EIPs in the **DOWN** state can be assigned.                                                                                                                                                                         |
   |                 |                 |                 | -  Existing EIPs cannot be used for creating BMSs in a batch. That is, this parameter is invalid in such a case.                                                                                                            |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | eip             | No              | Object          | Specifies the configuration for creating an EIP that will be automatically assigned to the BMS. For details, see :ref:`Table 12 <en-us_topic_0106040941__table139542215219>`.                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   You can configure either but not both of **id** and **eip** in the **publicip** field.

.. _en-us_topic_0106040941__table338522873815:

.. table:: **Table 7** **root_volume** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                               |
   +=================+=================+=================+===========================================================================================================================+
   | volumetype      | Yes             | String          | Specifies the BMS system disk type. The disk type must match the available disk type.                                     |
   |                 |                 |                 |                                                                                                                           |
   |                 |                 |                 | -  SAS: high I/O disk type                                                                                                |
   |                 |                 |                 | -  SSD: ultra-high I/O disk type                                                                                          |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+
   | size            | Yes             | Integer         | Specifies the system disk size (GB). The value ranges from **40** to **1024**.                                            |
   |                 |                 |                 |                                                                                                                           |
   |                 |                 |                 | Constraints:                                                                                                              |
   |                 |                 |                 |                                                                                                                           |
   |                 |                 |                 | The system disk size must be greater than or equal to the minimum system disk size of the image (**min_disk** attribute). |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table16541153834413:

.. table:: **Table 8** **data_volumes** data structure

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                         |
   +=================+=================+=================+=====================================================================================+
   | volumetype      | Yes             | String          | Specifies the BMS data disk type. The disk type must match the available disk type. |
   |                 |                 |                 |                                                                                     |
   |                 |                 |                 | -  SAS: high I/O disk type                                                          |
   |                 |                 |                 | -  SSD: ultra-high I/O disk type                                                    |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------+
   | size            | Yes             | Integer         | Specifies the data disk size (GB). The value ranges from **10** to **32768**.       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------+
   | shareable       | No              | Boolean         | Specifies whether the disk is shareable.                                            |
   |                 |                 |                 |                                                                                     |
   |                 |                 |                 | -  **true**: shared EVS disk                                                        |
   |                 |                 |                 | -  **false**: common EVS disk                                                       |
   |                 |                 |                 |                                                                                     |
   |                 |                 |                 | The default value is **false**.                                                     |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table12971921194613:

.. table:: **Table 9** **extendparam** data structure for creating BMSs

   +-----------------+-----------------+-----------------+-------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                           |
   +=================+=================+=================+=======================================================+
   | chargingMode    | No              | String          | Specifies the billing mode. Value range:              |
   |                 |                 |                 |                                                       |
   |                 |                 |                 | **postPaid**: pay-per-use billing                     |
   +-----------------+-----------------+-----------------+-------------------------------------------------------+
   | regionID        | No              | String          | Specifies the ID of the region where the BMS resides. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------+

.. _en-us_topic_0106040941__table615418218465:

.. table:: **Table 10** **schedulerHints** data structure

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                               |
   +=================+=================+=================+===========================================================================================+
   | dec_baremetal   | No              | String          | Specifies whether to create the BMS in a DeC. The value can be **share** or **dedicate**. |
   |                 |                 |                 |                                                                                           |
   |                 |                 |                 | Constraints:                                                                              |
   |                 |                 |                 |                                                                                           |
   |                 |                 |                 | -  If this parameter is not specified, the default value is **share**.                    |
   |                 |                 |                 | -  To create the BMS in a DeC, set this parameter to **dedicate**.                        |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table106007521267:

.. table:: **Table 11** **server_tags** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                           |
   +=================+=================+=================+=======================================================================================+
   | key             | Yes             | String          | Specifies the tag key.                                                                |
   |                 |                 |                 |                                                                                       |
   |                 |                 |                 | -  It contains a maximum of 36 Unicode characters and cannot be empty.                |
   |                 |                 |                 | -  It cannot contain ASCII characters (0-31) or special characters ``=*<>\,|/``       |
   |                 |                 |                 | -  The tag key of a BMS must be unique.                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------+
   | value           | No              | String          | Specifies the tag value.                                                              |
   |                 |                 |                 |                                                                                       |
   |                 |                 |                 | -  Each value contains a maximum of 43 Unicode characters and can be an empty string. |
   |                 |                 |                 | -  It cannot contain ASCII characters (0-31) or special characters ``=*<>\,|/``       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table139542215219:

.. table:: **Table 12** **eip** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================+
   | iptype          | Yes             | String          | Specifies the EIP type.                                                                                                         |
   |                 |                 |                 |                                                                                                                                 |
   |                 |                 |                 | Enumerated values: **5_bgp** and **5_sbgp**                                                                                     |
   |                 |                 |                 |                                                                                                                                 |
   |                 |                 |                 | For details, see the **publicip** field in "Assigning an EIP" in *Elastic IP API Reference*.                                    |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------+
   | bandwidth       | Yes             | Object          | Specifies the EIP bandwidth. For details, see :ref:`Table 13 <en-us_topic_0106040941__table189859220525>`.                      |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------+
   | extendparam     | Yes             | Object          | Provides additional information about the EIP. For details, see :ref:`Table 14 <en-us_topic_0106040941__table143091715113419>`. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table189859220525:

.. table:: **Table 13** **bandwidth** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================================================================================================================================================================================================================================================================+
   | name            | No              | String          | Specifies the bandwidth name.                                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sharetype       | Yes             | String          | Specifies the bandwidth sharing type.                                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | Value **PER** indicates dedicated bandwidth and **WHOLE** indicates shared bandwidth.                                                                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | id              | No              | String          | Specifies the shared bandwidth ID. You can specify an existing shared bandwidth when applying for an EIP with a **WHOLE** bandwidth.                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |    This parameter is mandatory when **sharetype** is set to **WHOLE**.                                                                                                                                                                                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | size            | Yes             | Integer         | -  The value ranges from 5 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can view the bandwidth range of each region on the management console.)                                                                                                                                                                                    |
   |                 |                 |                 | -  Specifies the bandwidth (Mbit/s). The minimum shared bandwidth is 5 Mbit/s by default.                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |    -  If a decimal fraction (for example **10.2**) or a character string (for example **10**) is specified, the specified value will be automatically converted to an integer. If the bandwidth is less than 300 Mbit/s, the step is 1 Mbit/s. If the bandwidth is from 300 Mbit/s to 1000 Mbit/s, the step is 50 Mbit/s. If the bandwidth is from 1000 Mbit/s to 2000 Mbit/s, the step is 1000 Mbit/s. |
   |                 |                 |                 |    -  This parameter is mandatory when **sharetype** is set to **PER** and is optional when **sharetype** is set to **WHOLE** with an ID specified.                                                                                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | chargemode      | No              | String          | Specifies the bandwidth billing mode.                                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | The value can be **traffic** or **bandwidth**.                                                                                                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | -  If this field is not specified, the BMS is billed by bandwidth.                                                                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 | -  If the field value is empty, the BMS is billed by bandwidth.                                                                                                                                                                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table143091715113419:

.. table:: **Table 14** **extendparam** data structure for assigning an EIP

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================================================================================================+
   | chargingMode    | Yes             | String          | Specifies the billing mode of an EIP. If bandwidth is charged by **bandwidth**, both **prePaid** and **postPaid** will be available for EIP. If bandwidth is charged by **traffic**, only **postPaid** will be available for EIP. |
   |                 |                 |                 |                                                                                                                                                                                                                                   |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                   |
   |                 |                 |                 | -  **prePaid**                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **postPaid**                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Request
---------------

-  Creating a pay-per-use BMS

   .. code-block::

      {
          "server":
          {
              "count": 1,
              "extendparam":
              {
                  "chargingMode": "postPaid"
              },
              "vpcid": "8b4e7a59-2bb9-4daf-a31a-2e72db451a3e",
              "name": "bms-local",
              "imageRef": "b7d6d5a1-7588-421c-8730-8a2b5549e5d9",
              "availability_zone": "eu-de-01",
              "nics": [
                  {
                      "subnet_id": "9cdc46bc-4d1a-44a9-af13-492f533d0299",
                      "ip_address": ""
                  }],
              "flavorRef": "physical.comtest07.large.ondemand",
              "adminPass": "Test",
              "user_data": "$USER_DATA",
              "metadata":
              {
                  "admin_pass": "$ADMIN_PASS",
                  "BYOL": "false",
                  "op_svc_userid": "e81efc34179c4186bd2bd4f9a2378cac"
              }
          }
      }

Response Parameters
-------------------

.. table:: **Table 15** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | order_id              | String                | Specifies the order ID returned after an order is submitted. You can query the order processing progress based on the ID.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 16** Abnormal response

   +-----------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                          | Description                                                                                                                                                 |
   +===========+===============================+=============================================================================================================================================================+
   | error     | Dictionary data structure [1] | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 17 <en-us_topic_0106040941__table6409189311151>`. |
   +-----------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0106040941__table6409189311151:

.. table:: **Table 17** **error** data structure

   ========= ====== ============================
   Parameter Type   Description
   ========= ====== ============================
   message   String Specifies the error message.
   code      String Specifies the error code.
   ========= ====== ============================

Example Response
----------------

-  Normal response

   .. code-block::

      {
          "order_id": "CS2009141523OQSEQ",
          "job_id": "ff808081748b760c01748b7f80370003"
      }

Returned Values
---------------

Normal values

=============== ============================================
Returned Values Description
=============== ============================================
200             The request has been successfully processed.
=============== ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
