:original_name: en-us_topic_0229339177.html

.. _en-us_topic_0229339177:

Attaching NICs to a BMS
=======================

Function
--------

This API is used to attach one or more NICs to a BMS.

URI
---

POST /v1/{project_id}/baremetalservers/{server_id}/nics

:ref:`Table 1 <en-us_topic_0229339177__table193622000312>` lists the parameters.

.. _en-us_topic_0229339177__table193622000312:

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

-  Request parameters

   +-----------------+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                                                    |
   +=================+=================+==================+================================================================================================================================================+
   | nics            | Yes             | Array of objects | Specifies the NICs to be attached. For details, see :ref:`Table 2 <en-us_topic_0229339177__table58396974>`.                                    |
   |                 |                 |                  |                                                                                                                                                |
   |                 |                 |                  | Constraints:                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                |
   |                 |                 |                  | Currently, you can concurrently attach a maximum of 10 NICs to a BMS. If more than 10 NICs are attached concurrently, the attachment may fail. |
   +-----------------+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0229339177__table58396974:

   .. table:: **Table 2** **nics** field data structure description

      +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type             | Description                                                                                                                                                                                         |
      +=================+=================+==================+=====================================================================================================================================================================================================+
      | subnet_id       | Yes             | String           | Specifies the subnet ID of the NIC.                                                                                                                                                                 |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | You can obtain the subnet ID (in UUID format) from the console or by referring to in *Virtual Private Cloud API Reference*.                                                                         |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | Constraints:                                                                                                                                                                                        |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | -  If **subnet_id** is specified, the value of **quota:min_rate** will be used as the minimum NIC bandwidth by default.                                                                             |
      |                 |                 |                  | -  If **subnet_id** is specified, the value of **quota:vif_multiqueue_num** will be used as the number of queues for a NIC by default.                                                              |
      |                 |                 |                  | -  For details about **quota:min_rate** and **quota:vif_multiqueue_num**, see :ref:`Querying Details About extra_specs Parameters of a BMS Flavor (Native OpenStack API) <en-us_topic_0114885743>`. |
      +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | security_groups | No              | Array of objects | Specifies the security groups for the NIC. For details, see :ref:`Table 3 <en-us_topic_0229339177__table16100147>`.                                                                                 |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | Constraints:                                                                                                                                                                                        |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | This parameter is valid only when **subnet_id** is specified. It is mandatory when **subnet_id** is used to attach NICs across tenants.                                                             |
      +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | ip_address      | No              | String           | Specifies the IP address of the NIC. If this parameter is left blank, the IP address is automatically assigned.                                                                                     |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | Constraints:                                                                                                                                                                                        |
      |                 |                 |                  |                                                                                                                                                                                                     |
      |                 |                 |                  | This parameter is valid only if **subnet_id** is specified.                                                                                                                                         |
      +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0229339177__table16100147:

   .. table:: **Table 3** **security_groups** field data structure description

      ========= ========= ====== ================================
      Parameter Mandatory Type   Description
      ========= ========= ====== ================================
      id        Yes       String Specifies the security group ID.
      ========= ========= ====== ================================

-  Example request

   .. code-block::

      {
          "nics": [
              {
                  "subnet_id": "d32019d3-bc6e-4319-9c1d-6722fc136a23",
                  "security_groups": [
                      {
                          "id": "f0ac4394-7e4a-4409-9701-ba8be283dbc3"
                      }
                  ]
              }
          ]
      }

Response
--------

-  Response parameters

.. table:: **Table 4** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 5** Abnormal response

   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                      | Description                                                                                                                                                |
   +===========+===========================+============================================================================================================================================================+
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 6 <en-us_topic_0229339177__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0229339177__table6409189311151:

.. table:: **Table 6** **error** data structure

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

=============== ============================================
Returned Values Description
=============== ============================================
200             The request has been successfully processed.
=============== ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
