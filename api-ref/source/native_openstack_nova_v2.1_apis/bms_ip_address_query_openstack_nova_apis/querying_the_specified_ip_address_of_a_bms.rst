:original_name: en-us_topic_0000002340222804.html

.. _en-us_topic_0000002340222804:

Querying the Specified IP Address of a BMS
==========================================

Function
--------

This API is used to query the specified IP address of a BMS based on the network name.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/ips/{vpc_id}

:ref:`Table 1 <en-us_topic_0000002340222804__en-us_topic_0053158662_table6532183934016>` lists the parameters.

.. _en-us_topic_0000002340222804__en-us_topic_0053158662_table6532183934016:

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
   | vpc_id                | Yes                   | Specifies the ID of the VPC where the BMS is located.                                                                                                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying the IP address of a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd) in a specified VPC

.. code-block:: text

   GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/ips/{vpc_id}

Response Parameters
-------------------

+-----------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Parameter             | Type                                                                                                       | Description                                             |
+=======================+============================================================================================================+=========================================================+
| Vpc_id                | Array of :ref:`address <en-us_topic_0000002340222804__en-us_topic_0053158662_table22651992144025>` objects | Specifies the VPC used by the BMS.                      |
|                       |                                                                                                            |                                                         |
|                       |                                                                                                            | **Vpc_id** indicates the ID of the VPC used by the BMS. |
+-----------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. _en-us_topic_0000002340222804__en-us_topic_0053158662_table22651992144025:

.. table:: **Table 2** Network parameter structure description

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
       "5849fdf1-9d79-4589-80c2-fe557990c417": [
           {
               "version": 4,
               "addr": "192.168.1.159"
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
