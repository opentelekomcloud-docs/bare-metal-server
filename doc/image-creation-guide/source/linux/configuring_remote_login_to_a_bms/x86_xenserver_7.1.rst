:original_name: en-us_topic_0151001260.html

.. _en-us_topic_0151001260:

x86: XenServer 7.1
==================

#. Use the vi editor to open the **/boot/grub/grub.cfg** file and add **console=ttyS0** after the XenServer startup parameter **console=tty0**.

   |image1|

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

.. |image1| image:: /_static/images/en-us_image_0151001152.png
