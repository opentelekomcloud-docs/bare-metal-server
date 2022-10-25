:original_name: en-us_topic_0053158665.html

.. _en-us_topic_0053158665:

Querying Information About a Disk Attached to a BMS (Native OpenStack API)
==========================================================================

Function
--------

This API is used to query information about a single disk attached to a BMS based on the disk ID.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}

:ref:`Table 1 <en-us_topic_0053158665__table17269134917502>` lists the parameters.

.. _en-us_topic_0053158665__table17269134917502:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                                                     |
   +=======================+=======================+=================================================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                                                       |
   |                       |                       |                                                                                                                                                                                 |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__.                           |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                                                           |
   |                       |                       |                                                                                                                                                                                 |
   |                       |                       | You can obtain the BMS ID from the BMS console or using the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>` API.                                           |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_id             | Yes                   | Specifies the EVS disk ID.                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                 |
   |                       |                       | You can query attached EVS disks attached to a BMS using the :ref:`Querying Information About the Disks Attached to a BMS (Native OpenStack API) <en-us_topic_0053158658>` API. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments/b53f23bd-ee8f-49ec-9420-d1acfeaf91d6

Response
--------

-  Response parameters

   +------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter        | Type   | Description                                                                                                                        |
   +==================+========+====================================================================================================================================+
   | volumeAttachment | Object | Specifies information about the disk attached to the BMS. For details, see :ref:`Table 2 <en-us_topic_0053158665__table42716605>`. |
   +------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158665__table42716605:

   .. table:: **Table 2** **volumeAttachment** field data structure description

      +-----------+--------+--------------------------------------------------------------+
      | Parameter | Type   | Description                                                  |
      +===========+========+==============================================================+
      | device    | String | Specifies the mount directory, for example, **/dev/vdb**.    |
      +-----------+--------+--------------------------------------------------------------+
      | id        | String | Specifies the ID of the attached resource.                   |
      +-----------+--------+--------------------------------------------------------------+
      | serverId  | String | Specifies the ID of the BMS to which the disks are attached. |
      +-----------+--------+--------------------------------------------------------------+
      | volumeId  | String | Specifies the ID of the disk attached to the BMS.            |
      +-----------+--------+--------------------------------------------------------------+

-  Example response

   ::

      {
          "volumeAttachment": {
              "device": "/dev/vdb",
              "serverId": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa",
              "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
              "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6"
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
