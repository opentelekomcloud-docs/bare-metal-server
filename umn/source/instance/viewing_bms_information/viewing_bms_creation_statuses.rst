:original_name: en-us_topic_0053536924.html

.. _en-us_topic_0053536924:

Viewing BMS Creation Statuses
=============================

**Scenarios**
-------------

After clicking **Submit** to request a BMS, you can query the task status in the **Task Status** area. A task involves several sub-tasks, such as creating a BMS resource, binding an EIP, and attaching an EVS disk.

The task status may be either **Creating** or **Failed**:

-  **Processing**: The system is processing the task.
-  **Failed**: The system has failed to process the task. The system rolls back the failed task and displays an error code, for example, **(BMS.3033) Failed to create system disk**.

This section describes how to query BMS application processing status and the information displayed in the **Task Status** area.

**Procedure**
-------------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. **Task Status** is displayed on the right of common operations, such as **Start**, **Stop**, **Restart**, and **Delete**. After you apply for a BMS, the **Task Status** area will show the task processing status.


   .. figure:: /_static/images/en-us_image_0166733479.png
      :alt: **Figure 1** BMS application status

      **Figure 1** BMS application status

#. Click the number displayed in the **Task Status** area to view details about the BMS application processing status. The tasks in **Processing** and **Failed** statuses are displayed.

   .. note::

      If **Failed** is displayed for a task in the **Task Status** area, but the BMS list contains the BMS, handle this issue by following the instructions in :ref:`Why Is the BMS Creation Task Displayed as Failed But the BMS List Shows the BMS? <en-us_topic_0053536915>`
