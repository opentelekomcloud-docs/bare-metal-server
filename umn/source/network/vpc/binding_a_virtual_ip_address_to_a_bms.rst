:original_name: en-us_topic_0120711877.html

.. _en-us_topic_0120711877:

Binding a Virtual IP Address to a BMS
=====================================

Scenarios
---------

You can bind a virtual IP address to a BMS for connection redundancy. This section describes how to bind a virtual IP address to a BMS.

What Is a Virtual IP Address?
-----------------------------

Virtual IP addresses, also called floating IP addresses, are used for active and standby switchover of servers to achieve high availability. If the active server is faulty and cannot provide services, the virtual IP address is dynamically switched to the standby server to provide services.

If you want to improve service high availability and avoid single points of failure, you can use BMSs that are deployed to work in the active/standby mode or one active and multiple standby modes. These BMSs use the same virtual IP address.


.. figure:: /_static/images/en-us_image_0176810855.png
   :alt: **Figure 1** Networking diagram of the HA mode

   **Figure 1** Networking diagram of the HA mode

-  Bind two BMSs in the same subnet to the same virtual IP address.
-  Configure Keepalived for the two BMSs to work in the active/standby mode. For details about Keepalived configurations, see the common configuration methods in the industry.

.. note::

   For more information about virtual IP addresses, see *Virtual Private Cloud User Guide*.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the BMS to which a virtual IP address needs to be bound.

   The page showing details of the BMS is displayed.

#. Click the **NICs** tab. Then, click **Manage Virtual IP Address**.

   The page showing details of the particular VPC is displayed.

#. On the **Virtual IP Address** tab, select a desired one or click **Assign Virtual IP Address** for a new one.

#. Click **Bind to Server** in the **Operation** column and select the target BMS and the NIC to bind the virtual IP address to the NIC.
