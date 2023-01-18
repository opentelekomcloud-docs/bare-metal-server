:original_name: en-us_topic_0053536915.html

.. _en-us_topic_0053536915:

Why Is the BMS Creation Task Displayed as Failed But the BMS List Shows the BMS?
================================================================================

Symptom
-------

After you applied for a BMS configured with an EIP on the management console, the BMS application request was successfully processed but the EIP could not be bound to the BMS due to insufficient EIPs. In this case, **Failed** will be displayed for the task in the **Task Status** area. However, the BMS that you applied for will be displayed in the BMS list.

Root Cause
----------

-  The BMS list shows all the BMSs whose application requests have been processed.
-  The **Task Status** area shows the processing status of the BMS creation task, including statuses of sub-tasks, such as preparing BMS resources and binding an EIP. Only when all subtasks have succeeded, the task status changes to **Succeeded**. Otherwise, the task status is displayed as **Failed**.

The BMS is only temporarily displayed in the BMS list. After the system rolls back the failed task, the BMS will be removed from the list.
