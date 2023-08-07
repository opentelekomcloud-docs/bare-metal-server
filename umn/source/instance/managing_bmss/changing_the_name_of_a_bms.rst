:original_name: en-us_topic_0083737000.html

.. _en-us_topic_0083737000:

Changing the Name of a BMS
==========================

Scenarios
---------

To make it easy for you to identify and manage each BMS, the cloud platform allows you to set BMS names and change the names at any time. The new name of a BMS takes effect after the BMS is restarted.

Constraints
-----------

The names of Windows BMSs cannot be changed.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   The BMS console is displayed.

#. Click the name of the BMS whose name is to be changed.

#. Click |image1| next to **Name**, enter a new name that meets requirements, and click |image2| to save the change.

   The BMS name can contain only letters, digits, hyphens (-), underscores (_), and periods (.).

#. Log in to the BMS OS and run the following command to enable automatic hostname synchronization:

   **sed -i 's/auto_synchronize_hostname.*/auto_synchronize_hostname = True/g' \`find / -name bms-network-config.conf**

   Check that automatic synchronization is enabled.

   **cat \`find / -name bms-network-config.conf**

   |image3|

   .. note::

      If the value of **auto_synchronize_hostname** is **False**, after the BMS is restarted, the hostname will be automatically changed to that set during BMS creation.

#. Log in to the management console again. Locate the row that contains the BMS, click **More** in the **Operation** column, and select **Restart**.

   After about 10 minutes, verify that the BMS is restarted and its hostname is automatically updated.

.. |image1| image:: /_static/images/en-us_image_0259262516.png
.. |image2| image:: /_static/images/en-us_image_0176591271.png
.. |image3| image:: /_static/images/en-us_image_0000001562180958.png
