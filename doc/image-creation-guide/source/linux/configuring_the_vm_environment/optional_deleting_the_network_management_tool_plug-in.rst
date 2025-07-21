:original_name: en-us_topic_0000001193878272.html

.. _en-us_topic_0000001193878272:

(Optional) Deleting the Network Management Tool Plug-in
=======================================================

.. note::

   A distributed BMS image uses the NetworkManager provided by the OS, you need to delete the **NetworkManager-config-server** plug-in from the VM. Otherwise, the NIC cannot automatically obtain an IP address. For a centralized BMS, skip this section because it does not use NetworkManager.

Run **rpm -qa \| grep NetworkManager-config-server** to check whether there is such a plug-in.

If yes, run **rpm -e NetworkManager-config-server** to delete it.
