:original_name: en-us_topic_0083745264.html

.. _en-us_topic_0083745264:

Security Group
==============

What Is a Security Group?
-------------------------

A security group is a virtual firewall that detects status and filters data packets. It is an important network isolation method used to set access control for ECSs, BMSs, load balancers, and database instances.

You can configure security group rules to allow instances in a security group to access the public or private network.

-  A security group is a logical group. You can add BMSs that have the same security protection requirements within a region to the same security group.
-  By default, BMSs in the same security group can communicate with each other through an internal network, whereas BMSs in different security groups cannot.
-  You can modify a security group rule at any time, and the modification takes effect immediately.

Default Security Group
----------------------

When you create a BMS in a region, the system will create a default security group if no security group exists in the region.

The default security group rule allows all outgoing data packets and blocks incoming data packets. BMSs in this security group can access each other already. You do not need to add additional rules.


.. figure:: /_static/images/en-us_image_0287158389.png
   :alt: **Figure 1** Default security group

   **Figure 1** Default security group

:ref:`Table 1 <en-us_topic_0083745264__table57441530644>` lists the rules for a default security group.

.. _en-us_topic_0083745264__table57441530644:

.. table:: **Table 1** Default security group rules

   +-----------+----------+------------+-------------------------------------------------------------+--------------------------------------------------------------+
   | Direction | Protocol | Port Range | Source/Destination                                          | Description                                                  |
   +===========+==========+============+=============================================================+==============================================================+
   | Outbound  | All      | All        | Destination: 0.0.0.0/0                                      | Allows all outbound traffic.                                 |
   +-----------+----------+------------+-------------------------------------------------------------+--------------------------------------------------------------+
   | Inbound   | All      | All        | Source: current security group ID (for example, sg-*xxxxx*) | Allows inbound traffic from BMSs in the same security group. |
   +-----------+----------+------------+-------------------------------------------------------------+--------------------------------------------------------------+
   | Inbound   | TCP      | 22         | Source: 0.0.0.0/0                                           | Allows all IP addresses to access Linux BMSs over SSH.       |
   +-----------+----------+------------+-------------------------------------------------------------+--------------------------------------------------------------+
   | Inbound   | TCP      | 3389       | Source: 0.0.0.0/0                                           | Allows all IP addresses to access Windows BMSs over RDP.     |
   +-----------+----------+------------+-------------------------------------------------------------+--------------------------------------------------------------+

For more information, see *Virtual Private Cloud User Guide*.
