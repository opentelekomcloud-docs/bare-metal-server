:original_name: en-us_topic_0000002374101017.html

.. _en-us_topic_0000002374101017:

Restarting a BMS
================

Function
--------

This API is used to restart a single BMS.

Constraints
-----------

Currently, only forcible restart is supported.

URI
---

POST /v2.1/{project_id}/servers/{server_id}/action

:ref:`Table 1 <en-us_topic_0000002374101017__en-us_topic_0053158716_table6943612162916>` lists the parameters.

.. _en-us_topic_0000002374101017__en-us_topic_0053158716_table6943612162916:

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

+-----------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                                                                |
+===========+===========+========+============================================================================================================================================================+
| reboot    | Yes       | Object | Specifies the operation of restarting the BMS. For details, see :ref:`Table 2 <en-us_topic_0000002374101017__en-us_topic_0053158716_table10346346162744>`. |
+-----------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002374101017__en-us_topic_0053158716_table10346346162744:

.. table:: **Table 2** **reboot** data structure

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                  |
   +=================+=================+=================+==============================================================================================+
   | type            | Yes             | String          | Specifies the type of the restart operation.                                                 |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | -  **SOFT**: soft restart                                                                    |
   |                 |                 |                 | -  **HARD**: forcible restart                                                                |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 |    .. note::                                                                                 |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 |       Currently, value **SOFT** is invalid. All BMS restart operations are forcible restart. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+

Example Request
---------------

Restarting a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd)

.. code-block:: text

   POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/action

::

   {
       "reboot": {
           "type": "HARD"
       }
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
