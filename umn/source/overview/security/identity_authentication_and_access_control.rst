:original_name: en-us_topic_0147508514.html

.. _en-us_topic_0147508514:

Identity Authentication and Access Control
==========================================

Identity and Access Management (IAM) provides functions such as user identity authentication, permission assignment, and access control. You can use IAM to securely control user access to your BMSs. IAM permissions define which actions on your cloud resources are allowed or denied. After creating an IAM user, add it to a user group and grant the permissions required by BMS to the user group. Then, all users in this group will be automatically granted with these permissions.

Account Security
----------------

If you are an enterprise administrator, you can use IAM to create a user and grant permissions to the user. Enterprise employees can use the user account to access the system, and you do not need to share your account password or key pair with them. This helps you manage resources efficiently. You can also configure account security policies to protect these user accounts and reduce security risks for your enterprise information.

Fine-Grained Authorization
--------------------------

You can grant refined permissions to employee accounts to ensure that cloud services are properly used.

Security Group
--------------

A security group is a virtual firewall that detects status and filters data packets. It is an important network isolation method used for access control of ECSs, BMSs, load balancers, and databases.

You can configure security group rules to allow instances in a security group to access the public or private network.

-  A security group is a logical group. You can add BMSs that have the same security protection requirements within a region to the same security group.
-  By default, BMSs in the same security group can communicate with each other through an internal network, whereas BMSs in different security groups cannot.
-  You can modify a security group rule at any time, and the modification takes effect immediately.

Default Security Group
----------------------

When you create a BMS in a region, the system will create a default security group if there is no security group in the region.

The default security group rule allows all outgoing data packets and blocks incoming data packets. BMSs in this security group can access each other already. You do not need to add additional rules.


.. figure:: /_static/images/en-us_image_0000001399664420.png
   :alt: **Figure 1** Default security group

   **Figure 1** Default security group

:ref:`Table 1 <en-us_topic_0147508514__table688715577463>` describes the rules of the default security group.

.. _en-us_topic_0147508514__table688715577463:

.. table:: **Table 1** Rules in the default security group

   +-----------+----------+------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Direction | Protocol | Port/Range | Source/Destination                                           | Description                                                                                                        |
   +===========+==========+============+==============================================================+====================================================================================================================+
   | Outbound  | All      | All        | Destination: 0.0.0.0/0                                       | Allows all outbound traffic.                                                                                       |
   +-----------+----------+------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Inbound   | All      | All        | Source: the current security group (for example, sg-*xxxxx*) | Allows communications among BMSs within the security group and denies all inbound traffic (incoming data packets). |
   +-----------+----------+------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

For more information, see *Virtual Private Cloud User Guide*.

Key Pair Authentication
-----------------------

-  What is a key pair?

A key pair, or SSH key pair, is an authentication method used when you remotely log in to Linux instances. A key pair is generated using an encryption algorithm. It contains a public key, and a private key reserved for you. The public key is used to encrypt data (for example, a password), and the private key is used to decrypt the data.

The cloud platform stores the public key, and you need to store the private key. Do not share your private key with anyone. Keep your private key secure.

-  Advantages

A key pair is more secure and easier to use than username/password in authentication.

.. table:: **Table 2** Comparison between the key pair and username/password

   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | Item                  | Key pair                                                                        | Username and Password                                                               |
   +=======================+=================================================================================+=====================================================================================+
   | Security              | -  More secure than username/password and free from brute-force attacks         | Less secure                                                                         |
   |                       | -  Cannot be derived from the public key                                        |                                                                                     |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | Easy to use           | Simultaneous login to a large number of Linux instances, simplifying management | Login to only one Linux instance at one time, giving no chance of batch maintenance |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

-  Constraints

   -  Only Linux instances support the key pair method.
   -  Only RSA key pairs are supported. RSA keys are typically 1024, 2048, or 4096 bits long.
   -  A Linux instance can have only one key pair. If a key pair has been bound to your BMS and you bind a new key pair to the BMS, the new key pair will replace the original one.

-  Generation

   -  Create a key pair on the management console.

      .. note::

         When a key pair is generated, download and properly keep it.

   -  Use PuTTYgen to create a key pair and import the key pair into the cloud platform.

Helpful Links
-------------

:ref:`Using an SSH Key Pair <en-us_topic_0083737006>`
