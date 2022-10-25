:original_name: en-us_topic_0053158693.html

.. _en-us_topic_0053158693:

Querying BMSs (Native OpenStack API)
====================================

Function
--------

This API is used to query BMSs.

Constraints
-----------

-  The query result returned by this interface includes both ECSs and BMSs. You need to filter out the BMSs using the flavor used to create the BMSs or the tags added to the BMSs during BMS creation.
-  If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMSs are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.

URI
---

GET /v2.1/{project_id}/servers{?changes-since={changes-since}&image={image}&flavor={flavor}&name={name}&status={status}&limit={limit}&marker={marker}&tags={tags}&not-tags={not-tags}&reservation_id={reservation_id}&sort_key={sort_key}&sort_dir={sort_dir}}

:ref:`Table 1 <en-us_topic_0053158693__table67612156510>` lists the parameters.

.. _en-us_topic_0053158693__table67612156510:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================================================================================================================================================================================================================+
   | changes-since   | No              | String          | Specifies the timestamp of the last BMS status update. The parameter is in ISO 8601 time format, for example, **2013-06-09T06:42:18Z**.                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | image           | No              | String          | Specifies the image ID.                                                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.                                                                                 |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flavor          | No              | String          | Specifies the flavor ID.                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | You can obtain the flavor ID from the BMS console or using the :ref:`Querying BMS Flavors (Native OpenStack API) <en-us_topic_0053158684>` API.                                                                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name            | No              | String          | Specifies the BMS name. This parameter supports fuzzy matching.                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | For example, the regular expression **?name=bob** will return both **bob** and **bobb**. To obtain only **bob**, you can use a regular expression matching the basic database syntax, such as MySQL or PostgreSQL (official website: https://www.postgresql.org/docs/9.2/static/functions-matching.html).                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | status          | No              | String          | Specifies the BMS status.                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **ACTIVE**: Running, Stopping, Deleting                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **BUILD**: Creating                                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ERROR**: Faulty                                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 | -  **HARD_REBOOT**: Forcibly Restarting                                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 | -  **REBOOT**: Restarting                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **DELETED**: Deleted                                                                                                                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | Specifies the number of BMSs displayed on each page.                                                                                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | marker          | No              | String          | Specifies the BMS ID to which the marker corresponds. The query will start from the next ID.                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | tags            | No              | String          | Queries the BMSs with specified tags.                                                                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | not-tags        | No              | String          | Queries the BMSs with tags not containing the specified value. The value is a list of tag keys.                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    For example, an existing tag is **a.b**. After the tag function upgrade, query the tag using "not-tags=a".                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | reservation_id  | No              | String          | Specifies the reserved ID, which can be used to query BMSs created in a batch.                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_key        | No              | String          | Specifies the BMS sorting attribute, which can be the BMS UUID (**uuid**), BMS status (**vm_state**), BMS name (**display_name**), BMS task status (**task_state**), power status (**power_state**), creation time (**created_at**), last time when the BMS is updated (**updated_at**), and AZ (**availability_zone**). You can specify multiple **sort_key** and **sort_dir** pairs. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | The default sorting is the reverse order by **created_at**.                                                                                                                                                                                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_dir        | No              | String          | Specifies the sorting direction.                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **asc**: The query results are displayed in ascending order.                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **desc** (default value): The query results are displayed in descending order.                                                                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example request

   -  With no optional parameter

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers

   -  With an optional parameter

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers?tags=__type_baremetal

   -  With multiple optional parameters

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers?tags=__type_baremetal&name=bms-test01

Response
--------

-  Response parameters

   +-----------+------------------+--------------------------------------------------------------------------------------------------+
   | Parameter | Type             | Description                                                                                      |
   +===========+==================+==================================================================================================+
   | servers   | Array of objects | Specifies the BMS list. For details, see :ref:`Table 2 <en-us_topic_0053158693__table11253402>`. |
   +-----------+------------------+--------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158693__table11253402:

   .. table:: **Table 2** **servers** field data structure description

      +-----------+------------------+---------------------------------------------------------------------------------------------------------------+
      | Parameter | Type             | Description                                                                                                   |
      +===========+==================+===============================================================================================================+
      | name      | String           | Specifies the BMS name.                                                                                       |
      +-----------+------------------+---------------------------------------------------------------------------------------------------------------+
      | id        | String           | Specifies the unique ID of the BMS.                                                                           |
      +-----------+------------------+---------------------------------------------------------------------------------------------------------------+
      | links     | Array of objects | Specifies shortcut links of the BMS. For details, see :ref:`Table 3 <en-us_topic_0053158693__table64121649>`. |
      +-----------+------------------+---------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158693__table64121649:

   .. table:: **Table 3** **links** field data structure description

      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                 |
      +=======================+=======================+=============================================================================================================+
      | rel                   | String                | Specifies the shortcut link marker name. The value can be:                                                  |
      |                       |                       |                                                                                                             |
      |                       |                       | -  **self**: resource link that contains the version number. It is used when immediate tracing is required. |
      |                       |                       | -  **bookmark**: resource link that can be stored for a long time.                                          |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | href                  | String                | Specifies the corresponding shortcut link.                                                                  |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "servers": [
              {
                  "name": "bms",
                  "links": [
                      {
                          "rel": "self",
                          "href": "https://openstack.example.com/v2.1/c685484a8cc2416b97260938705deb65/servers/820abbd0-2d8b-4bc5-ae46-69cacfd4fbaa"
                      },
                      {
                          "rel": "bookmark",
                          "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa"
                      }
                  ],
                  "id": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa"
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
