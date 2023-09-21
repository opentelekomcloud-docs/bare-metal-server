:original_name: en-us_topic_0107658627.html

.. _en-us_topic_0107658627:

Detaching an EVS Disk from a BMS
================================

Function
--------

This API is used to detach a disk from a BMS.

-  A disk attached to **/dev/sda** functions as the system disk. You can only detach the system disk from a stopped BMS.
-  Disks attached to a mount point other than **/dev/sda** function as data disks and can be detached from a running or stopped BMS.

Constraints
-----------

If a BMS is stopped, disks can be detached from it without any constraints on the OS. If a BMS is running, the constraints are as follows:

-  Before detaching an EVS disk from a Linux BMS, log in to the BMS, run the **unmount** command to disassociate the disk to be detached from the file system, and ensure that no program is reading data from or writing data to the disk. Otherwise, the disk will fail to be detached.
-  Before detaching an EVS disk from a Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

URI
---

DELETE /v1/{project_id}/baremetalservers/{server_id}/detachvolume/{attachment_id}

:ref:`Table 1 <en-us_topic_0107658627__table44563816121>` lists the parameters.

.. _en-us_topic_0107658627__table44563816121:

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
   | attachment_id         | Yes                   | Specifies the IDs of the EVS disks attached to the BMS.                                                                                |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      DELETE https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/cf2a8b97-b5c6-47ef-9714-eb27adf26e5b/detachvolume/6b604cef-9bd8-4f5a-ae56-45839e6e1f0a

Response
--------

See :ref:`Task ID Response <en-us_topic_0131356399>`.

Returned Values
---------------

Normal values

+----------------+---------------------------------------------------------------------+
| Returned Value | Description                                                         |
+================+=====================================================================+
| 202            | The request has been accepted, but the processing has been delayed. |
+----------------+---------------------------------------------------------------------+

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
