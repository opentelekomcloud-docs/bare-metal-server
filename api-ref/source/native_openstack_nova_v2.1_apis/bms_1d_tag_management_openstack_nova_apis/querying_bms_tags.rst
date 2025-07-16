:original_name: en-us_topic_0000002374260909.html

.. _en-us_topic_0000002374260909:

Querying BMS Tags
=================

Function
--------

This API is used to query all tags of a BMS.

You are required to use the HTTP header **X-OpenStack-Nova-API-Version: 2.26** to specify the micro version on the client.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/tags

:ref:`Table 1 <en-us_topic_0000002374260909__en-us_topic_0060410926_table0142163245812>` lists the parameters.

.. _en-us_topic_0000002374260909__en-us_topic_0060410926_table0142163245812:

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

Querying tags of a BMS (ID: 53206ed0-56de-4d6b-b7ee-ffc62ca26f43)

.. code-block:: text

   GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags

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
