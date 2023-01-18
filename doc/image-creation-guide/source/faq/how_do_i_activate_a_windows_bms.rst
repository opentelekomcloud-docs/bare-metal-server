:original_name: en-us_topic_0093469086.html

.. _en-us_topic_0093469086:

How Do I Activate a Windows BMS?
================================

Windows BMSs need to be activated manually.

#. Log in to the BMS.

#. Click **Start**, enter **cmd** in the **Type here to search** box to open the command-line interface (CLI).

#. Run the following command to configure the IP address of the Key Management Service (KMS) server:

   **slmgr -skms 100.125.4.21**

#. Run the following command to restart the BMS:

   **slmgr -ato**

   -  The BMS is activated if a message similar to "Activated the product" is displayed, and no further action is required.
   -  The BMS is not activated if the error 0xC004F074 (with description "The Key Management Server (KMS) is unavailable") occurs. Go to :ref:`5 <en-us_topic_0093469086__en-us_topic_0094568879_li1033861394512>`.

#. .. _en-us_topic_0093469086__en-us_topic_0094568879_li1033861394512:

   Check whether the BMS system time is synchronized with the standard time. If it is not, synchronize it with the standard time.

#. Run the following command to check whether the BMS can connect to the KMS server port:

   **telnet 100.125.4.21 1688**

   If the connection fails, disable the firewall or enable TCP port 1688 on the firewall. Stop security software such as safedog if any.

#. Run the following command to check whether the BMS has been activated:

   **slmgr -ato**
