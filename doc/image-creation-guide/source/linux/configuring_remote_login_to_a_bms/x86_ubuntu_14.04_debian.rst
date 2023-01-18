:original_name: en-us_topic_0083023007.html

.. _en-us_topic_0083023007:

x86: Ubuntu 14.04/Debian
========================

#. Use the vi editor to open the **/etc/default/grub** file and add the following information after the **GRUB_CMDLINE_LINUX** field:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyS0,115200

#. Run the following commands to update the configuration:

   **stty -F /dev/ttyS0 speed 115200**

   **grub-mkconfig -o /boot/grub/grub.cfg**

#. Create the **/etc/init/ttyS0.conf** file and use the vi editor to modify the file as follows:

   .. code-block::

      start on stopped rc RUNLEVEL=[12345]
      stop on runlevel [!12345]
      respawn
      exec /sbin/getty -L 115200 ttyS0 vt102

#. Run the following command to start ttyS0:

   **sudo start ttyS0**

#. To allow user **root** to log in to the BMS using a serial port, modify the security configuration file. Add **ttyS0** to the end of the **/etc/securetty** file.
