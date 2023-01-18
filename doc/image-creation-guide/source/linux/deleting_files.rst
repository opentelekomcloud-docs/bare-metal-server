:original_name: en-us_topic_0081116800.html

.. _en-us_topic_0081116800:

Deleting Files
==============

Deleting Uploaded Files
-----------------------

Delete files uploaded to the VM, such as the .rpm packages of bms-network-config and SDI drivers.

Deleting Temporary Files
------------------------

-  Run the following commands to delete user login records:

   **echo > /var/log/wtmp**

   **echo > /var/log/btmp**

-  Run the following commands to delete temporary files:

   **rm -rf /var/log/cloud-init\***

   **rm -rf /var/lib/cloud/\***

   **rm -rf /var/log/network-config.log**

-  Delete residual configurations.

   -  SUSE: Check for the files whose names start with **ifcfg** in the **/etc/sysconfig/network-scripts/** folder and delete them except **ifcfg-lo** and **ifcfg.template**.

      Command for viewing a file: **ll /etc/sysconfig/network/**

      Command for deleting a file: **rm -rf /etc/sysconfig/network/ifcfg**\ *xxx*

   -  RedHat/CentOS/Oracle/Euler: Check for the files whose names start with **ifcfg** in the **/etc/sysconfig/network-scripts/** folder and delete them except **ifcfg-lo**.

      Command for viewing a file: **ll /etc/sysconfig/network-scripts/**

      Command for deleting a file: **rm -rf /etc/sysconfig/network-scripts/ifcfg**\ *xxx*

   -  Ubuntu OS: Run the **rm -rf /etc/network/interfaces.d/50-cloud-init.cfg** command to delete the file.

-  Run the following command to delete operation records:

   **history -w;echo > /root/.bash_history;history -c;history -c;history -c;**
