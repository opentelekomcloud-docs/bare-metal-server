:original_name: en-us_topic_0081116836.html

.. _en-us_topic_0081116836:

Configuring the SSH Service
===========================

#. After Linux is installed on the host, open the Linux terminal and run the following command to check the SSH service status:

   **service sshd status**

   Check whether the SSH service is enabled and whether its status is **active**.

   -  If the SSH service is not enabled, run the **service enable sshd** command.
   -  If the status is not **active**, run the **service sshd start** command.

#. Modify the SSH service configuration file to enable user **root** to log in to the host using SSH.

   Configuration file path: **/etc/ssh/sshd_config**

   Set the value of **PermitRootLogin** to **yes**.

#. Run the following command to restart the SSH service after the configuration is complete:

   **service sshd restart**
