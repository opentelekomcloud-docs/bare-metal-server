:original_name: en-us_topic_0053158682.html

.. _en-us_topic_0053158682:

Creating a BMS (Native OpenStack API)
=====================================

Function
--------

This interface is used to create a BMS.

Constraints
-----------

-  This interface cannot be used to create BMSs in batches.
-  When you create a BMS using an image that supports Cloud-Init or Cloudbase-Init, only parameter **key_name** can be configured. (Parameter **adminPass** is invalid.) The password of a Linux BMS can be injected only using parameter **user_data**. The password of a Windows BMS can be injected only using metadata **admin_pass**.
-  When you create a BMS using an image that does not support Cloud-Init or Cloudbase-Init, both parameters **adminPass** and **key_name** are invalid. You need to use the password or certificate of the image to log in to the BMS.
-  File injection is not supported.
-  BMS creation from a system volume is not supported.
-  Parameter **port** in the three network parameters (**port**, **uuid**, and **fixed_ip**) has the highest priority. If parameter **fixed_ip** is set, you must specify the UUID.
-  After a BMS is created, it is recommended that you attach the **\__type_baremetal** tag to the BMS. This tag specifies that the created server is a BMS. Otherwise, the BMS may not be displayed in the BMS list on the management console.
-  A BMS can have a maximum of two VPCs, in which case the first VPC will be used by the primary NIC.

URI
---

POST /v2.1/{project_id}/servers

:ref:`Table 1 <en-us_topic_0053158682__table193302233354>` lists the parameters.

.. _en-us_topic_0053158682__table193302233354:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +-----------+-----------+--------+-------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                                                     |
   +===========+===========+========+=================================================================================================+
   | server    | Yes       | Object | Specifies the BMS information, see :ref:`Table 2 <en-us_topic_0053158682__table3034272816824>`. |
   +-----------+-----------+--------+-------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table3034272816824:

   .. table:: **Table 2** **server** field data structure description

      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter         | Mandatory       | Type             | Description                                                                                                                                                                                                                                                                                                                                            |
      +===================+=================+==================+========================================================================================================================================================================================================================================================================================================================================================+
      | imageRef          | Yes             | String           | Specifies the ID of the image used by the BMS or the image resource uniform resource locator (URL).                                                                                                                                                                                                                                                    |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | -  Example image ID: 3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2                                                                                                                                                                                                                                                                                              |
      |                   |                 |                  | -  Example image URL: http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2                                                                                                                                                                                                                                                  |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | .. note::                                                                                                                                                                                                                                                                                                                                              |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  |    -  BMSs using certain flavors do not support all public images provided by the cloud service platform. To obtain the images supported by a BMS flavor, log in to the management console, view the images displayed on the **Create ECS** page, and obtain the image IDs on the **Image Management Service** page.                                   |
      |                   |                 |                  |    -  If the creation fails, modify the parameter settings.                                                                                                                                                                                                                                                                                            |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flavorRef         | Yes             | String           | Specifies the ID or URL of the flavor used by the BMS.                                                                                                                                                                                                                                                                                                 |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | name              | Yes             | String           | Specifies the BMS name. It contains a maximum of 255 characters and cannot be left blank.                                                                                                                                                                                                                                                              |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | metadata          | No              | Object           | Specifies the BMS metadata. The maximum size for both the metadata **key** and **value** is 255 characters. For details, see :ref:`Table 3 <en-us_topic_0053158682__table2549048917552>`.                                                                                                                                                              |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | user_data         | No              | String           | Specifies the user data to be injected during the BMS creation.                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | Text, text files, and .gzip files can be injected. The content to be injected cannot be greater than 32 KB in size. The content to be injected must be encoded with base64.                                                                                                                                                                            |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | adminPass         | No              | String           | Specifies the initial login password of the BMS administrator account. This parameter is invalid for a Linux BMS. The administrator account of a Windows BMS is **Administrator**.                                                                                                                                                                     |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | Password complexity requirements:                                                                                                                                                                                                                                                                                                                      |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | -  The password contains 8 to 26 characters.                                                                                                                                                                                                                                                                                                           |
      |                   |                 |                  | -  The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (``!@$%^-_=+[{}]:,./?``).                                                                                                                                                                           |
      |                   |                 |                  | -  The password cannot contain the username or the username in reverse.                                                                                                                                                                                                                                                                                |
      |                   |                 |                  | -  The Windows BMS password cannot contain the username, the username in reverse order, or more than two consecutive characters in the username.                                                                                                                                                                                                       |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | Note: If this parameter is not specified, a random password will be generated.                                                                                                                                                                                                                                                                         |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | Special characters: ``!@$%^-_=+[{}]:,./?``                                                                                                                                                                                                                                                                                                             |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | security_groups   | No              | Array of objects | Specifies the security group of a BMS. The default value is **default**. This parameter is valid when you specify parameter **network**. You are not allowed to specify multiple security groups. For details, see :ref:`Table 4 <en-us_topic_0053158682__table42731625205411>`.                                                                       |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | networks          | Yes             | Array of objects | Specifies the BMS NICs. For details, see :ref:`Table 5 <en-us_topic_0053158682__table36009093171737>`.                                                                                                                                                                                                                                                 |
      |                   |                 |                  |                                                                                                                                                                                                                                                                                                                                                        |
      |                   |                 |                  | You can specify a maximum of four networks for a BMS, including two VXLAN networks and two GENEVE networks. The first network in the parameter must be a VXLAN network. The network is used as by the primary NIC of the BMS. If multiple groups of network parameters are specified, ensure that the parameters of each group belong to the same VPC. |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | key_name          | No              | String           | Specifies the name of a key pair. This is an extended attribute.                                                                                                                                                                                                                                                                                       |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | availability_zone | Yes             | String           | Specifies information about the AZ to which the BMS belongs. You are not allowed to specify host information.                                                                                                                                                                                                                                          |
      +-------------------+-----------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table2549048917552:

   .. table:: **Table 3** **metadata** field data structure description

      +---------------------------------------+-----------------+-----------------+---------------------------------------------------------+
      | Parameter                             | Mandatory       | Type            | Description                                             |
      +=======================================+=================+=================+=========================================================+
      | User-defined field key and value pair | No              | String          | Specifies the key and value pair of the metadata.       |
      |                                       |                 |                 |                                                         |
      |                                       |                 |                 | Each key or value contains a maximum of 255 characters. |
      +---------------------------------------+-----------------+-----------------+---------------------------------------------------------+

   .. _en-us_topic_0053158682__table42731625205411:

   .. table:: **Table 4** **security_groups** field data structure description

      +-----------+-----------+--------+--------------------------------------------------------------------+
      | Parameter | Mandatory | Type   | Description                                                        |
      +===========+===========+========+====================================================================+
      | name      | Yes       | String | Specifies the name of the security group to which the BMS belongs. |
      +-----------+-----------+--------+--------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table36009093171737:

   .. table:: **Table 5** **networks** field data structure description

      ========= ========= ====== =======================================
      Parameter Mandatory Type   Description
      ========= ========= ====== =======================================
      port      No        String Specifies the UUID of the network port.
      uuid      No        String Specifies the network UUID.
      fixed_ip  No        String Specifies the fixed IP address.
      ========= ========= ====== =======================================

-  Example request

   .. code-block:: text

      POST https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers

   ::

      {
          "server": {
              "imageRef": "1a6635d8-afea-4f2b-abb6-27a202bad319",
              "flavorRef": "physical.o2.medium",
              "name": "bms_name01",
              "availability_zone": "az-dc-1",
              "networks": [
                  {
                      "uuid": "8470310b-bfa2-4edf-8f64-d15196b2b2c9"
                  }
              ]
          }
      }

Response
--------

-  Response parameters

   +-----------+--------+---------------------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                                   |
   +===========+========+===============================================================================================================+
   | server    | Object | Specifies the BMS information. For details, see :ref:`Table 6 <en-us_topic_0053158682__table25637149173128>`. |
   +-----------+--------+---------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table25637149173128:

   .. table:: **Table 6** **server** field data structure description

      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                                                                                                       |
      +=======================+=======================+===================================================================================================================================================================================================+
      | security_groups       | Array of objects      | Specifies information about the BMS security group. For details, see :ref:`Table 7 <en-us_topic_0053158682__table1647050183630>`.                                                                 |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | OS-DCF:diskConfig     | String                | Specifies the disk configuration. The value can be:                                                                                                                                               |
      |                       |                       |                                                                                                                                                                                                   |
      |                       |                       | -  **MANUAL**: The API uses the partitioning scheme in the image and the file system to create a BMS. If the target flavor has a large disk, the API does not partition the remaining disk space. |
      |                       |                       | -  **AUTO**: The API uses a single partition with the same size as the disk of the target flavor to create a BMS. The API automatically adjusts the file system to adapt to the entire partition. |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | id                    | String                | Specifies the BMS ID.                                                                                                                                                                             |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | links                 | Array of objects      | Specifies the shortcut links of the BMS. For details, see :ref:`Table 8 <en-us_topic_0053158682__table3029270918355>`.                                                                            |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | adminPass             | String                | Specifies the initial login password of the BMS administrator account.                                                                                                                            |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table1647050183630:

   .. table:: **Table 7** **security_groups** field data structure description

      +-----------+--------+--------------------------------------------------------------------+
      | Parameter | Type   | Description                                                        |
      +===========+========+====================================================================+
      | name      | String | Specifies the name of the security group to which the BMS belongs. |
      +-----------+--------+--------------------------------------------------------------------+

   .. _en-us_topic_0053158682__table3029270918355:

   .. table:: **Table 8** **links** field data structure description

      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                 |
      +=======================+=======================+=============================================================================================================+
      | rel                   | String                | Specifies the shortcut link marker name. The value can be:                                                  |
      |                       |                       |                                                                                                             |
      |                       |                       | -  **self**: resource link that contains the version number. It is used when immediate tracing is required. |
      |                       |                       | -  **bookmark**: resource link that can be stored for a long time.                                          |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | href                  | String                | Specifies the corresponding shortcut link.                                                                  |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "server": {
              "security_groups": [
                  {
                      "name": "default"
                  }
              ],
              "OS-DCF:diskConfig": "MANUAL",
              "links": [
                  {
                      "rel": "self",
                      "href": "https://openstack.example.com/v2/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                  },
                  {
                      "rel": "bookmark",
                      "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                  }
              ],
              "id": "9ab74d89-61e7-4259-8546-465fdebe4944",
              "adminPass": "RjdD3h8U2DBe"
          }
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
