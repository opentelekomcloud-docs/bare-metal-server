:original_name: en-us_topic_0100536284.html

.. _en-us_topic_0100536284:

ARM: EulerOS/OpenEuler
======================

#. Use the vi editor to open the **/boot/EFI/grub2/grub.cfg** file, locate the **linux/vmlinuz-xxx.aarch64 root=/** line, and add the following information to the end of the line:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyAMA0,115200

#. To allow user **root** to log in to the BMS using a serial port, check whether the **/etc/securetty** configuration file contains **ttyAMA0**. If not, add it.
