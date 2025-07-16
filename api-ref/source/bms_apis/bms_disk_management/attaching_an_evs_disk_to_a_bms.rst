:original_name: en-us_topic_0107658564.html

.. _en-us_topic_0107658564:

Attaching an EVS Disk to a BMS
==============================

Function
--------

This API is used to attach EVS disks to a BMS as data disks after the BMS is created if existing data disks are insufficient or cannot meet requirements.

Constraints
-----------

-  EVS disks cannot be attached to a BMS in a batch.
-  A maximum of 40 EVS disks can be attached to a BMS.
-  A bootable disk cannot be attached to a BMS.
-  A disk cannot be attached to a BMS in the **PAUSED** state, which is specified using the **OS-EXT-STS:vm_state** parameter.
-  Only a shared disk or a disk in the **available** state can be attached to a BMS.
-  Only EVS disks whose device type is **SCSI** can be attached to a BMS.

URI
---

POST /v1/{project_id}/baremetalservers/{server_id}/attachvolume

:ref:`Table 1 <en-us_topic_0107658564__table228013461112>` lists the parameters.

.. _en-us_topic_0107658564__table228013461112:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                               |
   +=======================+=======================+===========================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                 |
   |                       |                       |                                                                                                                           |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`.               |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                     |
   |                       |                       |                                                                                                                           |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the API :ref:`Querying BMSs <en-us_topic_0000002340063012>`. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

+------------------+-----------+--------+----------------------------------------------------------------------------------------------------------------+
| Parameter        | Mandatory | Type   | Description                                                                                                    |
+==================+===========+========+================================================================================================================+
| volumeAttachment | Yes       | Object | Specifies the disks to be attached. For details, see :ref:`Table 2 <en-us_topic_0107658564__table6283335350>`. |
+------------------+-----------+--------+----------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0107658564__table6283335350:

.. table:: **Table 2** **volumeAttachment** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                           |
   +=================+=================+=================+=======================================================================================================================================================================================+
   | volumeId        | Yes             | String          | Specifies the ID of the disk to be attached to a BMS.                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                       |
   |                 |                 |                 | You can obtain the disk ID from the EVS console or by calling the "Querying EVS Disks" API in *Elastic Volume Service API Reference*.                                                 |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | device          | No              | String          | Specifies the mount point, such as **/dev/sda** and **/dev/sdb**.                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                       |
   |                 |                 |                 | The new disk mount point cannot be the same as an existing one.                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                       |
   |                 |                 |                 | The mount point must be specified based on the sequence of existing device names. If this parameter is left blank or set to **""**, the system automatically generates a mount point. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Request
---------------

Attaching an EVS disk (ID: b53f23bd-ee8f-49ec-9420-d1acfeaf91d6) to a BMS (ID: cf2a8b97-b5c6-47ef-9714-eb27adf26e5b)

.. code-block:: text

   POST https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/cf2a8b97-b5c6-47ef-9714-eb27adf26e5b/attachvolume

::

   {
       "volumeAttachment": {
           "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
           "device": ""
       }
   }

Response Parameters
-------------------

.. table:: **Table 3** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 4** Abnormal response

   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                      | Description                                                                                                                                                |
   +===========+===========================+============================================================================================================================================================+
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 5 <en-us_topic_0107658564__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0107658564__table6409189311151:

.. table:: **Table 5** **error** data structure

   ========= ====== ============================
   Parameter Type   Description
   ========= ====== ============================
   message   String Specifies the error message.
   code      String Specifies the error code.
   ========= ====== ============================

Example Response
----------------

-  Normal response

   ::

      {
          "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
      }

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
