:original_name: en-us_topic_0130145446.html

.. _en-us_topic_0130145446:

Querying EVS Disks Attached to a BMS
====================================

Function
--------

This API is used to query EVS disks attached to a BMS.

URI
---

GET /v1/{project_id}/baremetalservers/{server_id}/os-volume_attachments

:ref:`Table 1 <en-us_topic_0130145446__table35893824>` lists the parameters.

.. _en-us_topic_0130145446__table35893824:

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

None

Example Request
---------------

Querying EVS disks attached to a BMS (ID: 4d8c3732-a248-40ed-bebc-539a6ffd25c0)

.. code-block:: text

   GET https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/4d8c3732-a248-40ed-bebc-539a6ffd25c0/os-volume_attachments

Response Parameters
-------------------

+-------------------+------------------+------------------------------------------------------------------------------------------------------------+
| Parameter         | Type             | Description                                                                                                |
+===================+==================+============================================================================================================+
| volumeAttachments | Array of objects | Specifies disks attached to a BMS. For details, see :ref:`Table 2 <en-us_topic_0130145446__table7886611>`. |
+-------------------+------------------+------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0130145446__table7886611:

.. table:: **Table 2** **volumeAttachments** data structure

   +-----------+--------+----------------------------------------------------------+
   | Parameter | Type   | Description                                              |
   +===========+========+==========================================================+
   | device    | String | Specifies the mount directory, for example, **dev/sdd**. |
   +-----------+--------+----------------------------------------------------------+
   | id        | String | Specifies the ID of the attached resource.               |
   +-----------+--------+----------------------------------------------------------+
   | serverId  | String | Specifies the ID of the BMS that disks are attached to.  |
   +-----------+--------+----------------------------------------------------------+
   | volumeId  | String | Specifies the ID of the disk attached to the BMS.        |
   +-----------+--------+----------------------------------------------------------+

Example Response
----------------

::

   {
       "volumeAttachments": [
           {
               "device": "/dev/sdd",
               "id": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
               "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
               "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f803"
           },
           {
               "device": "/dev/sdc",
               "id": "a26887c6-c47b-4654-abb5-dfadf7d3f804",
               "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
               "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f804"
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
