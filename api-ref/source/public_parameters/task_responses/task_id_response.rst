:original_name: en-us_topic_0131356399.html

.. _en-us_topic_0131356399:

Task ID Response
================

Normal Response
---------------

.. table:: **Table 1** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | job_id                | String                | Specifies the task ID after a task command is issued. The task ID can be used to query the execution status of the task.                  |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

Abnormal Response
-----------------

.. table:: **Table 2** Abnormal response

   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                      | Description                                                                                                                                                |
   +===========+===========================+============================================================================================================================================================+
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 3 <en-us_topic_0131356399__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131356399__table6409189311151:

.. table:: **Table 3** **error** data structure

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

-  Abnormal response

   ::

      {
          "error": {"message": "", "code": XXX}
      }
