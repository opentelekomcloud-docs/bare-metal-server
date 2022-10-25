:original_name: en-us_topic_0114885743.html

.. _en-us_topic_0114885743:

Querying Details About extra_specs Parameters of a BMS Flavor (Native OpenStack API)
====================================================================================

Function
--------

**extra_specs** parameters specify the key-value pair of a BMS flavor. For example, **baremetal:extBootType** specifies the boot device of the BMS. Its value can be **LocalDisk** (local disk) or **Volume** (EVS disk). If you want to check whether a flavor supports quick provisioning, you can call this API.

URI
---

GET /v2.1/{project_id}/flavors/{flavor_id}/os-extra_specs

:ref:`Table 1 <en-us_topic_0114885743__table955744812451>` lists the parameters.

.. _en-us_topic_0114885743__table955744812451:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flavor_id             | Yes                   | Specifies the flavor ID.                                                                                                                              |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the flavor ID from the BMS console or using the :ref:`Querying BMS Flavors (Native OpenStack API) <en-us_topic_0053158684>` API.       |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/flavors/physical.s2.medium/os-extra_specs

Response
--------

-  Response parameters

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                                        |
   +=======================+=======================+====================================================================================================================================================================================================+
   | extra_specs           | Object                | Specifies the key-value pair of a BMS flavor.                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                                    |
   |                       |                       | -  **capabilities:cpu_arch**: specifies the CPU architecture of the BMS. The value can be **x86_64** (for x86 servers) or **aarch64** (for ARM servers).                                           |
   |                       |                       | -  **baremetal:disk_detail**: specifies the disk description.                                                                                                                                      |
   |                       |                       | -  **capabilities:hypervisor_type**: specifies the hypervisor type. The value is fixed at **ironic**.                                                                                              |
   |                       |                       | -  **baremetal:__support_evs**: specifies whether to support EVS disks. The value can be **true** or **false**. If the flavor does not contain this parameter, EVS disks are not supported either. |
   |                       |                       | -  **baremetal:extBootType**: specifies the boot device of the BMS. The value can be **LocalDisk** (local disk) or **Volume** (EVS disk).                                                          |
   |                       |                       | -  **baremetal:net_num**: specifies the number of NICs that can be attached to a BMS.                                                                                                              |
   |                       |                       | -  **baremetal:netcard_detail**: specifies description of the NIC.                                                                                                                                 |
   |                       |                       | -  **baremetal:cpu_detail**: specifies description of the CPU.                                                                                                                                     |
   |                       |                       | -  **resource_type**: specifies the resource type. The value is fixed at **ironic**.                                                                                                               |
   |                       |                       | -  **baremetal:memory_detail**: specifies description of the memory.                                                                                                                               |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "extra_specs": {
              "capabilities:cpu_arch": "x86_64",
              "baremetal:disk_detail": "SAS 8T",
              "capabilities:hypervisor_type": "ironic",
              "baremetal:__support_evs": "true",
              "baremetal:extBootType": "LocalDisk",
              "capabilities:board_type": "s2m",
              "baremetal:net_num": "2",
              "baremetal:netcard_detail": "2*10GE",
              "baremetal:cpu_detail": "2*8coreIntel Xeon E5-2667 V43.2GHz",
              "resource_type": "ironic",
              "baremetal:memory_detail": "256GB DDR4 RAM(GB)"
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
