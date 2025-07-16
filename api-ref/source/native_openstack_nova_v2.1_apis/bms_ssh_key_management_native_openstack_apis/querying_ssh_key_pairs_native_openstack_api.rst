:original_name: en-us_topic_0000002374101041.html

.. _en-us_topic_0000002374101041:

Querying SSH Key Pairs (Native OpenStack API)
=============================================

Function
--------

This API is used to query SSH key pairs.

Constraints
-----------

Pagination query is not supported.

URI
---

GET /v2.1/{project_id}/os-keypairs

:ref:`Table 1 <en-us_topic_0000002374101041__en-us_topic_0060384658_table875418115417>` lists the parameters.

.. _en-us_topic_0000002374101041__en-us_topic_0060384658_table875418115417:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying SSH key pairs in a project (ID: bbf1946d374b44a0a2a95533562ba954)

.. code-block:: text

   GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs

Response Parameters
-------------------

+-----------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Type             | Description                                                                                                                      |
+===========+==================+==================================================================================================================================+
| keypairs  | Array of objects | Specifies key pairs. For details, see :ref:`Table 2 <en-us_topic_0000002374101041__en-us_topic_0060384658_table31933500103718>`. |
+-----------+------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002374101041__en-us_topic_0060384658_table31933500103718:

.. table:: **Table 2** **keypairs** data structure

   +-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                                                                     |
   +===========+========+=================================================================================================================================================+
   | keypair   | Object | Specifies details about a key pair. For details, see :ref:`Table 3 <en-us_topic_0000002374101041__en-us_topic_0060384658_table58497453103718>`. |
   +-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002374101041__en-us_topic_0060384658_table58497453103718:

.. table:: **Table 3** **keypair** data structure

   +-----------------------+-----------------------+-------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                 |
   +=======================+=======================+=============================================================+
   | fingerprint           | String                | Specifies fingerprint information about the key pair.       |
   +-----------------------+-----------------------+-------------------------------------------------------------+
   | name                  | String                | Specifies the key pair name.                                |
   +-----------------------+-----------------------+-------------------------------------------------------------+
   | type                  | String                | Specifies the key type, which is **ssh** by default.        |
   |                       |                       |                                                             |
   |                       |                       | This field is supported in microversions later than 2.2.    |
   +-----------------------+-----------------------+-------------------------------------------------------------+
   | public_key            | String                | Specifies information about the public key in the key pair. |
   +-----------------------+-----------------------+-------------------------------------------------------------+

Example Response
----------------

::

   {
       "keypairs": [
           {
               "keypair": {
                   "fingerprint": "15:b0:f8:b3:f9:48:63:71:cf:7b:5b:38:6d:44:2d:4a",
                   "name": "keypair-test",
                   "type": "ssh",
                   "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC+Eo/RZRngaGTkFs7I62ZjsIlO79KklKbMXi8F+KITD4bVQHHn+kV+4gRgkgCRbdoDqoGfpaDFs877DYX9n4z6FrAIZ4PES8TNKhatifpn9NdQYWA+IkU8CuvlEKGuFpKRi/k7JLos/gHi2hy7QUwgtRvcefvD/vgQZOVw/mGR9Q== Generated-by-Nova"
               }
           }
       ]
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
