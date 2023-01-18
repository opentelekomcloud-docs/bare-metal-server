:original_name: en-us_topic_0245049910.html

.. _en-us_topic_0245049910:

CentOS/EulerOS ARM/OpenEuler ARM
================================

.. note::

   For CentOS and EulerOS ARM, you need to install cloud-init, cloud-utils-growpart, and gdisk. Cloud-Init has been installed in :ref:`Installing Cloud-Init <en-us_topic_0100489884>`.

   This section uses CentOS 7.6 ARM as an example to describe how to install them.

#. Check whether cloud-init and cloud-utils-growpart have been installed. If no, perform the following steps to install them.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep cloud-init
      cloud-init-0.7.5-10.el7.centos.1.x86_64
      [root@localhost ~]# rpm -qa | grep growpart
      [root@localhost ~]#

#. Run the following **yum** command to install cloud-utils-growpart online.

   **yum install cloud-utils-growpart**

#. Check whether gdisk is installed.

   **rpm -qa \| grep gdisk**

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep gdisk
      [root@localhost ~]#

   If no, run the **yum install gdisk** command to install it.

#. Check whether cloud-utils-growpart and gdisk are installed successfully.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep growpart
      cloud-utils-growpart-0.29-2.el7.noarch
      [root@localhost ~]# rpm -qa | grep gdisk
      gdisk-0.8.10-3.el7.x86_64
