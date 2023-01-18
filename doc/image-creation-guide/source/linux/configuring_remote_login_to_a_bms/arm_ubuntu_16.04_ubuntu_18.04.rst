:original_name: en-us_topic_0100489897.html

.. _en-us_topic_0100489897:

Arm: Ubuntu 16.04/Ubuntu 18.04
==============================

#. Use the vi editor to open the **/etc/default/grub** file and modify parameters as follows:

   -  Set **GRUB_CMDLINE_LINUX** to **consoleblank=600 console=tty0 console=ttyAMA0,115200**.
   -  Set **GRUB_TERMINAL** to **serial**.
   -  Set **GRUB_SERIAL_COMMAND** to **serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1**.

   Run the following command:

   **sudo update-grub2**

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

   For x86, check whether **ttyS0** is contained in the file. For ARM64, check whether **ttyAMA0** is contained in the file. If they are not, add them.
