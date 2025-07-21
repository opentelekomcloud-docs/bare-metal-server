:original_name: en-us_topic_0000001163136429.html

.. _en-us_topic_0000001163136429:

Creating an Execution User
==========================

-  Installation as the **root** user

   A non-root user is required for executing software. Therefore, you need to create such a user before the installation.

   -  If the non-root user is **HwHiAiUser**, the system will specify it as the execution user by default when you install a software package.
   -  If the non-root user is not **HwHiAiUser**, you need to specify an execution user by configuring the **--install-username=**\ *username* **--install-usergroup=**\ *usergroup* parameter when installing a software package.

-  Installation as a non-root user

   The installation user must be the same as the execution user.

   -  If a non-root user already exists, you do not need to create a new one.

      If you want to use a new non-root user, create one and set a password for it by performing the following operations as the **root** user:

      #. Create a non-root user.

         .. code-block::

            groupadd usergroup
            useradd -g usergroup-d /home/username -m username

      #. Set a password for the user.

         .. code-block::

            passwd username

   .. note::

      -  An execution user is specified for a driver only and will also be applied to firmware. You cannot specify an execution user for firmware separately.
      -  *username* indicates the username of the non-root user to be created. Replace it with an actual username, for example, **HwHiAiUser**.
      -  Permission control may cause security risks. You are not advised to add the new user to the **root** user group.
      -  Do not disable login authentication for the **HwHiAiUser** user.

      -  The password validity period is 90 days. You can change the password validity period in the **/etc/login.defs** file or by running the **chage** command. For details, see :ref:`Configuring Password Aging <en-us_topic_0000001163136429__en-us_topic_0000001163051323_section611110132028>`.

.. _en-us_topic_0000001163136429__en-us_topic_0000001163051323_section611110132028:

Configuring Password Expiry
---------------------------

For security purposes, run the **chage** command to set the validity period of a password.

The command is as follows:

**chage** [**-m** *minimum days*] [**-M** *maximum days*] [**-d** *last day*] [**-I** *inactive*] [**-E** *expiration date*] [**-W** *warning days*] *user*

:ref:`Table 1 <en-us_topic_0000001163136429__en-us_topic_0000001163051323_table1810299723>` describes the parameters.

.. _en-us_topic_0000001163136429__en-us_topic_0000001163051323_table1810299723:

.. table:: **Table 1** Password aging

   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                                                                                                                              |
   +===========+==========================================================================================================================================================================================================================+
   | -m        | Minimum number of days between password changes. **0** indicates that you can change your password at any time.                                                                                                          |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -M        | Maximum number of days during which a password is valid. **-1** will remove checking a password's validity and may cause security risks. You are not advised to set this parameter to **-1** unless extremely necessary. |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -d        | Date of the last password change.                                                                                                                                                                                        |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -I        | Number of inactive days after the password expiration before the account is locked.                                                                                                                                      |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -E        | Date when the account will expire.                                                                                                                                                                                       |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -W        | Number of days of warning before a password change is required.                                                                                                                                                          |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | -l        | Lists account expiry information.                                                                                                                                                                                        |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   -  :ref:`Table 1 <en-us_topic_0000001163136429__en-us_topic_0000001163051323_table1810299723>` lists only common **chage** parameters. You can run the **chage --help** command to learn other **chage** parameters.
   -  The date is in the format of *YYYY-MM-DD*. For example, **chage -E 2019-12-01 test** indicates that the **test** user will expire on December 1, 2019.
   -  If *user* is not specified, the settings will be applied to the **root** user by default.

For example, to make the **test** user expire on December 31, 2019, run the following command:

**chage -E 2019-12-31 test**

Installing the Network Script
-----------------------------

See :ref:`Installing bms-network-config <en-us_topic_0081116559>`.
