:original_name: en-us_topic_0053536942.html

.. _en-us_topic_0053536942:

Viewing BMS Details
===================

Scenarios
---------

After you obtain a BMS, you can view and manage your BMS on the management console. This section describes how to query detailed information about a BMS, such as the BMS name/ID, disks, NICs, and EIP.

Procedure
---------

#. Log in to the management console.

#. Under **Computing**, click **Bare Metal Server**.

   On the BMS list page, you can view your BMS and its flavor, image, and private IP address.

#. In the upper right corner of the BMS list, query BMSs by specifying the status, name, BMS ID, flavor, and private IP address. Alternatively, click **Search by Tag** above the upper right corner of the BMS list and search for a BMS by tag key and value.

#. Click the name of the queried BMS.

   The page showing details of the BMS is displayed.

#. View the BMS details, such as name, status, flavor, and VPC. You can also click the **Disks**, **NICs**, **Security Groups**, **EIPs**, **Tag**, and **Monitoring** tabs to attach EVS disks to or detach EVS disks from the BMS, change the security group, bind an EIP to or unbind an EIP from the BMS, and create agencies.

   .. note::

      The BMS monitoring data and charts are not displayed on the BMS details page. You need to view them on the Cloud Eye console. The prerequisite is that Agent has been installed on your BMS. For details, see *Cloud Eye User Guide*.
