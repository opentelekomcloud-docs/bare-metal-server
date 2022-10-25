:original_name: en-us_topic_0053158713.html

.. _en-us_topic_0053158713:

Deleting a BMS (Native OpenStack API)
=====================================

Function
--------

This interface is used to delete a BMS.

URI
---

DELETE /v2.1/{project_id}/servers/{server_id}

:ref:`Table 1 <en-us_topic_0053158713__table11676151834514>` lists the parameters.

.. _en-us_topic_0053158713__table11676151834514:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or using the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>` API.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      DELETE https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/9ab74d89-61e7-4259-8546-465fdebe4944

Response
--------

N/A

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
