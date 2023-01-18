:original_name: en-us_topic_0000001194358208.html

.. _en-us_topic_0000001194358208:

Configuring the Network
=======================

Scenario
--------

Configure an available IP address for the VM to enable it to communicate with the host.

If the **ifconfig** and **route** are unavailable for SUSE 15, use the **zypper install net-tools-deprecated** to install the tools.

Procedure
---------

#. On the VM, run the following command to query the NIC name:

   **ifconfig -a**

#. Run the following command to check whether the NIC has obtained an IP address:

   **ifconfig**

   If the following information is displayed, the NIC has obtained an IP address (*xxx* indicates the obtained IP address, and *XX* indicates the MAC address):

   .. code-block::

      eth0     Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
      inet addr:xxx.xxx.xxx.xxx  Bcast:xxx.xxx.x.xxx Mask:xxx.xxx.xxx.xxx

#. If the NIC has not obtained an IP address, run the following command to enable the NIC to dynamically obtain an IP address:

   **ifup** *NIC name*

   Example:

   **ifup eth0**

   The following information is displayed:

   .. code-block::

      Determining IP information for eth0... done

   If a message is displayed indicating that the **ifup** command failed, run the following commands:

   **ip link set** *NIC name* **up**

   **dhclient** *NIC name*

   You can also run the following command:

   **ifconfig eth0 up**

   Generally, no information is displayed.
