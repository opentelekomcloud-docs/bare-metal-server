:original_name: en-us_topic_0081116587.html

.. _en-us_topic_0081116587:

x86: SUSE 11 SP4
================

#. Use the vi editor to open the **/etc/inittab** file and add the following information to the end of the file:

   .. code-block::

      S0:12345:respawn:/sbin/agetty -L 115200 ttyS0

#. Modify the **/boot/grub/menu.lst** file and add the following information after **gfxmenu (hd0,1)/boot/message**:

   .. code-block::

      serial --unit=0 --speed=115200
      terminal --timeout=5 serial console

   Add the following information to the rows that contain kernel:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyS0,115200n8

   |image1|

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

.. |image1| image:: /_static/images/en-us_image_0111826871.png
