:original_name: en-us_topic_0120711878.html

.. _en-us_topic_0120711878:

Setting the Source/Destination Check for a NIC
==============================================

Scenarios
---------

After source/destination check is enabled, the system checks whether source IP addresses contained in the packets sent by BMSs are correct. If the IP addresses are incorrect, the system does not allow the BMSs to send the packets. This mechanism prevents packet spoofing, thereby improving system security.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the target BMS.

   The page showing details of the BMS is displayed.

#. Select the **NICs** tab. Expand the details of the target NIC.

#. Enable or disable **Source/Destination Check**.

   By default, **Source/Destination Check** is enabled. If the BMS functions as a NAT server, router, or firewall, you must disable the source/destination check for the BMS.
