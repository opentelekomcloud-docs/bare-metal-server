:original_name: en-us_topic_0000001238958153.html

.. _en-us_topic_0000001238958153:

Setting the Maximum Number of Handles to 65535.
===============================================

-  Generally, the default upper limit of handles on a Linux server is 1024. To check it, run the following command:

**[root@platservice6~]# ulimit -n**

1024

-  For a BMS, you need to change the value to **65535**.

Run the **vim** command to edit the **/etc/systemd/system.conf** file as follows:

**DefaultLimitNOFILE=65535**

**DefaultLimitNPROC=65535**

.. note::

   After the preceding operations are complete, you need to restart the VM. Otherwise, the number of handles does not take effect. After the restart, log in to the VM and check the maximum number of handles again.
