:original_name: en-us_topic_0113607322.html

.. _en-us_topic_0113607322:

Detaching an EVS Disk from a BMS
================================

Scenario
--------

A disk attached to a BMS can be detached.

-  A disk mounted to **/dev/sda** functions as the system disk. You can only detach the system disk from a stopped BMS.
-  Disks mounted to a mount point other than **/dev/sda** function as data disks and can be detached from a running or stopped BMS.

Restrictions and Limitations
----------------------------

If a BMS is stopped, disks can be detached from it without any limitation on the OS. If a BMS is running, the constraints are as follows:

-  Before detaching an EVS disk from a Linux BMS, log in to the BMS, run the **unmount** command to disassociate the disk to be detached from the file system, and ensure that no program is reading data from or writing data to the disk. Otherwise, the disk will fail to be detached.
-  Before detaching an EVS disk from a Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

Involved APIs
-------------

The following APIs are required:

-  Querying EVS disks attached to a BMS
-  Detaching an EVS disk from a BMS

Procedure
---------

#. Query EVS disks attached to a BMS.

   -  API information

      URI format: GET /v2/{project_id}/servers/{server_id}/os-volume_attachments

      For details, see section "Querying Information About the Disks Attached to a BMS (Native OpenStack API)" in the *Bare Metal Server API Reference*.

   -  Example request

      GET https://{ECS Endpoint}/v2/000efdc5f9064584b718b181df137bd7servers/9ab74d89-61e7-4259-8546-465fdebe4944/os-volume_attachments

   -  Example response

      .. code-block::

         {
             "volumeAttachment": {
                 "device": "/dev/vdb",
                 "serverId": "9ab74d89-61e7-4259-8546-465fdebe4944",
                 "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
                 "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6"
             }
         }

#. Detach an EVS disk from a BMS.

   -  API information

      URI format: DELETE /v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}

      For details, see section "Detaching an EVS Disk from a BMS (Native OpenStack API)" in the *Bare Metal Server API Reference*.

   -  Example request

      DELETE https://{ECS Endpoint}/v2.1/000efdc5f9064584b718b181df137bd7/servers/9ab74d89-61e7-4259-8546-465fdebe4944/os-volume_attachments/b53f23bd-ee8f-49ec-9420-d1acfeaf91d6

   -  Example response

      None
