:original_name: en-us_topic_0142827127.html

.. _en-us_topic_0142827127:

How Do I Create an Agency for Server Monitoring of the BMS?
===========================================================

#. On the management console, choose **Service List** > **Identity and Access Management**.
#. In the navigation pane on the left, choose **Agencies** and then click **Create Agency** in the upper right corner.

   -  **Agency Name**: Enter **bms_monitor_agency**.
   -  **Agency Type**: Select **Cloud service**.
   -  **Cloud Service**: Select **Elastic Cloud Server (ECS) and Bare Metal Server (BMS)** from the drop-down list.
   -  **Validity Period**: Select **Unlimited**.
   -  **Description**: Enter **Support BMS server monitoring**.

#. Click **Next**. On the **Select Policy/Role** page, search for and select **CES Administrator**.
#. Click **Next**. On the **Select Scope** page, select **All resources** or **Region-specific projects**.

   .. note::

      If the BMS belongs to a sub-project, ensure that the sub-project has the CES Administrator permission.

#. Click **OK**.
