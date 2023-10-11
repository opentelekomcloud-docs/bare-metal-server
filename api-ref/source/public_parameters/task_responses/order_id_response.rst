:original_name: en-us_topic_0131356400.html

.. _en-us_topic_0131356400:

Order ID Response
=================

Normal Response
---------------

.. table:: **Table 1** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | order_id              | String                | Specifies the order ID returned after an order is submitted. You can query the order processing progress based on the ID.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

Abnormal Response
-----------------

.. table:: **Table 2** Abnormal response

   +-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                          | Description                                                                                                                                                |
   +===========+===============================+============================================================================================================================================================+
   | error     | Dictionary data structure [1] | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 3 <en-us_topic_0131356400__table6409189311151>`. |
   +-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0131356400__table6409189311151:

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
          "order_id": "CS2009141523OQSEQ",
          "job_id": "ff808081748b760c01748b7f80370003"
      }

-  Abnormal response

   ::

      {
          "error": {"message": "", "code": XXX}
      }
