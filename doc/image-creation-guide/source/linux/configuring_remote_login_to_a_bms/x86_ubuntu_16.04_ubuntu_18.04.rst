:original_name: en-us_topic_0081116812.html

.. _en-us_topic_0081116812:

x86: Ubuntu 16.04/Ubuntu 18.04
==============================

#. Use the vi editor to open the **/etc/default/grub** file and add the following information after the **GRUB_CMDLINE_LINUX** field:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyS0,115200

#. Run the following commands to update the configuration:

   -  Run the **stty -F /dev/ttyS0 speed 115200** command to change the baud speed to **115200**.

      |image1|

   -  Run the **stty -F /dev/ttyS0 -a** command to check whether the baud speed is **115200**.

      |image2|

   -  Run the **grub-mkconfig -o /boot/grub/grub.cfg** command.

      |image3|

#. Use the vi editor to open the **/etc/rc.local** file and add the following content to the file:

   .. code-block::

      systemctl stop getty@ttyS0

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

#. Run the **systemctl is-enabled serial-getty@ttyS0** command to check whether serial-getty@ttyS0 is set to automatically start upon system startup.

   |image4|

.. |image1| image:: /_static/images/en-us_image_0000001423641861.png
.. |image2| image:: /_static/images/en-us_image_0000001372527566.png
.. |image3| image:: /_static/images/en-us_image_0000001423167817.png
.. |image4| image:: /_static/images/en-us_image_0000001422964193.png
