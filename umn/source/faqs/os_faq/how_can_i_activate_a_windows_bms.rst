:original_name: en-us_topic_0093431546.html

.. _en-us_topic_0093431546:

How Can I Activate a Windows BMS?
=================================

Perform the following operations to manually activate a Windows BMS:

#. Log in to the Windows BMS.

#. Click |image1| in the lower left corner and choose **Windows PowerShell**.

#. Run the following command to configure the IP address of the KMS server:

   **slmgr -skms 100.125.4.21**

#. Run the following command to check whether the BMS has been activated:

   **slmgr -ato**

   If error 0xC004F074 occurs, the BMS cannot be activated. In such an event, go to :ref:`5 <en-us_topic_0093431546__li58311247179>`.

#. .. _en-us_topic_0093431546__li58311247179:

   Verify that the time in the BMS is the same as the standard time. If the time is significantly different, the BMS cannot be activated.

#. Run the following command on the BMS to check whether the link between the BMS and the KMS server port is reachable:

   **telnet 100.125.4.21 1688**

   If the link is unreachable, port 1688 is not enabled on the BMS firewall. You must disable the firewall or enable port 1688 on the firewall. If the BMS has any security software such as safedog, stop using it.

#. Run the following command to check whether the BMS has been activated:

   **slmgr -ato**

.. |image1| image:: /_static/images/en-us_image_0284616151.png
