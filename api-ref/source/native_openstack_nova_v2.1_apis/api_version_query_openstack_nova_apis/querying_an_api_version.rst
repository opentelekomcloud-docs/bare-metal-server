:original_name: en-us_topic_0000002340222780.html

.. _en-us_topic_0000002340222780:

Querying an API Version
=======================

Function
--------

This API is used to query a specified API version.

URI
---

GET /{api_version}

:ref:`Table 1 <en-us_topic_0000002340222780__en-us_topic_0134720583_table4181222133410>` lists the parameters.

.. _en-us_topic_0000002340222780__en-us_topic_0134720583_table4181222133410:

.. table:: **Table 1** Parameter description

   =========== ========= ==========================================
   Parameter   Mandatory Description
   =========== ========= ==========================================
   api_version Yes       Specifies the API version, for example v2.
   =========== ========= ==========================================

Request Parameters
------------------

None

Example Request
---------------

Querying the API v2

.. code-block:: text

   GET https://{ECS Endpoint}/v2

Response Parameters
-------------------

+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                                                        |
+=======================+=======================+====================================================================================================================================================+
| version               | Object                | Specifies a specified version.                                                                                                                     |
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

Example response
----------------

::

   {
       "version": {
           "min_version": "",
           "media-types": [
               {
                   "type": "application/vnd.openstack.compute+json;version=2",
                   "base": "application/json"
               }
           ],
           "links": [
               {
                   "rel": "self",
                   "href": "https://ecs.service.domain.com:443/v2/"
               },
               {
                   "rel": "describedby",
                   "href": "http://docs.openstack.org/",
                   "type": "text/html"
               }
           ],
           "id": "v2.0",
           "updated": "1999-02-20T11:33:21Z",
           "version": "",
           "status": "SUPPORTED"
       }
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
