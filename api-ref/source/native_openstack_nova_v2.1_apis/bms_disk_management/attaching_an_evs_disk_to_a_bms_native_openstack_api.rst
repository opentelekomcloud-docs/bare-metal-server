:original_name: en-us_topic_0053158614.html

.. _en-us_topic_0053158614:

Attaching an EVS Disk to a BMS (Native OpenStack API)
=====================================================

Function
--------

This API is used to attach an EVS disk to a BMS.

Constraints
-----------

-  A bootable disk cannot be attached to a BMS.
-  A disk cannot be attached to a BMS when the BMS is in the **SUSPENDED** or **PAUSED** state, which is specified using the **OS-EXT-STS:vm_state** parameter.
-  Only a shared disk or a disk in the **available** state can be attached to a BMS.
-  Only EVS disks whose device type is **SCSI** can be attached to a BMS.

URI
---

POST /v2.1/{project_id}/servers/{server_id}/os-volume_attachments

:ref:`Table 1 <en-us_topic_0053158614__table12701051155110>` lists the parameters.

.. _en-us_topic_0053158614__table12701051155110:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or using the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>` API.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +------------------+-----------+--------+--------------------------------------------------------------------------------------------------------------------+
   | Parameter        | Mandatory | Type   | Description                                                                                                        |
   +==================+===========+========+====================================================================================================================+
   | volumeAttachment | Yes       | Object | Specifies the disks to be attached. For details, see :ref:`Table 2 <en-us_topic_0053158614__table40707503151632>`. |
   +------------------+-----------+--------+--------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158614__table40707503151632:

   .. table:: **Table 2** **volumeAttachment** field data structure description

      +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                    |
      +=================+=================+=================+================================================================================================================================================+
      | volumeId        | Yes             | String          | Specifies the ID of the disk to be attached to a BMS.                                                                                          |
      +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
      | device          | No              | String          | Specifies the mount point, such as **/dev/sda** and **/dev/sdb**.                                                                              |
      |                 |                 |                 |                                                                                                                                                |
      |                 |                 |                 | The new disk mount point cannot be the same as an existing one.                                                                                |
      |                 |                 |                 |                                                                                                                                                |
      |                 |                 |                 | The mount point must be specified based on the sequence of existing device names. Otherwise, the system automatically generates a mount point. |
      +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example request

   .. code-block:: text

      POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments

   ::

      {
          "volumeAttachment": {
              "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
              "device": "/dev/sdb"
          }
      }

Response
--------

-  Response parameters

   +------------------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter        | Type   | Description                                                                                                         |
   +==================+========+=====================================================================================================================+
   | volumeAttachment | Object | Specifies the disks attached to a BMS. For details, see :ref:`Table 3 <en-us_topic_0053158614__table548498215180>`. |
   +------------------+--------+---------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158614__table548498215180:

   .. table:: **Table 3** **volumeAttachment** field data structure description

      +-----------+--------+--------------------------------------------------------------------------------------------+
      | Parameter | Type   | Description                                                                                |
      +===========+========+============================================================================================+
      | device    | String | Specifies the device name, for example, **/dev/vdb**.                                      |
      +-----------+--------+--------------------------------------------------------------------------------------------+
      | serverId  | String | Specifies the ID of the BMS to which the disk is to be attached. The ID is in UUID format. |
      +-----------+--------+--------------------------------------------------------------------------------------------+
      | id        | String | Specifies the disk UUID.                                                                   |
      +-----------+--------+--------------------------------------------------------------------------------------------+
      | volumeId  | String | Specifies the attaching ID, which is the same as the UUID.                                 |
      +-----------+--------+--------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "volumeAttachment": {
              "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
              "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
              "serverId": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa",
              "device": "/dev/vdb"
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
