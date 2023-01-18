:original_name: en-us_topic_0053537013.html

.. _en-us_topic_0053537013:

Managing High-Speed Networks
============================

Scenarios
---------

A high-speed network is an internal network among BMSs and provides high bandwidth for connecting BMSs in the same AZ. If you want to deploy services requiring high throughput and low latency, you can create high-speed networks.

Constraints
-----------

-  When creating a BMS, the network segment used by common NICs cannot overlap with that used by high-speed NICs.
-  The high-speed network does not support security groups, EIPs, DNS, VPNs, and Direct Connect connections.
-  You must select different high-speed networks for different high-speed NICs of a BMS.
-  After a BMS is provisioned, you cannot configure a high-speed network.

Create a High-Speed Network
---------------------------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the **High-Speed Networks** tab and then click **Create High-Speed Network**.

#. Set the name and subnet for the high-speed network and click **OK**.

Change the Name of a High-Speed Network
---------------------------------------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the **High-Speed Networks** tab. Locate the target high-speed network and click **Modify** in the **Operation** column.

#. Change the high-speed network name and click **OK**.

Manage Private IP Addresses
---------------------------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the **High-Speed Networks** tab. Locate the target high-speed network, click **More** in the **Operation** column, and select **Manage Private IP Address** from the drop-down list.

   -  To reserve a private IP address in the high-speed network for binding the IP address to a BMS during BMS creation or for other purposes, perform steps :ref:`4 <en-us_topic_0053537013__li1182125141618>` to :ref:`5 <en-us_topic_0053537013__li1464622114267>`.
   -  To delete a private IP address, perform step :ref:`6 <en-us_topic_0053537013__li20230111011919>`.

#. .. _en-us_topic_0053537013__li1182125141618:

   Click **Assign** **Private IP Address**.

   -  If you select **Automatic Assignment**, the system automatically assigns a private IP address.
   -  If you select **Manual Assignment**, you can specify a specific IP address in the high-speed network segment as the private IP address.

#. .. _en-us_topic_0053537013__li1464622114267:

   Click **OK**.

#. .. _en-us_topic_0053537013__li20230111011919:

   Locate the row that contains the target private IP address, and click **Delete** in the **Operation** column. In the displayed dialog box, click **OK** to delete the IP address.
