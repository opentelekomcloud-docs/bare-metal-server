:original_name: en-us_topic_0140749073.html

.. _en-us_topic_0140749073:

Obtaining the Password of a Windows BMS
=======================================

Scenarios
---------

Password authentication mode is required to log in to a Windows BMS. Therefore, you must use the key file used when you created the BMS to obtain the administrator password generated when the BMS was initially installed. The administrator user is **Administrator** or the user configured using Cloudbase-Init. This password is randomly generated, offering high security.

Prerequisites
-------------

You have obtained the private key file used during BMS creation.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Locate the row that contains the Windows BMS, click **More** in the **Operation** column, and select **Obtain Password**.

#. Use either of the following methods to obtain the password through the private key:

   -  Click **Select File** and upload the private key from a local directory.
   -  Copy the private key content to the text field.

#. Click **Get Password** to obtain a random password.
