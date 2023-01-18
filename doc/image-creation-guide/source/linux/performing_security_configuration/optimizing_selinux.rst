:original_name: en-us_topic_0000001238962999.html

.. _en-us_topic_0000001238962999:

Optimizing SELinux
==================

.. note::

   SUSE does not have the SELinux configuration file. Skip this configuration item.

#. Open the **/etc/selinux/config** file.

   **vi /etc/selinux/config**

#. Press **I** to enter editing mode and set the value of **SELINUX** to **disabled**.

   |image1|

#. Press **Esc** and enter **:wq** to save and exit the file.

.. |image1| image:: /_static/images/en-us_image_0285808921.png
