:original_name: en-us_topic_0000002374260905.html

.. _en-us_topic_0000002374260905:

Querying an SSH Key Pair (Native OpenStack API)
===============================================

Function
--------

This API is used to query a specified SSH key pair based on the key pair name.

URI
---

GET /v2.1/{project_id}/os-keypairs/{keypair_name}

:ref:`Table 1 <en-us_topic_0000002374260905__en-us_topic_0060384659_table1179423205514>` lists the parameters.

.. _en-us_topic_0000002374260905__en-us_topic_0060384659_table1179423205514:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keypair_name          | Yes                   | Specifies the key pair name.                                                                                                                          |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the key pair name by calling the :ref:`Querying SSH Key Pairs (Native OpenStack API) <en-us_topic_0000002374101041>` API.              |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying details about a key pair (name: keypair-test)

.. code-block:: text

   GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs/keypair-test

Response Parameters
-------------------

+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Type   | Description                                                                                                                             |
+===========+========+=========================================================================================================================================+
| keypair   | Object | Specifies the SSH key pair. For details, see :ref:`Table 2 <en-us_topic_0000002374260905__en-us_topic_0060384659_table39136185104217>`. |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002374260905__en-us_topic_0060384659_table39136185104217:

.. table:: **Table 2** **keypair** data structure

   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                    |
   +=======================+=======================+================================================================================+
   | public_key            | String                | Specifies information about the public key in the key pair.                    |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | name                  | String                | Specifies the key pair name.                                                   |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | fingerprint           | String                | Specifies fingerprint information about the key pair.                          |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | created_at            | String                | Specifies the time when the key pair was created.                              |
   |                       |                       |                                                                                |
   |                       |                       | The timestamp format is ISO 8601, for example, **2019-05-07T12:06:13.681238**. |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | deleted               | Boolean               | Specifies the deleted key pair.                                                |
   |                       |                       |                                                                                |
   |                       |                       | -  **true**: indicates that the key has been deleted.                          |
   |                       |                       | -  **false**: indicates that the key is not deleted.                           |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | deleted_at            | String                | Specifies the time when the key pair was deleted.                              |
   |                       |                       |                                                                                |
   |                       |                       | The timestamp format is ISO 8601, for example, **2019-05-07T12:06:13.681238**. |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | id                    | String                | Specifies the key pair ID.                                                     |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | updated_at            | String                | Specifies the time when the key pair was updated.                              |
   |                       |                       |                                                                                |
   |                       |                       | The timestamp format is ISO 8601, for example, **2019-05-07T12:06:13.681238**. |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | user_id               | String                | Specifies information about the user owning the key pair.                      |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "keypair": {
           "created_at": "2019-05-07T12:06:13.681238",
           "deleted": false,
           "deleted_at": null,
           "fingerprint": "9d:00:f4:d7:26:6e:52:06:4c:c1:d3:1d:fd:06:66:01",
           "id": 1,
           "name": "keypair-3582d8b7-e588-4aad-b7f7-f4e76f0e4314",
           "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYJrTVpcMwFqQy/oMvtUSRofZdSRHEwrsX8AYkRvn2ZnCXM+b6+GZ2NQuuWj+ocznlnwiGFQDsL/yeE+/kurqcPJFKKp60mToXIMyzioFxW88fJtwEWawHKAclbHWpR1t4fQ4DS+/sIbX/Yd9btlVQ2tpQjodGDbM9Tr9/+/3i6rcR+EoLqmbgCgAiGiVV6VbM2Zx79yUwd+GnQejHX8BlYZoOjCnt3NREsITcmWE9FVFy6TnLmahs3FkEO/QGgWGkaohAJlsgaVvSWGgDn2AujKYwyDokK3dXyeX3m2Vmc3ejiqPa/C4nRrCOlko5nSgV/9IXRx1ERImsqZnE9usB Generated-by-Nova",
           "updated_at": null,
           "user_id": "fake"
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
