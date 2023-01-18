:original_name: en-us_topic_0053536889.html

.. _en-us_topic_0053536889:

Adding Security Group Rules
===========================

Scenarios
---------

The default security group rule allows all outgoing data packets. BMSs in a security group can access each other without the need to add access rules. After a security group is created, you can create different access rules for the security group to protect the BMSs that are added to this security group.

.. note::

   You can add only one security group when creating a BMS. After the BMS is created, you can modify the security group of each NIC on the BMS details page.

Suggestions
-----------

-  When adding a security group rule for a BMS, grant the minimum permissions possible:

   -  Enable specific ports rather than a port range, for example, port 80.
   -  Be cautious to authorize source address 0.0.0.0/0 (entire network segment).

-  You are not advised to use one security group to manage all applications because isolation requirements for different layers vary.
-  Configuring a security group for each BMS is unnecessary. Instead, you can add BMSs with the same security protection requirements to the same security group.
-  Simple security group rules are recommended. For example, if you add a BMS to multiple security groups, the BMS may comply with hundreds of security group rules, and a change to any rule may cause network disconnection for the BMS.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. In the BMS list, click the name of the BMS whose security group rules you want to modify.

   The page showing details of the BMS is displayed.

#. Click the **Security Groups** tab and then |image1| to view security group rules.

#. Click the security group ID.

   The system automatically switches to the **Security Group** page.

#. Click **Manage Rule** in the **Operation** column. On the security group details page, add a rule.

   Value **Inbound** indicates that traffic enters the security group, and value **Outbound** indicates that traffic leaves the security group.

   .. table:: **Table 1** Parameter description

      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                        |
      +===================================+====================================================================================================================================+
      | Protocol                          | Network protocol for which the security group rule takes effect. The value can be **All**, **TCP**, **UDP**, **ICMP**, or **GRE**. |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
      | Port                              | Port or port range for which the security group rule takes effect. The value ranges from **1** to **65535**.                       |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
      | Source                            | Traffic source (inbound rule). This parameter is required for an inbound rule.                                                     |
      |                                   |                                                                                                                                    |
      |                                   | The value can be an IP address or a security group.                                                                                |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
      | Destination                       | Traffic destination (outbound rule). This parameter is required for an outbound rule.                                              |
      |                                   |                                                                                                                                    |
      |                                   | The value can be an IP address or a security group.                                                                                |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      The default source IP address **0.0.0.0/0** indicates that all IP addresses can access BMSs in the security group.

.. |image1| image:: /_static/images/en-us_image_0176623771.png
