:original_name: en-us_topic_0100489885.html

.. _en-us_topic_0100489885:

XenServer
=========

#. Before configuring the yum source on the VM, back up files in the **/etc/yum.repos.d** directory. Perform the following operations to back up the default source:

   a. Open the directory and run the **cd /etc/yum.repos.d** command.

   b. Run the **ll -h** command to check the repo files in the directory.

      If no repo file exists, no further action is required.

   c. Run the **mv /etc/yum.repos.d/**\ *xxx.repo* **/etc/yum.repos.d/**\ *xxx.repo.backup* command to back up all repo files.

      *xxx* is a file name.

#. Run the following command to copy the yum source to the **/etc/yum.repos.d** directory:

   **wget -O /etc/yum.repos.d/CentOS7.repo** *Image source address*

   Alternatively, run the following command:

   **curl -o /etc/yum.repos.d/CentOS7.repo** *Image source address*

#. Run **yum repolist** command to update the yum repository.

   The access may fail (for example, "404 Not Found" is displayed).

   If this problem occurs, use the vi or vim editor to change the value of **$releasever** following **baseurl** to **7** in the **/etc/yum.repos.d/CentOS7.repo** file .

   Run the **yum repolist** command again to update the yum repository.

#. Run the following command to install Cloud-Init:

   **yum install cloud-init**

#. Run the following command to check the Cloud-Init version:

   **cloud-init -v**

   If the Cloud-Init version is displayed, the installation is successful.
