:original_name: en-us_topic_0100489896.html

.. _en-us_topic_0100489896:

ARM: CentOS 7
=============

#. Use the vi editor to open the **/etc/default/grub** file and add the following information after the **GRUB_CMDLINE_LINUX** field.

   .. code-block::

      consoleblank=600 console=tty0 console=ttyAMA0,115200

#. Run the following commands to update the configuration:

   **stty -F /dev/ttyAMA0 speed 115200**

   **grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg**

   **systemctl enable serial-getty@ttyAMA0**

#. To allow user **root** to log in to the BMS using a serial port, check whether the **/etc/securetty** configuration file contains **ttyAMA0**. If not, add it.
