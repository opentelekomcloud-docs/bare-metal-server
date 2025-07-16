:original_name: en-us_topic_0131629817.html

.. _en-us_topic_0131629817:

Deleting the Password of a Windows BMS
======================================

Function
--------

This API is used to delete the random password generated during initial Windows BMS installation. After the password is deleted, you can still use your password to log in to your BMS. However, you cannot use the Get Password function to recover the BMS initial password.

If the BMS is created from a private image, ensure that Cloudbase-Init has been installed. Cloudbase-Init is installed on public images by default.

URI
---

DELETE /v1/{project_id}/baremetalservers/{server_id}/os-server-password

:ref:`Table 1 <en-us_topic_0131629817__table23262209>` lists the parameters.

.. _en-us_topic_0131629817__table23262209:

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

Deleting the password of a BMS (ID: cf2a8b97-b5c6-47ef-9714-eb27adf26e5b)

.. code-block:: text

   DELETE https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/cf2a8b97-b5c6-47ef-9714-eb27adf26e5b/os-server-password

Response
--------

N/A

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
