:original_name: en-us_topic_0053158658.html

.. _en-us_topic_0053158658:

Querying Information About the Disks Attached to a BMS (Native OpenStack API)
=============================================================================

Function
--------

This API is used to query information about the EVS disks attached to a BMS.

URI
---

GET /v2.1/{project_id}/servers/{server_id}/os-volume_attachments

:ref:`Table 1 <en-us_topic_0053158658__table98221910184910>` lists the parameters.

.. _en-us_topic_0053158658__table98221910184910:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                                 |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`.                |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments

Response
--------

-  Response parameters

   +-------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter         | Type   | Description                                                                                                                        |
   +===================+========+====================================================================================================================================+
   | volumeAttachments | Object | Specifies information about the disks attached to the BMS. For details, see :ref:`Table 2 <en-us_topic_0053158658__table7886611>`. |
   +-------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158658__table7886611:

   .. table:: **Table 2** **volumeAttachments** field data structure description

      +-----------+--------+--------------------------------------------------------------+
      | Parameter | Type   | Description                                                  |
      +===========+========+==============================================================+
      | device    | String | Specifies the mount directory, for example, **/dev/vdb**.    |
      +-----------+--------+--------------------------------------------------------------+
      | id        | String | Specifies the ID of the attached resource.                   |
      +-----------+--------+--------------------------------------------------------------+
      | serverId  | String | Specifies the ID of the BMS to which the disks are attached. |
      +-----------+--------+--------------------------------------------------------------+
      | volumeId  | String | Specifies the IDs of the EVS disks attached to the BMS.      |
      +-----------+--------+--------------------------------------------------------------+

-  Example response

   ::

      {
          "volumeAttachments": {
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
