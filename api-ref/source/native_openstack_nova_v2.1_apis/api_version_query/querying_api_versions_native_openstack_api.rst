:original_name: en-us_topic_0134720582.html

.. _en-us_topic_0134720582:

Querying API Versions (Native OpenStack API)
============================================

Function
--------

This interface is used to query all available Nova versions.

URI
---

GET /

Request Message
---------------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/

Response Message
----------------

-  Response parameters

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                        |
   +=======================+=======================+====================================================================================================================================================+
   | versions              | Array of objects      | Specifies the list of all API versions.                                                                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | id                    | String                | Specifies the version ID, for example, v1.                                                                                                         |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | links                 | Array of objects      | Specifies the API URL.                                                                                                                             |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | href                  | String                | Specifies the reference address of the current API version.                                                                                        |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | rel                   | String                | Specifies the relationship between the current API version and the referenced address.                                                             |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | version               | String                | If the APIs of this version support minor versions, set this parameter to the maximum minor version supported. If not, leave this parameter blank. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | status                | String                | Specifies the version status. Possible values are as follows:                                                                                      |
   |                       |                       |                                                                                                                                                    |
   |                       |                       | -  **CURRENT**: indicates a primary version.                                                                                                       |
   |                       |                       | -  **SUPPORTED**: indicates an old version that is still supported.                                                                                |
   |                       |                       | -  **DEPRECATED**: indicates a deprecated version which may be deleted later.                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | updated               | String                | Specifies the version release time, which must be the UTC time.                                                                                    |
   |                       |                       |                                                                                                                                                    |
   |                       |                       | For example, the release time of v1 is 2014-06-28T12:20:21Z.                                                                                       |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | min_version           | String                | If the APIs of this version support minor versions, set this parameter to the supported minimum minor version. If not, leave this parameter blank. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "versions": [
              {
                  "links": [
                      {
                          "rel": "self",
                          "href": "https://192.168.82.231:443/v2/"
                      }
                  ],
                  "id": "v2.0",
                  "updated": "2018-09-21T12:33:21Z",
                  "status": "SUPPORTED"
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
