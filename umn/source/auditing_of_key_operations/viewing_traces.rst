:original_name: en-us_topic_0110303863.html

.. _en-us_topic_0110303863:

Viewing Traces
==============

Scenarios
---------

Once CTS is enabled, it starts recording BMS operations. You can view operations recorded in the last seven days on the CTS management console.

This section describes how to view the records.

Procedure
---------

#. Log in to the management console.

#. Click **Service List**. Under **Management & Governance**, select **Cloud Trace Service**.

#. In the navigation pane on the left, choose **Trace List**.

#. Set the filter criteria and click **Query**.

   The following filters are available:

   -  **Trace Type**, **Trace Source**, **Resource Type**, and **Search By**.

      Select **Management** for **Trace Type** and **BMS** for **Trace Source**.

      Note that:

      -  If you select **Resource ID** for **Search By**, you need to enter a resource ID. Only whole word match is supported.
      -  If you select **Resource name** for **Search By**, you need to select or enter a specific resource name.

   -  **Operator**: Select a specific operator from the drop-down list.

   -  **Trace Status**: Available values are **All trace statuses**, **Normal**, **Warning**, and **Incident**.

   -  Time range: You can select **Last 1 hour**, **Last 1 day**, **Last 1 week**, or **Customize**.

#. Locate the target trace and click |image1| to expand the trace details.


   .. figure:: /_static/images/en-us_image_0285431353.png
      :alt: **Figure 1** Expanding a trace

      **Figure 1** Expanding a trace

#. Click **View Trace** in the upper right corner of the trace details area.


   .. figure:: /_static/images/en-us_image_0285431358.png
      :alt: **Figure 2** Viewing a trace

      **Figure 2** Viewing a trace

   For details about the key fields in the CTS trace structure, see *Cloud Trace Service User Guide*.

.. |image1| image:: /_static/images/en-us_image_0285431352.png
