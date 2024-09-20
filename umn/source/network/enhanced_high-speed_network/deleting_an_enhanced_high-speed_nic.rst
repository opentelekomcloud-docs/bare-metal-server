:original_name: en-us_topic_0160902760.html

.. _en-us_topic_0160902760:

Deleting an Enhanced High-Speed NIC
===================================

Scenarios
---------

You can delete an enhanced high-speed NIC if you do not need it any longer.

Constraints
-----------

The BMS must be in **Running** or **Stopped** state.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the target BMS.

   The page showing details of the BMS is displayed.

#. Click the **NICs** tab, locate the target enhanced high-speed NIC, click |image1| to expand its details, and make a note of the MAC address.

   .. note::

      After deleting a NIC on the console, you need to log in to the BMS OS and perform related operations to delete the device (the MAC address recorded will be used).

#. Click **Delete**.

#. Click **Yes**.

Follow-up Operations
--------------------

Delete network devices by following the "Delete a NIC" part in :ref:`Configuring an Enhanced High-Speed NIC (SUSE Linux Enterprise Server 12) <en-us_topic_0121593247>` to :ref:`Configuring an Enhanced High-Speed NIC (Windows Server) <en-us_topic_0121593252>`.

.. |image1| image:: /_static/images/en-us_image_0167839253.png
