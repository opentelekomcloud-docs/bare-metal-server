:original_name: en-us_topic_0131036398.html

.. _en-us_topic_0131036398:

Querying NICs Attached to a BMS
===============================

Function
--------

This API is used to query information about NICs attached to a BMS, such as the IP address and MAC address of each NIC.

URI
---

GET /v1/{project_id}/baremetalservers/{server_id}/os-interface

:ref:`Table 1 <en-us_topic_0131036398__table38523909>` lists the parameters.

.. _en-us_topic_0131036398__table38523909:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                            |
   +=======================+=======================+========================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                              |
   |                       |                       |                                                                                                                                        |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`.                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                  |
   |                       |                       |                                                                                                                                        |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{BMS Endpoint}/v1/c685484a8cc2416b97260938705deb65/baremetalservers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-interface

Response
--------

-  Response parameters

   +----------------------+------------------+----------------------------------------------------------------------------------------------+
   | Parameter            | Type             | Description                                                                                  |
   +======================+==================+==============================================================================================+
   | interfaceAttachments | Array of objects | Specifies BMS NICs. For details, see :ref:`Table 2 <en-us_topic_0131036398__table49805933>`. |
   +----------------------+------------------+----------------------------------------------------------------------------------------------+

   .. _en-us_topic_0131036398__table49805933:

   .. table:: **Table 2** **interfaceAttachments** field data structure description

      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | Parameter   | Type             | Description                                                                                                           |
      +=============+==================+=======================================================================================================================+
      | port_state  | String           | Specifies the NIC port status. The value can be **ACTIVE**, **BUILD**, or **DOWN**.                                   |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | fixed_ips   | Array of objects | Specifies private IP addresses of NICs. For details, see :ref:`Table 3 <en-us_topic_0131036398__table19750463>`.      |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | net_id      | String           | Specifies the ID of the subnet (**network_id**) to which the NIC ports belong.                                        |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | port_id     | String           | Specifies the ID of the NIC port.                                                                                     |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | mac_addr    | String           | Specifies the MAC address of the NIC.                                                                                 |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | driver_mode | String           | Specifies the NIC driver type in Guest OS. The value can be **virtio** or **hinic**. The default value is **virtio**. |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+
      | pci_address | String           | Specifies the BDF number of the NIC in Linux Guest OS.                                                                |
      +-------------+------------------+-----------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0131036398__table19750463:

   .. table:: **Table 3** **fixed_ips** field data structure description

      +------------+--------+----------------------------------------------------------------------------------------------------+
      | Parameter  | Type   | Description                                                                                        |
      +============+========+====================================================================================================+
      | subnet_id  | String | Specifies the ID of the subnet (**subnet_id**) corresponding to the private IP address of the NIC. |
      +------------+--------+----------------------------------------------------------------------------------------------------+
      | ip_address | String | Specifies the NIC private IP address.                                                              |
      +------------+--------+----------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "interfaceAttachments": [
              {
                  "port_state": "ACTIVE",
                  "fixed_ips": [
                      {
                          "subnet_id": "a5052101-11e1-4f3d-a5fa-f6ba6791219c",
                          "ip_address": "192.168.1.147"
                      }
                  ],
                  "net_id": "ad0fadbf-4bc1-472c-a030-5310e53b3818",
                  "port_id": "bb585b04-f2a2-4528-9064-fd0aeb4e15a9",
                  "mac_addr": "fa:16:3e:3b:58:fc"
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
