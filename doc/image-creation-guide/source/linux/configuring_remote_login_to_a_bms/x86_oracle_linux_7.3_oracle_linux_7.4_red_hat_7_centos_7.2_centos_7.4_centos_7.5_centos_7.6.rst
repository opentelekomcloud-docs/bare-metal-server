:original_name: en-us_topic_0081116835.html

.. _en-us_topic_0081116835:

x86: Oracle Linux 7.3/Oracle Linux 7.4/Red Hat 7/CentOS 7.2/CentOS 7.4/CentOS 7.5/CentOS 7.6
============================================================================================

.. note::

   This section uses the configuration files of CentOS 7.2 as an example. Configuration files of other types of OSs may be different.

#. Use the vi editor to open the **/etc/sysconfig/grub** file and add **consoleblank=600 console=tty0 console=ttyS0,115200n8** after the **GRUB_CMDLINE_LINUX** field.

   .. code-block::

      GRUB_TIMEOUT=5
      GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
      GRUB_DEFAULT=saved
      GRUB_DISABLE_SUBMENU=true
      GRUB_TERMINAL_OUTPUT="console"
      GRUB_CMDLINE_LINUX="crashkernel=512M rhgb quiet consoleblank=600 console=tty0 console=ttyS0,115200n8"
      GRUB_DISABLE_RECOVERY="true"
      ~
      ~

#. Run the following commands to update the configuration:

   **stty -F /dev/ttyS0 speed 115200**

   **grub2-mkconfig -o /boot/grub2/grub.cfg**

   **systemctl enable serial-getty@ttyS0**

#. To enable user **root** to log in to the BMS through a serial port, add **ttyS0** to the end of the security configuration file **/etc/securetty**.

   .. code-block::

      vc/1
      ...
      vc/9
      vc/10
      vc/11
      tty1
      ...
      tty9
      tty10
      tty11
      ttyS0
      "securetty" 39L, 221C

   .. note::

      For CentOS 7, if garbled characters are displayed over the serial port, as shown in :ref:`Figure 1 <en-us_topic_0081116835__en-us_topic_0094568703_fig16664175318153>`, perform the following operations:

      .. _en-us_topic_0081116835__en-us_topic_0094568703_fig16664175318153:

      .. figure:: /_static/images/en-us_image_0000001092284762.png
         :alt: **Figure 1** Garbled characters during login

         **Figure 1** Garbled characters during login

      a. Use the vi editor to open the **/etc/default/grub** file and add **115200** to the end of the **GRUB_CMDLINE_LINUX** field.

      |image1|

      b. Run the **systemctl disable getty@ttyS0** and **systemctl stop getty@ttyS0** commands to change the getty@ttyS0 service status as follows.

      |image2|

      c. Run the **stty -F /dev/ttyS0 speed 115200** command to change the baud speed to **115200**.

      |image3|

      d. Run the **grub2-mkconfig -o /boot/grub2/grub.cfg** command again. (The directory of the **grub.cfg** file is an example only.)

      e. Run the following command to check whether the baud speed is **115200**:

      stty -F /dev/ttyS0 -a

      |image4|

.. |image1| image:: /_static/images/en-us_image_0000001092444428.jpg
.. |image2| image:: /_static/images/en-us_image_0000001092604360.jpg
.. |image3| image:: /_static/images/en-us_image_0000001139666565.jpg
.. |image4| image:: /_static/images/en-us_image_0000001139583739.gif
