:original_name: en-us_topic_0204212311.html

.. _en-us_topic_0204212311:

How Do BMSs in Different AZs of the Same Region Communicate with Each Other?
============================================================================

If they are in the same VPC, they communicate with each other through an internal network. If they are on the same subnet of a VPC, they communicate with each other through the layer-2 network. If they are on different subnets of a VPC, they communicate with each other through the layer-3 network. An EIP must be bound to the primary NIC of each BMS so that they can communicate with each other.
