:original_name: en-us_topic_0113607321.html

.. _en-us_topic_0113607321:

Attaching an EVS Disk to a BMS
==============================

Scenario
--------

If the existing disks of a BMS fail to meet service requirements, for example, due to insufficient disk space or poor disk performance, you can attach more available disks to the BMS, or call the EVS disk creation API to create disks and attach them to the BMS. To attach an EVS disk to a BMS, you need to call the required API.

Restrictions and Limitations
----------------------------

-  EVS disks cannot be attached to a BMS in a batch.
-  A maximum of EVS disks can be attached to a BMS.
-  A bootable disk cannot be attached to a BMS.
-  A disk cannot be attached to a BMS in the **SUSPENDED** or **PAUSED** state, which is specified using the **OS-EXT-STS:vm_state** parameter.
-  Only a shared disk or a disk in the **available** state can be attached to a BMS.
-  Only EVS disks whose device type is **SCSI** can be attached to a BMS.

Involved APIs
-------------

The following APIs are required:

-  Querying EVS disks
-  Attaching an EVS disk

Procedure
---------

#. Query EVS disks.

   -  API information

      URI format: GET /v2/{project_id}/volumes

      For details, see section "Querying EVS Disks" in the *Elastic Volume Service API Reference*.

   -  Example request

      GET https://{EVS Endpoint}/v2/000efdc5f9064584b718b181df137bd7/volumes

   -  Example response

      .. code-block::

         {
             "volumes": [
                 {
                     "id": "6b604cef-9bd8-4f5a-ae56-45839e6e1f0a",
                     "links": [
                         {
                             "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/6b604cef-9bd8-4f5a-ae56-45839e6e1f0a",
                             "rel": "self"
                         },
                         {
                             "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/6b604cef-9bd8-4f5a-ae56-45839e6e1f0a",
                             "rel": "bookmark"
                         }
                     ],
                     "name": "zjb_u25_test"
                 },
                 {
                     "id": "2bce4552-9a7d-48fa-8484-abbbf64b206e",
                     "links": [
                         {
                             "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/2bce4552-9a7d-48fa-8484-abbbf64b206e",
                             "rel": "self"
                         },
                         {
                             "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/2bce4552-9a7d-48fa-8484-abbbf64b206e",
                             "rel": "bookmark"
                         }
                     ],
                     "name": "zjb_u25_test"
                 },
                 {
                     "id": "3f1b98ec-a8b5-4e92-a727-88def62d5ad3",
                     "links": [
                         {
                             "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/3f1b98ec-a8b5-4e92-a727-88def62d5ad3",
                             "rel": "self"
                         },
                         {
                             "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/3f1b98ec-a8b5-4e92-a727-88def62d5ad3",
                             "rel": "bookmark"
                         }
                     ],
                     "name": "zjb_u25_test"
                 }
             ],
             "volumes_links": [
                 {
                     "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes?limit=3&marker=3f1b98ec-a8b5-4e92-a727-88def62d5ad3",
                     "rel": "next"
                 }
             ]
         }

      or

      .. code-block::

         {
             "error": {
                 "message": "XXXX",
                 "code": "XXX"
             }
         }

      In the preceding example, **error** indicates a general error, for example, **badRequest** or **itemNotFound**. An example is provided as follows:

      .. code-block::

         {
             "badRequest": {
                 "message": "XXXX",
                 "code": "XXX"
             }
         }

#. Attach an EVS disk to a BMS.

   -  API information

      URI format: POST /v2.1/{project_id}/servers/{server_id}/os-volume_attachments

      For details, see section "Attaching an EVS Disk to a BMS (Native OpenStack API)" in the *Bare Metal Server API Reference*.

   -  Example request

      POST https://{ECS Endpoint}/v2.1/000efdc5f9064584b718b181df137bd7/servers/9ab74d89-61e7-4259-8546-465fdebe4944/os-volume_attachments

      .. code-block::

         {
             "volumeAttachment": {
                 "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
                 "device": "/dev/sdb"
             }
         }

   -  Example response

      .. code-block::

         {
             "volumeAttachment": {
                 "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
                 "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
                 "serverId": "9ab74d89-61e7-4259-8546-465fdebe4944",
                 "device": "/dev/vdb"
             }
         }
