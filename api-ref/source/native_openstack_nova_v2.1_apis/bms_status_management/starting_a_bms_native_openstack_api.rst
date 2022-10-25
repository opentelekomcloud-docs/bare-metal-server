:original_name: en-us_topic_0053158659.html

.. _en-us_topic_0053158659:

Starting a BMS (Native OpenStack API)
=====================================

Function
--------

This API is used to start a single BMS.

URI
---

POST /v2.1/{project_id}/servers/{server_id}/action

:ref:`Table 1 <en-us_topic_0053158659__table15103162717019>` lists the parameters.

.. _en-us_topic_0053158659__table15103162717019:

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

   +-----------+-----------+------+---------------------------------------------------------------------------+
   | Parameter | Mandatory | Type | Description                                                               |
   +===========+===========+======+===========================================================================+
   | os-start  | Yes       | null | Specifies the operation of starting the BMS. The data structure is empty. |
   +-----------+-----------+------+---------------------------------------------------------------------------+

-  Example request

   .. code-block:: text

      POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/action

   ::

      {
          "os-start": {}
                          }

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
