:original_name: en-us_topic_0000001194358210.html

.. _en-us_topic_0000001194358210:

(Optional) Modifying DHCP Configuration Items
=============================================

Scenario
--------

This section is only necessary for SUSE. For other OSs, skip it.

Procedure
---------

#. In the VM OS, enter the (CLI) mode and run the **su root** command to switch to user **root**.

#. Run the **vi /etc/sysconfig/network/dhcp** command to open the configuration file.

#. Enter **?DHCLIENT_PRIMARY_DEVICE** to locate the configuration item to be modified.

   Press **i** to enter the editing mode, and set the value of the configuration item to **yes** so that the system obtains the default gateway using DHCP.

   Press **Esc** to exit the editing mode.

   .. note::

      If **DHCLIENT_PRIMARY_DEVICE** does not exist in the configuration file, skip this step.

#. Enter **?DHCLIENT_SET_HOSTNAME** to locate the configuration item to be modified.

   Press **i** to enter the editing mode, and set the value of the configuration item to **no** so that the host name will not be changed when DHCP is used.

   Press **Esc** to exit the editing mode.

#. Enter **?DHCLIENT_USE_LAST_LEASE** to locate the configuration item to be modified.

   Press **i** to enter the editing mode, and set the value of the configuration item to **no** so that the fallback to the last lease is disabled.

   Press **Esc** to exit the editing mode.

#. Enter **?DHCLIENT6_MODE** to locate the configuration item to be modified.

   Press **i** to enter the editing mode and set the value of the configuration item to **managed**.

   Press **Esc** to exit the editing mode.

#. Enter **:wq** to save your settings and exit.
