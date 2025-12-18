:original_name: en-us_topic_0131356393.html

.. _en-us_topic_0131356393:

Stopping BMSs
=============

Function
--------

This API is used to stop BMSs of specified IDs. You can stop a maximum of 1000 BMSs at a time.

.. note::

   This is an asynchronous API. Calling the API successfully indicates that the task is delivered successfully. To check whether the task is successful, use the :ref:`Querying Task Statuses <en-us_topic_0118696596>` API.

URI
---

POST /v1/{project_id}/baremetalservers/action

:ref:`Table 1 <en-us_topic_0131356393__table66418347>` lists the parameters.

.. _en-us_topic_0131356393__table66418347:

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

.. note::

   In the request, the command to stop BMSs must be sent with the parameter **os-stop**. For details, see the example request.

+-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                          |
+===========+===========+========+======================================================================================================================+
| os-stop   | Yes       | Object | Specifies the operation to stop BMSs. For details, see :ref:`Table 2 <en-us_topic_0131356393__table51053190162024>`. |
+-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131356393__table51053190162024:

.. table:: **Table 2** **os-stop** data structure

   +-----------------+-----------------+------------------+---------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                 |
   +=================+=================+==================+=============================================================================================+
   | servers         | Yes             | Array of objects | Specifies BMS IDs. For details, see :ref:`Table 3 <en-us_topic_0131356393__table48932206>`. |
   +-----------------+-----------------+------------------+---------------------------------------------------------------------------------------------+
   | type            | No              | String           | Specifies how BMSs are stopped. The default value is **HARD**.                              |
   |                 |                 |                  |                                                                                             |
   |                 |                 |                  | Value:                                                                                      |
   |                 |                 |                  |                                                                                             |
   |                 |                 |                  | **HARD**: forcible stop                                                                     |
   +-----------------+-----------------+------------------+---------------------------------------------------------------------------------------------+

.. _en-us_topic_0131356393__table48932206:

.. table:: **Table 3** **servers** data structure

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                               |
   +=================+=================+=================+===========================================================================================================================+
   | id              | Yes             | String          | Specifies the BMS ID.                                                                                                     |
   |                 |                 |                 |                                                                                                                           |
   |                 |                 |                 | You can obtain the BMS ID from the BMS console or by calling the API :ref:`Querying BMSs <en-us_topic_0000002340063012>`. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+

Example Request
---------------

Stopping two BMSs (IDs: are 616fb98f-46ca-475e-917e-2563e5a8cd19 and 726fb98f-46ca-475e-917e-2563e5a8cd20)

.. code-block:: text

   POST https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/action

::

   {
       "os-stop": {
           "type": "HARD",
           "servers": [
               {
                   "id": "616fb98f-46ca-475e-917e-2563e5a8cd19"
               },
               {
                   "id": "726fb98f-46ca-475e-917e-2563e5a8cd20"
               }
           ]
       }
   }

Response Parameters
-------------------

-  Normal response

.. table:: **Table 4** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

-  Abnormal response

.. table:: **Table 5** Abnormal response

   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                      | Description                                                                                                                                                |
   +===========+===========================+============================================================================================================================================================+
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 6 <en-us_topic_0131356393__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131356393__table6409189311151:

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
