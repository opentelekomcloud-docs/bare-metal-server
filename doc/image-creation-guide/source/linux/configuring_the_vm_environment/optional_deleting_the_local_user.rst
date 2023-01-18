:original_name: en-us_topic_0000001194198216.html

.. _en-us_topic_0000001194198216:

(Optional) Deleting the Local User
==================================

Scenario
--------

A local user is created during the VM creation. If you do not need it any longer, delete it.

Procedure
---------

Run the **userdel -rf** *xxx* command.

*xxx* indicates the name of the local user. If no folder of this user exists in the **/home** directory, the user is deleted successfully.

.. note::

   If the local user fails to be deleted, restart the VM, log in to the VM as user **root**, and run the **userdel -rf** *xxx* command again.
