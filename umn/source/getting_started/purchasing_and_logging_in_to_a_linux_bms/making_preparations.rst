:original_name: en-us_topic_0083737005.html

.. _en-us_topic_0083737005:

Making Preparations
===================

Create a Key Pair
-----------------

The cloud platform uses public key cryptography to protect the login information of your BMS. You need to specify the key pair name and provide the private key when logging in to the BMS using SSH.

If you do not have a key pair, create one on the management console.

.. note::

   If you want to create BMSs in multiple regions, you need to create a key pair in each region. For more information about regions, see :ref:`Region and AZ <en-us_topic_0083745259>`.

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. In the navigation tree, choose **Key Pair**.

#. On the right side of the page, click **Create Key Pair**.

#. Enter the key name and click **OK**.

   An automatically populated key name consists of **KeyPair-** and a 4-digit random number. Change it to an easy-to-remember one, for example, **KeyPair-**\ *xxxx*\ **\_bms**.

#. Download the private key file. The file name is the specified key pair name with a suffix of .pem. Store the private key file securely. In the displayed dialog box, click **OK**.

   .. caution::

      You can save the private key file only once. When you create a BMS, provide the key pair name. Each time you log in to the BMS using SSH, you need to provide the private key.
