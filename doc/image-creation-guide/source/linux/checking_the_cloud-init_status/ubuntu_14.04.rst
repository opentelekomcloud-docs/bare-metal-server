:original_name: en-us_topic_0082901702.html

.. _en-us_topic_0082901702:

Ubuntu 14.04
============

Run the following commands:

**initctl status cloud-init**

**initctl status cloud-init-local**

**initctl status cloud-config**

**initctl status cloud-final**

If Cloud-Init installation information is displayed, the installation is successful.

.. code-block:: console

   [root@ubuntu:~]# initctl status cloud-init
   cloud-init stop/waiting
   [root@ubuntu:~]# initctl status cloud-init-local
   cloud-init-local stop/waiting
   [root@ubuntu:~]# initctl status cloud-config
   cloud-config stop/waiting
   [root@ubuntu:~]# initctl status cloud-final
   cloud-final stop/waiting
