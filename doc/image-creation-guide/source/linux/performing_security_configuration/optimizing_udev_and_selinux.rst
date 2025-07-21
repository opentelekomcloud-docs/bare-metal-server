:original_name: en-us_topic_0000001238962999.html

.. _en-us_topic_0000001238962999:

Optimizing udev and SELinux
===========================

Optimizing udev
---------------

Delete the **/etc/udev/rules.d/70-persistent-net.rules** file.

Optimizing SELinux
------------------

.. note::

   SUSE does not have the SELinux configuration file. Skip this configuration item.

#. Open the **/etc/selinux/config** file.

   **vi /etc/selinux/config**

#. Press **I** to enter editing mode and set the value of **SELINUX** to **disabled**.

   |image1|

#. Press **Esc** and enter **:wq** to save and exit the file.

.. |image1| image:: /_static/images/en-us_image_0000002124205222.png
