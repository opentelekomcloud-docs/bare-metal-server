:original_name: en-us_topic_0078771807.html

.. _en-us_topic_0078771807:

How Can I Restore System Disk Data Using the Snapshot?
======================================================

You can create snapshots of the BMS system disk on the EVS console periodically. To restore the system disk data, mount the target system disk to the **sda** mount point.

#. Power off the BMS.

   a. Log in to the management console.

   b. Under **Computing**, click **Bare Metal Server**.

      The BMS console is displayed.

   c. Locate the target BMS and click **Stop**.

#. Detach the system disk.

   a. Click the BMS after it is powered off.

      The page showing details of the BMS is displayed.

   b. Locate the target system disk and click **Detach**.

      In the displayed dialog box, click **OK**.

#. Attach the system disk.

   a. On the page showing the BMS details, click **Attach Disk**.

      The **Attach Disk** page is displayed.

   b. Select the system disk and mount point **/dev/sda**, and click **Attach Disk**.

      In the displayed dialog box, click **OK**.
