:original_name: en-us_topic_0000002340063052.html

.. _en-us_topic_0000002340063052:

Deleting Tags from a BMS
========================

Function
--------

This API is used to delete all tags of a BMS.

You are required to use the HTTP header **X-OpenStack-Nova-API-Version: 2.26** to specify the micro version on the client.

Constraints
-----------

.. note::

   -  Tag **\__type_baremetal** is used to identify a BMS. You are not advised to delete this tag. Otherwise, the BMS will be displayed only on the ECS console.
   -  After deleting the **\__type_baremetal** tag, you can add it again by following the instructions in :ref:`Adding a Tag for a BMS <en-us_topic_0000002374101049>`. After the tag is added, the BMS will be displayed on the BMS console.

URI
---

DELETE /v2.1/{project_id}/servers/{server_id}/tags

:ref:`Table 1 <en-us_topic_0000002340063052__en-us_topic_0060410928_table17718161117017>` lists the parameters.

.. _en-us_topic_0000002340063052__en-us_topic_0060410928_table17718161117017:

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

Deleting tags from a BMS (ID: 53206ed0-56de-4d6b-b7ee-ffc62ca26f43)

.. code-block:: text

   DELETE https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags

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
