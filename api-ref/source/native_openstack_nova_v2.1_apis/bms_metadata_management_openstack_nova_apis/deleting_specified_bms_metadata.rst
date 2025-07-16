:original_name: en-us_topic_0000002340063028.html

.. _en-us_topic_0000002340063028:

Deleting Specified BMS Metadata
===============================

Function
--------

This API is used to delete specified BMS metadata.

Constraints
-----------

The BMS **OS-EXT-STS:vm_state** attribute (BMS status) must be **active**, **stopped**, or **paused**.

URI
---

DELETE /v2.1/{project_id}/servers/{server_id}/metadata/{key}

:ref:`Table 1 <en-us_topic_0000002340063028__en-us_topic_0053158683_table12474435113619>` lists the parameters.

.. _en-us_topic_0000002340063028__en-us_topic_0053158683_table12474435113619:

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
   | key                   | Yes                   | Specifies the BMS metadata key value to be deleted.                                                                                                   |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Deleting metadata of a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd)

.. code-block:: text

   DELETE https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/metadata/{key}

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
