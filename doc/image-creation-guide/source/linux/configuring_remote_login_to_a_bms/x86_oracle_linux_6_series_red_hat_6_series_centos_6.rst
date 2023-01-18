:original_name: en-us_topic_0081116693.html

.. _en-us_topic_0081116693:

x86: Oracle Linux 6 series/Red Hat 6 series/CentOS 6
====================================================

.. note::

   This section uses the configuration files of Red Hat 6.7 as an example. Configuration files of other types of OSs may be different.

#. Use the vi editor to open the **/boot/grub/grub.conf** file, locate **hiddenmenu**, and add the following information after **hiddenmenu**:

   .. code-block::

      serial --unit=0 --speed=115200
      terminal --timeout=5 serial console

   Add the following information to the end of the line that contains **kernel**:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyS0,115200n8

   |image1|

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

.. |image1| image:: /_static/images/en-us_image_0111826727.png
