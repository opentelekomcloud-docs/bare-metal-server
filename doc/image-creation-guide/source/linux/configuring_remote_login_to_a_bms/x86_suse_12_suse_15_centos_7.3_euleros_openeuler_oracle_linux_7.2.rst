:original_name: en-us_topic_0081116787.html

.. _en-us_topic_0081116787:

x86: SUSE 12/SUSE 15/CentOS 7.3/EulerOS/OpenEuler/Oracle Linux 7.2
==================================================================

.. note::

   This section uses the configuration files of SUSE 12 SP1 as an example. Configuration files of other types of OSs may be different.

#. Use the vi editor to open the **/etc/default/grub** file and add the following information after the **GRUB_CMDLINE_LINUX** field:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyS0,115200

#. Run the following commands to update the configuration:

   **stty -F /dev/ttyS0 speed 115200**

   **grub2-mkconfig -o /boot/grub2/grub.cfg**

   **systemctl enable serial-getty@ttyS0**

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.
