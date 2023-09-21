:original_name: en-us_topic_0053158611.html

.. _en-us_topic_0053158611:

Detaching an EVS Disk from a BMS (Native OpenStack API)
=======================================================

Function
--------

This API is used to detach an EVS disk from a BMS.

Constraints
-----------

If a BMS is stopped, disks can be detached from it without any limitation on the OS. If a BMS is in running state, the constraints are as follows:

-  Before detaching an EVS disk from a Linux BMS, log in to the BMS, run the **unmount** command to disassociate the disk to be detached from the file system, and ensure that no program is reading data from or writing data to the disk. Otherwise, the disk will fail to be detached.
-  Before detaching an EVS disk from a running Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

URI
---

DELETE /v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}

:ref:`Table 1 <en-us_topic_0053158611__table88181828105313>` lists the parameters.

.. _en-us_topic_0053158611__table88181828105313:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`.                                          |
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

      DELETE https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments/b53f23bd-ee8f-49ec-9420-d1acfeaf91d6

Response
--------

N/A

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
