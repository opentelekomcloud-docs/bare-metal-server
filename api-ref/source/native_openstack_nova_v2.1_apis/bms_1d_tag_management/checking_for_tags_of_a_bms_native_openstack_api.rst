:original_name: en-us_topic_0060410930.html

.. _en-us_topic_0060410930:

Checking for Tags of a BMS (Native OpenStack API)
=================================================

Function
--------

This API is used to check whether a BMS has a specified tag.

You are required to use the HTTP header **X-OpenStack-Nova-API-Version: 2.26** to specify the micro version on the client.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/tags/{tag}

:ref:`Table 1 <en-us_topic_0060410930__table6300135020116>` lists the parameters.

.. _en-us_topic_0060410930__table6300135020116:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`.                |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | tag                   | Yes                   | Specifies the key of the tag to be queried.                                                                                                           |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | Constraints:                                                                                                                                          |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | -  URL encoding is required for special characters.                                                                                                   |
   |                       |                       | -  If no tag key is specified, all tags of the BMS are displayed.                                                                                     |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/2d85af7c-cbfe-40c5-a378-4d03b42fb0e2/tags/{tag}

Response
--------

If the specified tag exists, no response is returned.

If the specified tag does not exist, the response is as follows:

::

   {
       "itemNotFound": {
           "message": "Server 2d85af7c-cbfe-40c5-a378-4d03b42fb0e2 has no tag 'abc'",
           "code": 404
       }
   }

Returned Values
---------------

Normal values

+-----------------+----------------------------------------------------------------------+
| Returned Values | Description                                                          |
+=================+======================================================================+
| 204             | The server has processed the request but did not return any content. |
+-----------------+----------------------------------------------------------------------+

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
