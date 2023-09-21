:original_name: en-us_topic_0053158687.html

.. _en-us_topic_0053158687:

Querying Information About a Specified BMS NIC (Native OpenStack API)
=====================================================================

Function
--------

This API is used to query information about a specified BMS NIC based on the NIC ID.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/os-interface/{id}

:ref:`Table 1 <en-us_topic_0053158687__table1210415012480>` lists the parameters.

.. _en-us_topic_0053158687__table1210415012480:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                                                                                                              |
   +=======================+=======================+==========================================================================================================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                                                                                                                |
   |                       |                       |                                                                                                                                                                                                                                          |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__.                                                                                    |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                                                                                                                    |
   |                       |                       |                                                                                                                                                                                                                                          |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`.                                                                                                   |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | id                    | Yes                   | Specifies the ID of the NIC.                                                                                                                                                                                                             |
   |                       |                       |                                                                                                                                                                                                                                          |
   |                       |                       | You can obtain the NIC ID from the **NICs** tab page on the BMS details page or by calling the :ref:`Querying Information About BMS NICs (Native OpenStack API) <en-us_topic_0053158678>` API. (The NIC ID is the value of **port_id**). |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-interface/ce531f90-199f-48c0-816c-13e38010b442

Response
--------

-  Response parameters

   +---------------------+--------+-----------------------------------------------------------------------------------------------------------------------------+
   | Parameter           | Type   | Description                                                                                                                 |
   +=====================+========+=============================================================================================================================+
   | interfaceAttachment | Object | Specifies information about the specified BMS NIC. For details, see :ref:`Table 2 <en-us_topic_0053158687__table24005299>`. |
   +---------------------+--------+-----------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158687__table24005299:

   .. table:: **Table 2** **interfaceAttachment** field data structure description

      +------------+------------------+--------------------------------------------------------------------------------------------------------------+
      | Parameter  | Type             | Description                                                                                                  |
      +============+==================+==============================================================================================================+
      | port_state | String           | Specifies the status of the NIC port. The value can be **ACTIVE**, **BUILD**, or **DOWN**.                   |
      +------------+------------------+--------------------------------------------------------------------------------------------------------------+
      | fixed_ips  | Array of objects | Specifies the IP addresses of NICs. For details, see :ref:`Table 3 <en-us_topic_0053158687__table53180163>`. |
      +------------+------------------+--------------------------------------------------------------------------------------------------------------+
      | net_id     | String           | Specifies the ID of the subnet (**network_id**) to which the NIC ports belong.                               |
      +------------+------------------+--------------------------------------------------------------------------------------------------------------+
      | port_id    | String           | Specifies the ID of the NIC port.                                                                            |
      +------------+------------------+--------------------------------------------------------------------------------------------------------------+
      | mac_addr   | String           | Specifies the MAC address of the NIC.                                                                        |
      +------------+------------------+--------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158687__table53180163:

   .. table:: **Table 3** **fixed_ips** field data structure description

      +------------+--------+----------------------------------------------------------------------------------------------------+
      | Parameter  | Type   | Description                                                                                        |
      +============+========+====================================================================================================+
      | subnet_id  | String | Specifies the ID of the subnet (**subnet_id**) corresponding to the private IP address of the NIC. |
      +------------+--------+----------------------------------------------------------------------------------------------------+
      | ip_address | String | Specifies the NIC IP address.                                                                      |
      +------------+--------+----------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "interfaceAttachment": {
              "port_state": "ACTIVE",
              "fixed_ips": [
      {
                      "subnet_id": "f8a6e8f8-c2ec-497c-9f23-da9616de54ef",
                      "ip_address": "192.168.1.3"
                          }
                  ],
              "net_id": "3cb9bc59-5699-4588-a4b1-b87f96708bc6",
              "port_id": "ce531f90-199f-48c0-816c-13e38010b442",
              "mac_addr": "fa:16:3e:4c:2c:30"
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
