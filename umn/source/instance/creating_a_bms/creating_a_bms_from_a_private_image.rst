:original_name: en-us_topic_0140737793.html

.. _en-us_topic_0140737793:

Creating a BMS from a Private Image
===================================

Scenarios
---------

If you want to create a BMS that has the same OS and applications as an existing BMS, you can create a private image using the existing BMS and then create a BMS using the private image. This frees you from repeatedly configuring BMSs and improves efficiency.

Background
----------

You can create a private image using either of the following methods:

-  :ref:`Creating a Private Image from a BMS <en-us_topic_0084807532>`
-  :ref:`Creating a Private Image from an External Image File <en-us_topic_0078468105>`

Procedure
---------

Create a BMS by following the instructions in :ref:`Creating a Common BMS <en-us_topic_0053536933>`.

Note for setting the parameters:

-  **Region**: Select the region where the private image is located.
-  **Image**: Select **Private image** or **Shared image** and select the required image from the drop-down list.
-  **Disk**: If the selected flavor supports quick provisioning, you are advised to increase **System Disk** by 2 GB or more.
