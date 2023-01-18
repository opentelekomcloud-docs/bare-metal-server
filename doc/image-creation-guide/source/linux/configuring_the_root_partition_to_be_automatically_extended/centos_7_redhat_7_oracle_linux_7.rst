:original_name: en-us_topic_0108604185.html

.. _en-us_topic_0108604185:

CentOS 7/RedHat 7/Oracle Linux 7
================================

.. note::

   CentOS 7, RedHat 7, and Oracle Linux 7 use the 3.10 (>3.8) kernel. Therefore, you do not need to install dracut-modules-growroot. You only need to install cloud-init and cloud-utils-growpart. Cloud-Init has been installed in :ref:`Installing Cloud-Init <en-us_topic_0100489884>`.

   This section uses CentOS 7.3 as an example to describe how to install them.

#. Check whether cloud-init and cloud-utils-growpart have been installed. If no, perform the following steps to install them.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep cloud-init
      cloud-init-0.7.5-10.el7.centos.1.x86_64
      [root@localhost ~]# rpm -qa | grep growpart
      [root@localhost ~]#

#. Run the following **yum** command to install cloud-utils-growpart online.

   **yum install cloud-utils-growpart**

#. Check whether cloud-utils-growpart is installed successfully.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep growpart
      cloud-utils-growpart-0.29-2.el7.noarch
