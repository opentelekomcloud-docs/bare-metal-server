:original_name: en-us_topic_0000001193878272.html

.. _en-us_topic_0000001193878272:

(Optional) Deleting the Network Management Tool Plug-in
=======================================================

.. note::

   A distributed BMS image uses the NetworkManager provided by the OS, you need to delete the **NetworkManager-config-server** plug-in from the VM. Otherwise, the NIC cannot automatically obtain an IP address. For a centralized BMS, skip this section because it does not use NetworkManager.

Run the **rpm -qa \| grep NetworkManager-config-server** command to query whether the plug-in exists. If yes, run the **rpm -e NetworkManager-config-server** command to delete it.
