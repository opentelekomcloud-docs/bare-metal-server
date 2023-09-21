:original_name: en-us_topic_0053158712.html

.. _en-us_topic_0053158712:

Updating BMS Metadata (Native OpenStack API)
============================================

Function
--------

This API is used to update BMS metadata.

-  If the metadata does not contain the target field, the field is automatically added to the field.
-  If the metadata contains the target field, the field value is automatically updated.

Constraints
-----------

The BMS **OS-EXT-STS:vm_state** attribute (BMS status) must be **active**, **stopped**, or **paused**.

URI
---

POST /v2.1/{project_id}/servers/{server_id}/metadata

:ref:`Table 1 <en-us_topic_0053158712__table560512381338>` lists the parameters.

.. _en-us_topic_0053158712__table560512381338:

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
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`.                |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                                                                                            |
   +===========+===========+========+========================================================================================================================================+
   | metadata  | Yes       | Object | Specifies the user-defined metadata key and value pair. For details, see :ref:`Table 2 <en-us_topic_0053158712__table59792218185333>`. |
   +-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158712__table59792218185333:

   .. table:: **Table 2** **metadata** field data structure description

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

-  Example request

   .. code-block:: text

      POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/metadata

   ::

      {
          "metadata": {
              "key": "value"
          }
          }

Response
--------

-  Response parameters

   +-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                                                            |
   +===========+========+========================================================================================================================================+
   | metadata  | Object | Specifies the user-defined metadata key and value pair. For details, see :ref:`Table 3 <en-us_topic_0053158712__table22722954185333>`. |
   +-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0053158712__table22722954185333:

   .. table:: **Table 3** **metadata** field data structure description

      +---------------------------------------+-----------------------+-----------------------------------------------------------------+
      | Parameter                             | Type                  | Description                                                     |
      +=======================================+=======================+=================================================================+
      | User-defined field key and value pair | String                | Specifies the key and value pair of the metadata.               |
      |                                       |                       |                                                                 |
      |                                       |                       | -  Each key or value contains a maximum of 255 characters.      |
      |                                       |                       |                                                                 |
      |                                       |                       | -  The value does not support the following special characters: |
      |                                       |                       |                                                                 |
      |                                       |                       |    \\"                                                          |
      +---------------------------------------+-----------------------+-----------------------------------------------------------------+

-  Example response

   ::

      {
          "metadata": {
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
