:original_name: en-us_topic_0131326852.html

.. _en-us_topic_0131326852:

Querying Flavor Details and Extended Flavor Information
=======================================================

Function
--------

This API is used to query BMS flavor details and extended flavor information. You can call this API to query the value of parameter **baremetal:extBootType** to check whether a flavor supports quick BMS provisioning.

URI
---

GET /v1/{project_id}/baremetalservers/flavors

:ref:`Table 1 <en-us_topic_0131326852__table50905282>` lists the parameters.

.. _en-us_topic_0131326852__table50905282:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                   |
   |                       |                       |                                                                                                             |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Parameters for querying BMS flavors

   ================= ========= ====== ======================
   Parameter         Mandatory Type   Description
   ================= ========= ====== ======================
   availability_zone No        String Specifies the AZ name.
   ================= ========= ====== ======================

Request Parameters
------------------

None

Example Request
---------------

Querying BMS flavor details and extended flavor information in the **az1** AZ

.. code-block:: text

   GET https://{BMS Endpoint}/v1/c685484a8cc2416b97260938705deb65/baremetalservers/flavors?availability_zone=az1

Response Parameters
-------------------

+-----------+------------------+-------------------------------------------------------------------------------------------------+
| Parameter | Type             | Description                                                                                     |
+===========+==================+=================================================================================================+
| flavors   | Array of objects | Specifies BMS flavors. For details, see :ref:`Table 3 <en-us_topic_0131326852__table15697576>`. |
+-----------+------------------+-------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131326852__table15697576:

.. table:: **Table 3** **flavors** data structure

   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | Parameter                  | Type                  | Description                                                                                                          |
   +============================+=======================+======================================================================================================================+
   | id                         | String                | Specifies the ID of a BMS flavor.                                                                                    |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | name                       | String                | Specifies the name of a BMS flavor.                                                                                  |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | vcpus                      | String                | Specifies the number of CPU cores in a BMS flavor.                                                                   |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | ram                        | Integer               | Specifies the memory size (MB) in a BMS flavor.                                                                      |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | disk                       | String                | Specifies the system disk size in a BMS flavor. The value **0** indicates that the disk size is not limited.         |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | swap                       | String                | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | OS-FLV-EXT-DATA:ephemeral  | Integer               | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | OS-FLV-DISABLED:disabled   | Boolean               | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | rxtx_factor                | Float                 | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | rxtx_quota                 | String                | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | rxtx_cap                   | String                | This is a reserved attribute.                                                                                        |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | os-flavor-access:is_public | Boolean               | Specifies whether a flavor is public.                                                                                |
   |                            |                       |                                                                                                                      |
   |                            |                       | **false** indicates a private flavor and **true** indicates a public flavor.                                         |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | links                      | Array of objects      | Specifies shortcut links of a flavor. For details, see :ref:`Table 4 <en-us_topic_0131326852__table35958848194647>`. |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
   | os_extra_specs             | Object                | Specifies extended fields of a BMS flavor. For details, see :ref:`Table 5 <en-us_topic_0131326852__table59078165>`.  |
   +----------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131326852__table35958848194647:

.. table:: **Table 4** **links** data structure

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
   | type                  | String                | Specifies the shortcut link type.                                                                           |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131326852__table59078165:

.. table:: **Table 5** **os_extra_specs** data structure

   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                    | Type                  | Description                                                                                                                                                     |
   +==============================+=======================+=================================================================================================================================================================+
   | resource_type                | String                | Specifies the resource type of a flavor.                                                                                                                        |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | capabilities:cpu_arch        | String                | Specifies the CPU architecture of the BMS. The value can be:                                                                                                    |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | -  **x86_64** (applicable to x86 servers)                                                                                                                       |
   |                              |                       | -  **aarch64** (applicable to Arm servers)                                                                                                                      |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:disk_detail        | String                | Specifies physical disk specifications.                                                                                                                         |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | capabilities:hypervisor_type | String                | Specifies a flavor of the Ironic type.                                                                                                                          |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:__support_evs      | String                | Specifies whether a flavor supports EVS disks.                                                                                                                  |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | -  true                                                                                                                                                         |
   |                              |                       | -  false                                                                                                                                                        |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | If the flavor of a BMS does not contain this parameter, EVS disks cannot be attached to the BMS.                                                                |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:extBootType        | String                | Specifies the boot source of the BMS.                                                                                                                           |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | -  **LocalDisk**: local disk                                                                                                                                    |
   |                              |                       | -  **Volume**: EVS disk (quick provisioning)                                                                                                                    |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | capabilities:board_type      | String                | Specifies the type of a BMS flavor in the format of flavor abbreviation. For example, if the flavor name is **physical.o2.medium**, the flavor type is **o2m**. |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:net_num            | String                | Specifies the maximum number of NICs on the BMS.                                                                                                                |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:netcard_detail     | String                | Specifies physical NIC specifications.                                                                                                                          |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:cpu_detail         | String                | Specifies physical CPU specifications.                                                                                                                          |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | baremetal:memory_detail      | String                | Specifies physical memory specifications.                                                                                                                       |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cond:operation:status        | String                | Specifies the status of a BMS flavor. If this parameter is not set, its default value is **normal**.                                                            |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | -  **normal**: indicates normal commercial use of the flavor.                                                                                                   |
   |                              |                       | -  **abandon**: indicates that the flavor has been disabled (not displayed).                                                                                    |
   |                              |                       | -  **sellout**: indicates that the flavor has been sold out.                                                                                                    |
   |                              |                       | -  **obt**: indicates that the flavor is under OBT.                                                                                                             |
   |                              |                       | -  **promotion**: indicates the recommended flavor (commercial use, which is similar to **normal**).                                                            |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cond:operation:az            | String                | Specifies the status of a BMS flavor in an AZ.                                                                                                                  |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | This parameter takes effect AZ-wide. If an AZ is not configured in this parameter, the value of the **cond:operation:status** parameter is used by default.     |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | Its format is az (*xx*). *xx* indicates the status of a BMS flavor in an AZ, and it is mandatory.                                                               |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | For example, a flavor is for commercial use in AZ0 and AZ3, sold out in AZ1, for OBT in AZ2, and is canceled in other AZs. Then, set parameters as follows:     |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | -  **cond:operation:status**: **abandon**                                                                                                                       |
   |                              |                       | -  **cond:operation:az**: **az0(normal), az1(sellout), az2(obt), az3(promotion)**                                                                               |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       | .. note::                                                                                                                                                       |
   |                              |                       |                                                                                                                                                                 |
   |                              |                       |    Configure this parameter if the flavor status in an AZ is different from the **cond:operation:status** value.                                                |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "flavors": [
            {
               "id": "physical.kl1.3xlarge",
               "name": "physical.kl1.3xlarge",
               "vcpus": "24",
               "ram": 321729,
               "disk": "6707",
               "swap": "",
               "links": [
                   {
                       "rel": "self",
                       "href": "https://compute.Region.dc1.domainname.com/v2/bbf1946d374b44a0a2a95533562ba954/flavors/physical.kl1.3xlarge",
                       "type": null
                   },
                   {
                       "rel": "bookmark",
                       "href": "https://compute.Region.dc1.domainname.com/bbf1946d374b44a0a2a95533562ba954/flavors/physical.kl1.3xlarge",
                       "type": null
                   }
               ],
               "OS-FLV-EXT-DATA:ephemeral": 0,
               "rxtx_factor": 1,
               "OS-FLV-DISABLED:disabled": false,
               "rxtx_quota": null,
               "rxtx_cap": null,
               "os-flavor-access:is_public": false,
               "os_extra_specs": {
                   "capabilities:cpu_arch": "x86_64",
                   "baremetal:disk_detail": "SAS SSD:2*800G Raid 1 + NVMe SSD Card1.6T",
                   "capabilities:hypervisor_type": "ironic",
                   "baremetal:__support_evs": "true",
                   "baremetal:extBootType": "LocalDisk",
                   "capabilities:board_type": "o2m",
                   "baremetal:net_num": "2",
                   "baremetal:netcard_detail": "2 x 2*10GE",
                   "baremetal:cpu_detail": "Intel Xeon E5-2667 V4 (2*8core* 3.2 GHz)",
                   "resource_type": "ironic",
                   "baremetal:memory_detail": "256GB DDR4 RAM(GB)"
               }
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
