:original_name: en-us_topic_0131703289.html

.. _en-us_topic_0131703289:

Updating BMS Metadata
=====================

Function
--------

This API is used to update BMS metadata.

-  If the metadata does not contain the target field, the field is automatically added to the field.
-  If the metadata contains the target field, the field value is automatically updated.
-  If the field in the metadata is not requested, the field value remains unchanged.

Constraints
-----------

The BMS must be in active, stopped, or paused state. The state is indicated by the **OS-EXT-STS:vm_state** parameter.

URI
---

POST /v1/{project_id}/baremetalservers/{server_id}/metadata

:ref:`Table 1 <en-us_topic_0131703289__table18618337185333>` lists the parameters.

.. _en-us_topic_0131703289__table18618337185333:

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

Request
-------

.. table:: **Table 2** Request parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================+
   | metadata        | Yes             | Object          | Specifies the user-defined metadata key-value pair.                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | If you do not specify any key-value pair, metadata will not be updated.                                                                                                |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **key**:                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | It contains a maximum of 255 Unicode characters which can be letters, digits, hyphens (-), underscores (_), colons (:), and periods (.). **key** cannot be left blank. |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **value**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | It contains a maximum of 255 Unicode characters.                                                                                                                       |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example request

   .. code-block:: text

      POST https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/cf2a8b97-b5c6-47ef-9714-eb27adf26e5b/metadata

   ::

      {
          "metadata": {
              "key": "value"
          }
      }

Response
--------

.. table:: **Table 3** Parameter description

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================+
   | metadata        | Yes             | Object          | Specifies the user-defined metadata key-value pair.                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | If you do not specify any key-value pair, metadata will not be updated.                                                                                                |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **key**:                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | It contains a maximum of 255 Unicode characters which can be letters, digits, hyphens (-), underscores (_), colons (:), and periods (.). **key** cannot be left blank. |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **value**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | It contains a maximum of 255 Unicode characters.                                                                                                                       |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "metadata":{
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
