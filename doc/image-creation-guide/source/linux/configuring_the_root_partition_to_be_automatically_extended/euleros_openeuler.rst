:original_name: en-us_topic_0108604186.html

.. _en-us_topic_0108604186:

EulerOS/OpenEuler
=================

.. note::

   For EulerOS, you do not need to install dracut-modules-growroot package. You only need to install cloud-init and cloud-utils-growpart. Cloud-Init has been installed in :ref:`Installing Cloud-Init <en-us_topic_0100489884>`.

#. .. _en-us_topic_0108604186__en-us_topic_0103075368_li10494141311509:

   Check whether cloud-init and cloud-utils-growpart have been installed. If no, perform the following steps to install them.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep cloud-init
      cloud-init-0.7.6-3.x86_64
      [root@localhost ~]# rpm -qa | grep growpart
      [root@localhost ~]#

#. Download the **cloud-utils-growpart-0.27-10.x86_64.rpm** package (from http://repo.huaweicloud.com/euler/2.2/os/x86_64/Packages/), upload the package to the VM, and run the following commands to install it:

   **rpm -ivh** *cloud-utils-growpart-0.27-10.x86_64.rpm*

   .. code-block:: console

      [root@bms-eulor22 home]# rpm -ivh cloud-utils-growpart-0.27-10.x86_64.rpm
      Preparing...                          ############################### [100%]
      Updating / installing...
         1:cloud-utils-growpart-0.27-10     ############################### [100%]

   You can also use an ISO file as the local repo source and run the **yum install cloud-utils-growpart** command to install it.

#. Run the commands in :ref:`1 <en-us_topic_0108604186__en-us_topic_0103075368_li10494141311509>` again to check whether cloud-utils-growpart is successfully installed.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep growpart
      cloud-utils-growpart-0.27-10.x86_64
