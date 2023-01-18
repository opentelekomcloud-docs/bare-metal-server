:original_name: en-us_topic_0108486961.html

.. _en-us_topic_0108486961:

Installing the megaraid_sas Driver
==================================

Scenario
--------

If the BMS uses 3408 or 3508 RAID cards, you need to install the megaraid_sas driver on the VM.

Procedure
---------

#. Upload the **RAID-3004iMR_3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-1-x86_64.rpm** package obtained in :ref:`Making Preparations <en-us_topic_0131700230>` to the VM.

#. Install the megaraid_sas driver.

   a. Go to the directory where the .rpm installation package is stored and run the following commands to install it:

      **rpm -ivh RAID-3004iMR_3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-1-x86_64.rpm**

      .. code-block:: console

         [root@localhost 3408]# rpm -ivh RAID-3004iMR_3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-1-x86_64.rpm
         Preparing...                          ###################################### [100%]
         Updating / installing...
            1:kmod-megaraid_sas-07.716.01.00_el###################################### [100%]
         [root@localhost 3408]#

   b. Run the **dracut -f** command to update the kernel:

#. After the installation is complete, run the **rpm -qa \| grep raid** command to check whether the installation is successful.

   .. code-block::

      kmod-megaraid_sas-07.716.01.00-1-x86_64
