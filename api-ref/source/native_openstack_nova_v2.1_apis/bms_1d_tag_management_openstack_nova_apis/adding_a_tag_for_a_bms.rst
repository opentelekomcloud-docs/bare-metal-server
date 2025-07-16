:original_name: en-us_topic_0000002374101049.html

.. _en-us_topic_0000002374101049:

Adding a Tag for a BMS
======================

Function
--------

This API is used to add a tag for a BMS.

You are required to use the HTTP header **X-OpenStack-Nova-API-Version: 2.26** to specify the micro version on the client.

Constraints
-----------

-  A BMS can have a maximum of 50 tags.
-  The tag contains a maximum of 80 characters.
-  The tag cannot start with a period (.).
-  An empty tag cannot be created.

.. note::

   It is recommended that you add the **\__type_baremetal** tag to BMSs to distinguish BMSs from ECSs.

URI
---

PUT /v2.1/{project_id}/servers/{server_id}/tags/{tag}

:ref:`Table 1 <en-us_topic_0000002374101049__en-us_topic_0060410929_table19718185512020>` lists the parameters.

.. _en-us_topic_0000002374101049__en-us_topic_0060410929_table19718185512020:

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
   | tag                   | Yes                   | Specifies the tag information.                                                                                                                        |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | Constraints:                                                                                                                                          |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | -  The tag contains a maximum of 80 characters.                                                                                                       |
   |                       |                       | -  The tag cannot start with a period (.).                                                                                                            |
   |                       |                       | -  An empty tag cannot be created.                                                                                                                    |
   |                       |                       | -  URL encoding is required for special characters.                                                                                                   |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Adding a tag for a BMS (ID: 53206ed0-56de-4d6b-b7ee-ffc62ca26f43)

.. code-block:: text

   PUT https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags/{tag}

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
