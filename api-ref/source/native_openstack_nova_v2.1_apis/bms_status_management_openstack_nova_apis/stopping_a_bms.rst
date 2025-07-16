:original_name: en-us_topic_0000002374260881.html

.. _en-us_topic_0000002374260881:

Stopping a BMS
==============

Function
--------

This API is used to stop a single BMS.

This API has been deprecated. Use the API in :ref:`Stopping BMSs <en-us_topic_0131356393>`.

Constraints
-----------

-  The **OS-EXT-STS:vm_state** attribute (BMS status) must be **active** or **error**.
-  Currently, only forcible stopping is supported.

URI
---

POST /v2.1/{project_id}/servers/{server_id}/action

:ref:`Table 1 <en-us_topic_0000002374260881__en-us_topic_0053158685_table1997078319>` lists the parameters.

.. _en-us_topic_0000002374260881__en-us_topic_0053158685_table1997078319:

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

+-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                                                              |
+===========+===========+========+==========================================================================================================================================================+
| os-stop   | Yes       | Object | Specifies the operation of stopping the BMS. For details, see :ref:`Table 2 <en-us_topic_0000002374260881__en-us_topic_0053158685_table10346346162744>`. |
+-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002374260881__en-us_topic_0053158685_table10346346162744:

.. table:: **Table 2** **os-stop** data structure

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                    |
   +=================+=================+=================+================================================================================================+
   | type            | No              | String          | Specifies the type of the BMS stopping operation.                                              |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  **SOFT**: normal BMS stopping                                                               |
   |                 |                 |                 | -  **HARD**: Forcible BMS stopping                                                             |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 |    .. note::                                                                                   |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 |       Currently, this parameter is invalid. All BMS stopping operations are forcible stopping. |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------+

Example Request
---------------

Stopping a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd)

.. code-block:: text

   POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/action

::

   {
       "os-stop": {}
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
