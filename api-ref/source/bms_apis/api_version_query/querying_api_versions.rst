:original_name: en-us_topic_0132973804.html

.. _en-us_topic_0132973804:

Querying API Versions
=====================

Function
--------

This API is used to query all available API versions of the BMS service.

URI
---

GET /

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{BMS Endpoint}/

Response
--------

-  Response parameters

   +-----------+------------------+--------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type             | Description                                                                                                              |
   +===========+==================+==========================================================================================================================+
   | versions  | Array of objects | Specifies API versions of the BMS service. For details, see :ref:`Table 1 <en-us_topic_0132973804__table5036780310489>`. |
   +-----------+------------------+--------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0132973804__table5036780310489:

   .. table:: **Table 1** **versions** field data structure description

      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                         |
      +=======================+=======================+=====================================================================================================================+
      | id                    | String                | Specifies the API version ID.                                                                                       |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | links                 | Array of objects      | Specifies the API URL. For details, see :ref:`Table 2 <en-us_topic_0132973804__t759e6d15d244474e8f286185ede143fb>`. |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | min_version           | String                | Specifies the earliest micro API version that is supported.                                                         |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | status                | String                | Specifies the API version status.                                                                                   |
      |                       |                       |                                                                                                                     |
      |                       |                       | -  **CURRENT**: indicates a primary version.                                                                        |
      |                       |                       | -  **SUPPORTED**: indicates an earlier version which is still supported.                                            |
      |                       |                       | -  **DEPRECATED**: indicates a deprecated version which may be deleted later.                                       |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | updated               | String                | Specifies the release date of an API version.                                                                       |
      |                       |                       |                                                                                                                     |
      |                       |                       | The timestamp format is YYYY-MM-DDTHH:MM:SSZ (ISO 8601), for example, 2018-09-30T00:00:00Z.                         |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | version               | String                | Specifies the latest micro API version that is supported.                                                           |
      +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0132973804__t759e6d15d244474e8f286185ede143fb:

   .. table:: **Table 2** **links** field data structure description

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

-  Example response

   ::

      {
          "versions": [
              {
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
