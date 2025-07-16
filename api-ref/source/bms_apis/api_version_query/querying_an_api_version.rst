:original_name: en-us_topic_0132973805.html

.. _en-us_topic_0132973805:

Querying an API Version
=======================

Function
--------

This API is used to query a specified API version of the BMS service.

URI
---

GET /{api_version}

:ref:`Table 1 <en-us_topic_0132973805__table46110007>` lists the parameters.

.. _en-us_topic_0132973805__table46110007:

.. table:: **Table 1** Parameter description

   =========== ========= ===========================================
   Parameter   Mandatory Description
   =========== ========= ===========================================
   api_version Yes       Specifies the API version, for example, v1.
   =========== ========= ===========================================

Request Parameters
------------------

None

Example Request
---------------

Querying the API V1

.. code-block:: text

   GET https://{BMS Endpoint}/v1

Response Parameters
-------------------

+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Type   | Description                                                                                                                        |
+===========+========+====================================================================================================================================+
| version   | Object | Specifies a specified API version of the BMS service. For details, see :ref:`Table 2 <en-us_topic_0132973805__table786171513527>`. |
+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0132973805__table786171513527:

.. table:: **Table 2** version data structure

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                         |
   +=======================+=======================+=====================================================================================================================+
   | id                    | String                | Specifies the API version ID.                                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | links                 | Array of objects      | Specifies the API URL. For details, see :ref:`Table 3 <en-us_topic_0132973805__t759e6d15d244474e8f286185ede143fb>`. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | min_version           | String                | Specifies the earliest micro API version that is supported.                                                         |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | status                | String                | Specifies the API version status.                                                                                   |
   |                       |                       |                                                                                                                     |
   |                       |                       | -  **CURRENT**: indicates a primary version.                                                                        |
   |                       |                       | -  **SUPPORTED**: indicates an earlier version that is still supported.                                             |
   |                       |                       | -  **DEPRECATED**: indicates a deprecated version that may be deleted later.                                        |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | updated               | String                | Specifies the release date of an API version.                                                                       |
   |                       |                       |                                                                                                                     |
   |                       |                       | The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2018-09-30T00:00:00Z.                         |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
   | version               | String                | Specifies the latest micro API version that is supported.                                                           |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0132973805__t759e6d15d244474e8f286185ede143fb:

.. table:: **Table 3** links data structure

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | href                  | String                | Specifies the API URL.                                                                                      |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | rel                   | String                | Specifies the API URL dependency. The value can be:                                                         |
   |                       |                       |                                                                                                             |
   |                       |                       | -  **self**: resource link that contains the version number. It is used when immediate tracing is required. |
   |                       |                       | -  **bookmark**: resource link that can be stored for a long time.                                          |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "version": {
           "id": "v1",
           "links": [
               {
                   "href": "http://bms.xxx.com/v1/",
                   "rel": "self"
               }
           ],
           "min_version": "",
           "status": "CURRENT",
           "updated": "2018-09-30T00:00:00Z",
           "version": ""
       }
   }

Returned Values
---------------

Normal values

============ ============================================
Return Value Description
============ ============================================
200          The request has been successfully processed.
============ ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
