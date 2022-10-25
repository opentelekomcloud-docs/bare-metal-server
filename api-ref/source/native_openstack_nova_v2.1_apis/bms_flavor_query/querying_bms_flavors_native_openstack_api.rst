:original_name: en-us_topic_0053158684.html

.. _en-us_topic_0053158684:

Querying BMS Flavors (Native OpenStack API)
===========================================

Function
--------

This API is used to query BMS flavors.

Constraints
-----------

The flavors you obtained using this API are all the flavors in the system. The flavors whose names starting with **physical** are BMS flavors and can be used to create BMSs.

URI
---

GET /v2.1/{project_id}/flavors/detail{?minDisk={minDisk}&minRam={minRam}&sort_key={sort_key}&sort_dir={sort_dir}}

:ref:`Table 1 <en-us_topic_0053158684__table1687344817416>` lists the parameters.

.. _en-us_topic_0053158684__table1687344817416:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

:ref:`Table 2 <en-us_topic_0053158684__table1719300427>` lists the optional parameters that can be used to query BMS flavors.

.. _en-us_topic_0053158684__table1719300427:

.. table:: **Table 2** Optional parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================================================+
   | minDisk         | No              | String          | Specifies the minimum disk size in GB. Only the BMSs with a disk size greater than or equal to the minimum size can be queried.                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | minRam          | No              | String          | Specifies the minimum memory size in MB. Only the BMSs with the memory size greater than or equal to the minimum size can be queried.                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_key        | No              | String          | Specifies the sorting field. The default value is **flavorid**. The value of this parameter can also be **name**, **memory_mb**, **vcpus**, **root_gb**, or **flavorid**. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_dir        | No              | String          | Specifies the sorting of BMS flavors.                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | The value can be **asc** or **desc**, and is **asc** by default.                                                                                                          |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   -  With no optional parameter

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/flavors/detail

   -  With an optional parameter

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/flavors/detail?minDisk=3725

   -  With multiple optional parameters

      .. code-block:: text

         GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/flavors/detail?minDisk=3725&is_public=true

Response
--------

-  Response parameters

   +-----------+------------------+-------------------------------------------------------------------------------------------------+
   | Parameter | Type             | Description                                                                                     |
   +===========+==================+=================================================================================================+
   | flavors   | Array of objects | Specifies BMS flavors. For details, see :ref:`Table 3 <en-us_topic_0053158684__table13194498>`. |
   +-----------+------------------+-------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158684__table13194498:

   .. table:: **Table 3** **flavors** field data structure description

      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | Parameter                  | Type             | Description                                                                                                                |
      +============================+==================+============================================================================================================================+
      | id                         | String           | Specifies the BMS flavor ID.                                                                                               |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | name                       | String           | Specifies the BMS flavor name.                                                                                             |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | vcpus                      | Integer          | Specifies the number of CPU cores in the BMS flavor.                                                                       |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | ram                        | Integer          | Specifies the memory size (MB) in the BMS flavor.                                                                          |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | disk                       | Integer          | Specifies the disk size (GB) in the BMS flavor.                                                                            |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | swap                       | String           | This is a reserved attribute.                                                                                              |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | OS-FLV-EXT-DATA:ephemeral  | Integer          | This is a reserved attribute.                                                                                              |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | OS-FLV-DISABLED:disabled   | Boolean          | This is a reserved attribute.                                                                                              |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | rxtx_factor                | Float            | This is a reserved attribute.                                                                                              |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | os-flavor-access:is_public | Boolean          | This is a reserved attribute.                                                                                              |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+
      | links                      | Array of objects | Specifies shortcut links of the BMS flavor. For details, see :ref:`Table 4 <en-us_topic_0053158684__table15913898194628>`. |
      +----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158684__table15913898194628:

   .. table:: **Table 4** **links** field data structure description

      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                 |
      +=======================+=======================+=============================================================================================================+
      | rel                   | String                | Specifies the shortcut link marker name.                                                                    |
      |                       |                       |                                                                                                             |
      |                       |                       | -  **self**: resource link that contains the version number. It is used when immediate tracing is required. |
      |                       |                       | -  **bookmark**: resource link that can be stored for a long time.                                          |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
      | href                  | String                | Specifies the corresponding shortcut link.                                                                  |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

-  Example response

   .. code-block::

      {
          "flavors": [
              {
                  "name": "physical.o2.medium",
                  "links": [
                      {
                          "href": "https://openstack.example.com/v2/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                          "rel": "self"
                      },
                      {
                          "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                          "rel": "bookmark"
                       }
                  ],
                  "ram": 321725,
                  "OS-FLV-DISABLED:disabled": false,
                  "vcpus": 56,
                  "swap": "",
                  "os-flavor-access:is_public": true,
                  "rxtx_factor": 1,
                  "OS-FLV-EXT-DATA:ephemeral": 0,
                  "disk": 3725,
                  "id": "physical.o2.medium"
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
