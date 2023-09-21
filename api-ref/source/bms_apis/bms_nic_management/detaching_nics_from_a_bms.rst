:original_name: en-us_topic_0229339178.html

.. _en-us_topic_0229339178:

Detaching NICs from a BMS
=========================

Function
--------

This API is used to detach one or more NICs from a BMS.

.. note::

   The primary NIC of a BMS has routing rules configured and cannot be detached.

URI
---

POST /v1/{project_id}/baremetalservers/{server_id}/nics/delete

:ref:`Table 1 <en-us_topic_0229339178__table42885739>` lists the parameters.

.. _en-us_topic_0229339178__table42885739:

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

   +-----------+-----------+------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type             | Description                                                                                                 |
   +===========+===========+==================+=============================================================================================================+
   | nics      | Yes       | Array of objects | Specifies the NICs to be detached. For details, see :ref:`Table 2 <en-us_topic_0229339178__table43212049>`. |
   +-----------+-----------+------------------+-------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0229339178__table43212049:

   .. table:: **Table 2** **nics** field data structure description

      ========= ========= ====== =================================
      Parameter Mandatory Type   Description
      ========= ========= ====== =================================
      id        Yes       String Specifies the port ID of the NIC.
      ========= ========= ====== =================================

-  Example request

   .. code-block::

      {
          "nics": [
              {
                  "id": "d32019d3-bc6e-4319-9c1d-6722fc136a23"
              }
          ]
      }

Response
--------

-  Response parameters

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
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 5 <en-us_topic_0229339178__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0229339178__table6409189311151:

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

=============== ============================================
Returned Values Description
=============== ============================================
200             The request has been successfully processed.
=============== ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
