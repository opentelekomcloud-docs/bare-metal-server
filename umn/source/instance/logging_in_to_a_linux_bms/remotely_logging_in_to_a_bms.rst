:original_name: en-us_topic_0075481007.html

.. _en-us_topic_0075481007:

Remotely Logging In to a BMS
============================

Scenarios
---------

If common remote connection software (such as PuTTY) is unavailable, you can use the remote login function on the management console to log in to a BMS.

Constraints
-----------

-  Only Linux BMSs support remote login.
-  Only the user who creates a BMS or users with the Tenant Administrator or Server Administrator role can log in to the BMS remotely.
-  When you log in to a BMS remotely, shortcut keys such as Ctrl and Alt are not well supported. For example, if you enter **Alt +** *ASCII code*, multiple special characters are displayed.
-  Before exiting the management console, log out of the OS.

Prerequisites
-------------

-  The BMS must be in **Running** state.

-  If you selected the key pair login mode when creating the BMS, log in to the BMS by following the instructions in :ref:`SSH Key Pair <en-us_topic_0053536938>` and set a password for the BMS. The detailed operations are as follows:

   Log in to the BMS using the key pair, switch to user **root**, and run the **passwd** command to set a password for user **root**.


   .. figure:: /_static/images/en-us_image_0149836859.png
      :alt: **Figure 1** Setting a password for user **root**

      **Figure 1** Setting a password for user **root**

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Locate the row that contains the target BMS and click **Remote Login** in the **Operation** column.

   After about one minute, the login page is displayed. Press **Enter** and enter username **root** and password to log in.

   .. note::

      -  If you do not log in within 10 minutes after obtaining the remote login link, it will become invalid.
      -  If you do not perform any operation on the remote login page within 10 minutes, you need to obtain the link again.
      -  If the login page does not respond after you press **Enter**, a possible cause is that remote login is not configured for the BMS image. You can resolve the issue by following the instructions in :ref:`What Do I Do If the Login Page Does Not Respond? <en-us_topic_0075481008>`
      -  If the BMS console is displayed improperly (such as broken lines and garbled characters) after you remotely log in to it, see :ref:`What Do I Do If the BMS Console Is Displayed Improperly After I Remotely Log In to a BMS? <en-us_topic_0078504478>`
      -  If numbers are not properly displayed after you enter them using the numeric keypad for remote login, see :ref:`What Do I Do If the Numeric Keypad Does Not Work During Remote Login? <en-us_topic_0243372663>`
