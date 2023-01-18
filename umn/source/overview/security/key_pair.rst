:original_name: en-us_topic_0140735214.html

.. _en-us_topic_0140735214:

Key Pair
========

What Is a Key Pair?
-------------------

A key pair, or SSH key pair, is an authentication method used when you remotely log in to Linux instances. A key pair is generated using an encryption algorithm. It contains a public key, and a private key reserved for you. The public key is used to encrypt data (for example, a password), and the private key is used to decrypt the data.

The cloud platform stores the public key, and you need to store the private key. Do not share your private key with anyone. Keep your private key secure.

Advantages
----------

The key pair is more secure and convenient than the username/password method.

.. table:: **Table 1** Comparison between the key pair and username/password

   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | Item                  | Key Pair                                                                        | Username and Password                                                               |
   +=======================+=================================================================================+=====================================================================================+
   | Security              | -  More secure than the password and free from brute-force attacks              | Poor security                                                                       |
   |                       | -  The private key cannot be derived from the public key.                       |                                                                                     |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | Convenience           | Simultaneous login to a large number of Linux instances, simplifying management | Login to only one Linux instance at one time, giving no chance of batch maintenance |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Constraints
-----------

-  Only Linux instances support the key pair method.
-  Only RSA key pairs are supported. RSA keys are typically 1024, 2048, or 4096 bits long.
-  A Linux instance can have only one key pair. If a key pair has been bound to your BMS and you bind a new key pair to the BMS, the new key pair will replace the original one.

Generation Method
-----------------

-  Create a key pair on the management console.

   .. note::

      When a key pair is generated, download and properly keep it.

-  Use PuTTYgen to create a key pair and import the key pair into the cloud platform.

Related Operations
------------------

:ref:`Using an SSH Key Pair <en-us_topic_0083737006>`
