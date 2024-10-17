:original_name: en-us_topic_0140740387.html

.. _en-us_topic_0140740387:

Stopping a BMS
==============

Scenarios
---------

You can stop BMSs in **Running** state.

.. note::

   -  Stopping a BMS will forcibly interrupt services running on it. Before performing this operation, ensure that you have saved files on the BMS.
   -  You can stop a BMS only on the management console and cannot run **shutdown** to stop it. It is because that the **shutdown** and other commands attempting to stop a BMS will be regarded as unexpected operations and will not take effect.

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
