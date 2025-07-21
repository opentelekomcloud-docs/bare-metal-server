:original_name: en-us_topic_0000002340222800.html

.. _en-us_topic_0000002340222800:

Modifying Specified BMS Metadata
================================

Function
--------

This API is used to modify specified BMS metadata.

Constraints
-----------

The BMS **OS-EXT-STS:vm_state** attribute (BMS status) must be **active**, **stopped**, or **paused**.

URI
---

PUT /v2.1/{project_id}/servers/{server_id}/metadata/{key}

:ref:`Table 1 <en-us_topic_0000002340222800__en-us_topic_0053158695_table1370626163519>` lists the parameters.

.. _en-us_topic_0000002340222800__en-us_topic_0053158695_table1370626163519:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the API :ref:`Querying BMSs <en-us_topic_0000002340063012>`.                             |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | key                   | Yes                   | Specifies the BMS metadata key value to be modified.                                                                                                  |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

+-----------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                                                                         |
+===========+===========+========+=====================================================================================================================================================================+
| meta      | Yes       | Object | Specifies the user-defined metadata key and value pair. For details, see :ref:`Table 2 <en-us_topic_0000002340222800__en-us_topic_0053158695_table40778039192629>`. |
+-----------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002340222800__en-us_topic_0053158695_table40778039192629:

.. table:: **Table 2** **meta** data structure

   +---------------------------------------+-----------------+-----------------+-----------------------------------------------------------------+
   | Parameter                             | Mandatory       | Type            | Description                                                     |
   +=======================================+=================+=================+=================================================================+
   | User-defined field key and value pair | Yes             | String          | Specifies the user-defined metadata key and value pair.         |
   |                                       |                 |                 |                                                                 |
   |                                       |                 |                 | -  Each key or value contains a maximum of 255 characters.      |
   |                                       |                 |                 |                                                                 |
   |                                       |                 |                 | -  The key does not support the following special characters:   |
   |                                       |                 |                 |                                                                 |
   |                                       |                 |                 |    :literal:`:`~!@#$%^&*()=+<,>?/'";{[]}|\\`                    |
   |                                       |                 |                 |                                                                 |
   |                                       |                 |                 | -  The value does not support the following special characters: |
   |                                       |                 |                 |                                                                 |
   |                                       |                 |                 |    \\"                                                          |
   +---------------------------------------+-----------------+-----------------+-----------------------------------------------------------------+

Example Request
---------------

Modifying the metadata of a BMS (ID: 95bf2490-5428-432c-ad9b-5e3406f869dd) to customize a key-value pair

.. code-block:: text

   PUT https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/metadata/{key}

::

   {
       "meta": {
           "key": "value"
       }
   }

Response Parameters
-------------------

+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Type   | Description                                                                                                                                                         |
+===========+========+=====================================================================================================================================================================+
| meta      | Object | Specifies the user-defined metadata key and value pair. For details, see :ref:`Table 3 <en-us_topic_0000002340222800__en-us_topic_0053158695_table34604820192629>`. |
+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002340222800__en-us_topic_0053158695_table34604820192629:

.. table:: **Table 3** **meta** data structure

   +---------------------------------------+-----------------------+---------------------------------------------------------+
   | Parameter                             | Type                  | Description                                             |
   +=======================================+=======================+=========================================================+
   | User-defined field key and value pair | String                | Specifies the user-defined metadata key and value pair. |
   |                                       |                       |                                                         |
   |                                       |                       | Each key or value contains a maximum of 255 characters. |
   +---------------------------------------+-----------------------+---------------------------------------------------------+

Example Response
----------------

::

   {
       "meta": {
           "key": "value"
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
