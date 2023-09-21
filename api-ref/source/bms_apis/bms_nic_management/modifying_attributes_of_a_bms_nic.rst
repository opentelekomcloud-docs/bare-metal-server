:original_name: en-us_topic_0229339179.html

.. _en-us_topic_0229339179:

Modifying Attributes of a BMS NIC
=================================

Function
--------

This API is used to specify whether to delete a NIC when the BMS is deleted or the NIC is detached.

URI
---

PUT /v1/{project_id}/baremetalservers/{server_id}/os-interface/{port_id}

:ref:`Table 1 <en-us_topic_0229339179__table247714319133>` lists the parameters.

.. _en-us_topic_0229339179__table247714319133:

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
   | port_id               | Yes                   | Specifies the BMS NIC ID.                                                                                                              |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +----------------------+-----------+--------+-----------------------------------------------------------------------------------------------------------------------+
   | Parameter            | Mandatory | Type   | Description                                                                                                           |
   +======================+===========+========+=======================================================================================================================+
   | interface_attachment | Yes       | Object | Specifies the attribute to be modified. For details, see :ref:`Table 2 <en-us_topic_0229339179__table0304200101710>`. |
   +----------------------+-----------+--------+-----------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0229339179__table0304200101710:

   .. table:: **Table 2** **interface_attachment** field data structure description

      +-----------------------+-----------+---------+-----------------------------------------------------------------------------------+
      | Parameter             | Mandatory | Type    | Description                                                                       |
      +=======================+===========+=========+===================================================================================+
      | delete_on_termination | Yes       | Boolean | Specifies whether to delete a NIC when the BMS is deleted or the NIC is detached. |
      +-----------------------+-----------+---------+-----------------------------------------------------------------------------------+

-  Example request

   .. code-block::

      {
          "interface_attachment" : {
              "delete_on_termination": false
          }
      }

Response
--------

None

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
