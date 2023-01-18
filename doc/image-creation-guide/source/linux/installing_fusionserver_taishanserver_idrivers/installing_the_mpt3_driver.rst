:original_name: en-us_topic_0143801232.html

.. _en-us_topic_0143801232:

Installing the mpt3 Driver
==========================

Scenario
--------

If the BMS uses 3108 or 3008 RAID cards, you need to install the mpt3sas driver on the VM.

Procedure
---------

#. Upload the **RAID-3008IR_3008IT_3408IT_3416IT-CentOS7.6-mpt3sas-27.00.00.00-1-x86_64.rpm** package obtained in :ref:`Making Preparations <en-us_topic_0131700230>` to the VM.

#. Install the mpt3 driver.

   a. Go to the directory where the .rpm installation package is stored and run the following command to install it:

      **rpm -ivh** **RAID-3008IR_3008IT_3408IT_3416IT-CentOS7.6-mpt3sas-27.00.00.00-1-x86_64.rpm**

      .. code-block:: console

         [root@localhost mpt3-82599]# rpm -ivh RAID-3008IR_3008IT_3408IT_3416IT-CentOS7.6-mpt3sas-27.00.00.00-1-x86_64.rpm
         Preparing...                               ################################## [100%]
         Updating / installing...
            1:kmod-mpt3sas-27.00.00.00_el7.6-1      ################################## [100%]
         [root@localhost mpt3-82599]#

   b. Run the **dracut -f** command to update the kernel:

#. After the installation is complete, run the **rpm -qa \| grep mpt3** command. The installation is successful if the following information is displayed:

   .. code-block::

      kmod-mpt3sas-27.00.00.00_el7.6-1.x86_64
