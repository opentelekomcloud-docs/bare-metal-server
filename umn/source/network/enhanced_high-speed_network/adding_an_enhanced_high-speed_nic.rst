:original_name: en-us_topic_0160902759.html

.. _en-us_topic_0160902759:

Adding an Enhanced High-Speed NIC
=================================

This section describes how to add an enhanced high-speed NIC to a BMS.

Constraints
-----------

The BMS must be in **Running** state.

Procedure
---------

.. note::

   A BMS has a maximum of two enhanced high-speed NICs and depends on the total bandwidth of the extension NICs. For example, if the total bandwidth allowed for the extension NICs is 2 x 10GE and the bandwidth of the first enhanced high-speed NIC is 2 x 10GE, you cannot add another enhanced high-speed NIC.

   You can view the total bandwidth of extension NICs in the **Extended Configuration** column in **Flavor**.

   -  If a flavor's **Extended Configuration** contains **2*10GE** (for example, the **Extended Configuration** of flavor physical.h2.large is **1*100G IB + 2*10GE**), BMSs of this flavor has only one NIC without extension NIC, and the total bandwidth of extension NICs is 0.
   -  If a flavor's **Extended Configuration** contains **2 x 2*10GE** (for example, the **Extended Configuration** of flavor physical.s3.large is **2 x 2*10GE**), BMSs of this flavor has two NICs, of which one is an extension NIC, and the total bandwidth of extension NICs is 2*10GE.

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the target BMS.

   The page showing details of the BMS is displayed.

#. Click the **NICs** tab. Then, click **Add NIC**.

#. Set the NIC type to enhanced high-speed NIC and select the bandwidth.

#. Click **OK**.

Follow-up Operations
--------------------

The BMS cannot identify the newly added enhanced high-speed NIC. You must manually activate the NIC by following the instructions in sections :ref:`Configuring an Enhanced High-Speed NIC (SUSE Linux Enterprise Server 12) <en-us_topic_0121593247>` to :ref:`Configuring an Enhanced High-Speed NIC (Windows Server) <en-us_topic_0121593252>`.
