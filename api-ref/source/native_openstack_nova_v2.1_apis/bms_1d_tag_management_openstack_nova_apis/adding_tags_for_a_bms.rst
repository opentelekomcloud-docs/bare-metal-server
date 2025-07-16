:original_name: en-us_topic_0000002340222824.html

.. _en-us_topic_0000002340222824:

Adding Tags for a BMS
=====================

Function
--------

This API is used to add tags for a BMS.

You are required to use the HTTP header **X-OpenStack-Nova-API-Version: 2.26** to specify the micro version on the client.

Constraints
-----------

A BMS can have a maximum of 50 tags.

.. note::

   -  It is recommended that you add the **\__type_baremetal** tag to BMSs to distinguish BMSs from ECSs. Otherwise, BMSs will be available only on the ECS console.
   -  A new tag will overwrite the existing one. If you want to retain the original tag, add it to the list of new tags. You are advised to add **\__type_baremetal** to the added tags list each time you add a tag.

URI
---

PUT /v2.1/{project_id}/servers/{server_id}/tags

:ref:`Table 1 <en-us_topic_0000002340222824__en-us_topic_0060410927_table7714219185912>` lists the parameters.

.. _en-us_topic_0000002340222824__en-us_topic_0060410927_table7714219185912:

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

+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------+
| Parameter       | Mandatory       | Type             | Description                                                                         |
+=================+=================+==================+=====================================================================================+
| tags            | Yes             | Array of strings | -  Specifies the tags to be added. Each tag can contain a maximum of 80 characters. |
|                 |                 |                  | -  The tag cannot start with a period (.).                                          |
|                 |                 |                  | -  A BMS can have a maximum of 50 tags.                                             |
|                 |                 |                  | -  An empty tag cannot be created.                                                  |
+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------+

Example Request
---------------

Adding tags **baz**, **foo**, and **qux** for a BMS (ID: 53206ed0-56de-4d6b-b7ee-ffc62ca26f43)

.. code-block:: text

   PUT https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags

::

   {
       "tags": [
           "baz",
           "foo",
           "qux"
       ]
   }

Response Parameters
-------------------

========= ================ =====================================
Parameter Type             Description
========= ================ =====================================
tags      Array of strings Specifies user-defined tags of a BMS.
========= ================ =====================================

Example Response
----------------

::

   {
       "tags": [
           "baz",
           "foo",
           "qux"
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
