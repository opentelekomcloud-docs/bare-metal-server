:original_name: en-us_topic_0078758302.html

.. _en-us_topic_0078758302:

Installing and Configuring Agent
================================

Scenarios
---------

This section describes how to install and configure Agent on a BMS.

Prerequisites
-------------

The BMS is running properly.

Constraints
-----------

Private images do not support this function.

:ref:`Table 1 <en-us_topic_0078758302__table67513102711>` lists the Linux images that support server monitoring.

.. _en-us_topic_0078758302__table67513102711:

.. table:: **Table 1** Linux images that support server monitoring

   ============ ================================
   OS Type      Version
   ============ ================================
   Red Hat      6.5, 6.7, 6.8, 7.2, 7.3, and 7.4
   SUSE         11.4 and 12.1
   Oracle Linux 6.5, 7.3, and 7.4
   CentOS       6.9, 7.2, 7.3, and 7.4
   EulerOS      2.2
   ============ ================================

Procedure
---------

#. .. _en-us_topic_0078758302__li172641224134219:

   Perform the following steps to create an agency for server monitoring of the BMS:

   a. On the management console homepage, choose **Service List** > **Management & Deployment** > **Identity and Access Management**.

   b. In the navigation pane on the left, choose **Agency** and then click **Create Agency** in the upper right corner.

      -  **Agency Name**: Enter **bms_monitor_agency**.
      -  **Agency Type**: Select **Cloud service**.
      -  **Cloud Service**: This parameter is available if you select **Cloud service** for **Agency Type**. Click **Select**, select **ECS BMS** in the displayed **Select Cloud Service** dialog box, and click **OK**.
      -  **Validity Period**: Select **Permanent**.
      -  **Description**: This parameter is optional. You can enter **Support BMS server monitoring**.
      -  **Permissions**: Locate the region where the BMS resides and click **Modify** in the **Operation** column. In the displayed dialog box, enter **CES** in the **Available Policies** search box. Then select **CES (CES Administrator)** and click **OK**.

         .. note::

            If the BMS belongs to a sub-project, ensure that the sub-project has the CES Administrator permission.

   c. Click **OK**.

      The operations to create an agency for server monitoring of the BMS are complete.

#. Inject the agency.

   -  To inject an agency into a new BMS, select the agency created in :ref:`1 <en-us_topic_0078758302__li172641224134219>` when you create the BMS.
   -  To inject an agency into an existing BMS, click the BMS name to enter its details page, click **Monitoring**, and select the agency created in :ref:`1 <en-us_topic_0078758302__li172641224134219>`.

#. Install and configure Agent on the BMS. For details, see "Installing and Configuring the Agent on a Linux ECS or BMS" in *Cloud Eye User Guide*.

#. Log in to the management console and choose **Management & Deployment** > **Cloud Eye**. On the **Server Monitoring** page, you can view the monitoring data of the BMS.
