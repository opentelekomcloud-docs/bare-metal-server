:original_name: en-us_topic_0191726734.html

.. _en-us_topic_0191726734:

Deleting BMSs
=============

Function
--------

This API is used to delete specified BMSs in a batch or one by one.

Constraints
-----------

-  This API can only be used to delete pay-per-use BMSs.

URI
---

POST /v1/{project_id}/baremetalservers/delete

:ref:`Table 1 <en-us_topic_0191726734__table52652517>` lists the parameters.

.. _en-us_topic_0191726734__table52652517:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                   |
   |                       |                       |                                                                                                             |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter       | Mandatory       | Type             | Description                                                                                                                                                                                           |
+=================+=================+==================+=======================================================================================================================================================================================================+
| servers         | Yes             | Array of objects | Specifies the BMSs to be deleted. For details, see :ref:`Table 2 <en-us_topic_0191726734__table32603030>`.                                                                                            |
+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| delete_publicip | Yes             | Boolean          | Specifies whether to delete the EIP bound to the BMS when the BMS is deleted. If you choose not to delete the EIP, the system only unbinds the EIP from the BMS and reserves the EIP.                 |
|                 |                 |                  |                                                                                                                                                                                                       |
|                 |                 |                  | The value can be **true** or **false**. The default value is **false**.                                                                                                                               |
|                 |                 |                  |                                                                                                                                                                                                       |
|                 |                 |                  | -  **true**: The EIP bound to the BMS is deleted when the BMS is deleted.                                                                                                                             |
|                 |                 |                  | -  **false**: The EIP is unbound from the BMS when the BMS is deleted, but not deleted.                                                                                                               |
+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| delete_volume   | No              | Boolean          | Specifies whether to delete a data disk attached to the BMS when the BMS is deleted. If you choose not to delete the data disk, the system only detaches the disk from the BMS and reserves the disk. |
|                 |                 |                  |                                                                                                                                                                                                       |
|                 |                 |                  | The value can be **true** or **false**. The default value is **false**.                                                                                                                               |
|                 |                 |                  |                                                                                                                                                                                                       |
|                 |                 |                  | -  **true**: The data disk attached to the BMS is deleted when the BMS is deleted.                                                                                                                    |
|                 |                 |                  | -  **false**: The data disk is detached from the BMS when the BMS is deleted, but not deleted.                                                                                                        |
+-----------------+-----------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0191726734__table32603030:

.. table:: **Table 2** **servers** data structure

   ========= ========= ====== ==========================================
   Parameter Mandatory Type   Description
   ========= ========= ====== ==========================================
   id        Yes       String Specifies the ID of the BMS to be deleted.
   ========= ========= ====== ==========================================

Example Request
---------------

Deleting a BMS (ID: 616fb98f-46ca-475e-917e-2563e5a8cd19) without deleting its EIPs and data disks

.. code-block::

   {
       "servers": [
           {
               "id": "616fb98f-46ca-475e-917e-2563e5a8cd19"
           }
       ],
       "delete_publicip": false,
       "delete_volume": false
   }

Response
--------

See :ref:`Task ID Response <en-us_topic_0131356399>`.

Returned Values
---------------

Normal values

============== ============================================
Returned Value Description
============== ============================================
200            The request has been successfully processed.
============== ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
