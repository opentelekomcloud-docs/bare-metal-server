:original_name: en-us_topic_0000002374260889.html

.. _en-us_topic_0000002374260889:

Querying IP Addresses of a BMS
==============================

Function
--------

This API is used to query private IP addresses of a BMS.

Constraints
-----------

Pagination query is not supported.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/ips

:ref:`Table 1 <en-us_topic_0000002374260889__en-us_topic_0053158696_table1152617127395>` lists the parameters.

.. _en-us_topic_0000002374260889__en-us_topic_0053158696_table1152617127395:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                                 |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the API :ref:`Querying BMSs <en-us_topic_0000002340063012>`.                             |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying the private IP addresses of a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd)

.. code-block:: text

   GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/ips

Response Parameters
-------------------

+-----------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| Parameter             | Type                                                                                                                   | Description                                              |
+=======================+========================================================================================================================+==========================================================+
| addresses             | Map<String,Array of :ref:`address <en-us_topic_0000002374260889__en-us_topic_0053158696_table22651992144025>` objects> | Specifies the VPC used by the BMS.                       |
|                       |                                                                                                                        |                                                          |
|                       |                                                                                                                        | -  **key**: indicates the ID of the VPC used by the BMS. |
|                       |                                                                                                                        | -  **value** indicates the VPC details.                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

.. _en-us_topic_0000002374260889__en-us_topic_0053158696_table22651992144025:

.. table:: **Table 2** **address** parameter structure description

   +-----------------------+-----------------------+-----------------------------------------------------+
   | Parameter             | Type                  | Description                                         |
   +=======================+=======================+=====================================================+
   | version               | Integer               | Specifies the IP address version. The value can be: |
   |                       |                       |                                                     |
   |                       |                       | -  **4**: IPv4 address                              |
   |                       |                       | -  **6**: IPv6 address                              |
   +-----------------------+-----------------------+-----------------------------------------------------+
   | addr                  | String                | Specifies the IP address.                           |
   +-----------------------+-----------------------+-----------------------------------------------------+

Example Response
----------------

::

   {
       "addresses": {
           "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
               {
                   "version": 4,
                   "addr": "192.168.2.90"
               }
           ]
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
