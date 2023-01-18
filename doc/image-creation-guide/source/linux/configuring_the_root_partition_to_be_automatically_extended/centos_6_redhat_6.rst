:original_name: en-us_topic_0108604184.html

.. _en-us_topic_0108604184:

CentOS 6/RedHat 6
=================

.. note::

   For CentOS 6 and Red Hat 6, you need to install cloud-init, cloud-utils-growpart, and dracut-modules-growroot. Cloud-Init has been installed in :ref:`Installing Cloud-Init <en-us_topic_0100489884>`.

   This section uses CentOS 6.9 as an example to describe how to install them.

#. .. _en-us_topic_0108604184__en-us_topic_0103075366_li10494141311509:

   Check whether cloud-init, cloud-utils-growpart, and dracut-modules-growroot have been installed. If no, perform the following steps to install them.

   .. code-block:: console

      [root@localhost ~]# rpm -qa | grep cloud-init
      cloud-init-0.7.5-10.el6.centos.2.x86_64
      [root@localhost ~]# rpm -qa | grep growpart
      [root@localhost ~]# rpm -qa | grep growroot
      [root@localhost ~]#

#. Download cloud-utils-growpart-*0.27-10.el6.x86_64*.rpm and upload it to the VM as instructed in :ref:`Upload Required Software Packages <en-us_topic_0000001194038234>`.

   You can download the package from:

   https://dl.fedoraproject.org/pub/epel/

#. Run the following command to install cloud-utils-growpart:

   **rpm -ivh** *cloud-utils-growpart-0.27-10.el6.x86_64.rpm*

   .. code-block:: console

      [root@localhost redhat]# rpm -ivh cloud-utils-growpart-0.27-10.el6.x86_64.rpm
      Preparing...                 ############################### [100%]
         1:cloud-utils-growpart    ############################### [100%]
      [root@localhost redhat]#

#. Install dracut-modules-growroot.

   a. Run the following command:

      **yum install -y https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm**

   b. Run the **yum install dracut-modules-growroot** command to install dracut-modules-growroot online.

      Enter **y** when the message **Is this ok [y/N]** is displayed.

   c. Run the **dracut -f** command to update the kernel.

#. Run the commands in :ref:`1 <en-us_topic_0108604184__en-us_topic_0103075366_li10494141311509>` again to check whether cloud-init, cloud-utils-growpart and dracut-modules-growroot are successfully installed.
