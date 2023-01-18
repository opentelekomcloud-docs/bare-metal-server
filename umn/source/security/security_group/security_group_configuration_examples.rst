:original_name: en-us_topic_0140749075.html

.. _en-us_topic_0140749075:

Security Group Configuration Examples
=====================================

Case 1: BMSs in Different Security Groups Need to Communicate with Each Other Through an Internal Network
---------------------------------------------------------------------------------------------------------

-  Scenario

   Resources on a BMS in a security group need to be copied to a BMS in another security group. The two BMSs are in the same VPC. Then, you can enable internal network communication between the two BMSs and copy resources.

-  Security group configuration

   In the same VPC, BMSs associated with the same security group can communicate with one another by default, and no additional configuration is required. However, BMSs in different security groups cannot communicate with each other by default. You must add security group rules to enable the BMSs to communicate with each other through an internal network.

   However, BMSs in different security groups cannot communicate with each other by default. You must add security group rules to enable the BMSs to communicate with each other through an internal network.

   +-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------+-------------------------------------------------------------+
   | Protocol                                                                                                              | Direction | Port Range/ICMP Protocol Type           | Source                                                      |
   +=======================================================================================================================+===========+=========================================+=============================================================+
   | Protocol to be used for internal network communication. Supported values are **TCP**, **UDP**, **ICMP**, and **All**. | Inbound   | Port number range or ICMP protocol type | IPv4 address, IPv4 CIDR block, or another security group ID |
   +-----------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------+-------------------------------------------------------------+

Case 2: Only Specified IP Addresses Can Remotely Access BMSs in a Security Group
--------------------------------------------------------------------------------

-  Scenario

   To prevent BMSs from being attacked, you can change the port number for remote login and configure security group rules that allow only specified IP addresses to remotely access the BMSs.

-  Security group configuration

   To allow IP address **192.168.20.2** to remotely access Linux BMSs in a security group over the SSH protocol and port 22, you can configure the following security group rule.

   +-----------------+-----------------+-----------------+-------------------------------------------------------------+
   | Protocol        | Direction       | Port Range      | Source                                                      |
   +=================+=================+=================+=============================================================+
   | SSH (22)        | Inbound         | 22              | IPv4 address, IPv4 CIDR block, or another security group ID |
   |                 |                 |                 |                                                             |
   |                 |                 |                 | For example, 192.168.20.2                                   |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------+

Case 3: Remotely Connecting to a Linux BMS Through SSH
------------------------------------------------------

-  Scenario

   To remotely connect to a Linux BMS through SSH, you need to add a security group rule.

   .. note::

      The default security group comes with this rule. If you use the default security group, you do not need to configure the rule again.

-  Security group configuration

   ======== ========= ========== =========
   Protocol Direction Port Range Source
   ======== ========= ========== =========
   SSH (22) Inbound   22         0.0.0.0/0
   ======== ========= ========== =========

Case 4: Remotely Connecting to a Windows BMS Through RDP
--------------------------------------------------------

-  Scenario

   To remotely connect to a Windows BMS through RDP, you need to add a security group rule.

   .. note::

      The default security group comes with this rule. If you use the default security group, you do not need to configure the rule again.

-  Security group configuration

   ========== ========= ========== =========
   Protocol   Direction Port Range Source
   ========== ========= ========== =========
   RDP (3389) Inbound   3389       0.0.0.0/0
   ========== ========= ========== =========

Case 5: Pinging a BMS from the Internet
---------------------------------------

-  Scenario

   To ping BMSs from each other to check connectivity, you need to add a security group rule.

-  Security group configuration

   ======== ========= ========== =========
   Protocol Direction Port Range Source
   ======== ========= ========== =========
   ICMP     Inbound   All        0.0.0.0/0
   ======== ========= ========== =========
