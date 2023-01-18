:original_name: en-us_topic_0140740387.html

.. _en-us_topic_0140740387:

Stopping a BMS
==============

Scenarios
---------

You can stop BMSs in **Running** state.

.. note::

   If you choose to forcibly stop a BMS, services running on the BMS will be stopped. Before performing this operation, ensure that you have saved files on the BMS.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Locate the row that contains the target BMS, click **More** in the **Operation** column, and select **Stop** from the drop-down list. To stop multiple BMSs, select them and click **Stop** at the top of the BMS list.

#. In the displayed dialog box, click **Yes**.

After a BMS is stopped, its status becomes **Stopped**.

You can perform the following operations only when the BMS is stopped:

-  :ref:`Detaching the System Disk <en-us_topic_0102427988>`
-  :ref:`Creating an Image <en-us_topic_0084807532>`
-  :ref:`Rebuilding a BMS <en-us_topic_0095819241>`
