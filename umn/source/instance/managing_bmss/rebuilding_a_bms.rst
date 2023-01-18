:original_name: en-us_topic_0095819241.html

.. _en-us_topic_0095819241:

Rebuilding a BMS
================

Scenarios
---------

If a BMS cannot work properly due to hardware or SDI card damage, you can rebuild it. This section describes how to rebuild a BMS.

.. note::

   A BMS cannot be rebuilt automatically. You need to contact the operation administrator to rebuild it.

Notes
-----

-  Currently, only BMSs that are quickly provisioned can be rebuilt.
-  After a BMS is rebuilt, it will start automatically.
-  If the BMS uses an IB NIC, record the IP address of the IB NIC rebuilding the BMS.
-  If the BMS uses a QinQ network, record the IP address of the QinQ network before rebuilding the BMS.

Constraints
-----------

-  A BMS can only be rebuilt in the same POD.
-  A BMS to be rebuilt must use an EVS disk as its system disk.
-  Data on local disks cannot be migrated after a BMS is rebuilt.

Prerequisites
-------------

-  The BMS to be rebuilt must be stopped.
-  The BMS to be rebuilt must have a system disk.

Procedure
---------

#. If your BMS uses a QinQ network, delete configurations of the original QinQ network before rebuilding the BMS. For example, if eth3 and eth5 form port group bond1 for the QinQ network, delete the following configuration files:

   **rm** **/etc/udev/rules.d/80-persistent-net.rules**

   **rm** **/etc/sysconfig/network-scripts/ifcfg-eth3**

   **rm** **/etc/sysconfig/network-scripts/ifcfg-eth5**

   **rm** **/etc/sysconfig/network-scripts/ifcfg-bond1**

#. Contact the operation administrator and apply for rebuilding the BMS.

   -  If your BMS uses the QinQ network, reconfigure the QinQ network based on the original QinQ network configuration and by following the instructions in :ref:`Configuring a User-defined VLAN (SUSE Linux Enterprise Server 12) <en-us_topic_0095251843>` to :ref:`Configuring a User-defined VLAN (Windows Server) <en-us_topic_0095251848>` after the BMS is rebuilt.
   -  If your BMS uses the IB network and the IB NIC IP address assignment mode is DHCP, the IP address of the BMS will change after it is rebuilt. Therefore, if your service heavily depends on the IP address, you need to reconfigure the IP address of the IB network using the static configuration method. The operations describe how to set the IP address of the IB NIC to the original IP address.

      a. Log in to the BMS OS.

      b. Create the **/etc/sysconfig/network-scripts/ifcfg-ib0** configuration file. The following uses CentOS as an example. Set **IPADDR** to the IP address of the BMS before it is rebuilt.

         .. code-block::

            #/etc/sysconfig/network-scripts/ifcfg-ib0
            DEVICE=ib0
            ONBOOT=yes
            BOOTPROTO=none
            IPADDR=172.31.0.254
            NETWORK=172.31.0.0
            BROADCAST=172.31.0.255
            NETMASK=255.255.255.0

      c. Change the value of **enable_ib** in the **/opt/huawei/network_config/bms-network-config.conf** file to **False**.


         .. figure:: /_static/images/en-us_image_0143392043.png
            :alt: **Figure 1** Changing the parameter value

            **Figure 1** Changing the parameter value

      d. Save the configuration and exit. Then restart the NIC.

         **ifdown** **ib0**

         **ifup** **ib0**

      e. Run the following command to check whether the configured IP address takes effect:

         **ifconfig** **ib0**
