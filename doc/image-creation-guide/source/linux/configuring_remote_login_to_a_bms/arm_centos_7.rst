:original_name: en-us_topic_0100489896.html

.. _en-us_topic_0100489896:

ARM: CentOS 7
=============

#. Use the vi editor to open the **/boot/efi/EFI/centos** file, locate the line **linux /vmlinuz-**\ *xxx*.\ **aarch64 root=/dev/mapper/cla-root ro crashkernel=auto rd.lvm.lv=cla/root rd.lvm.lv=cla/swap LANG=en_US.UTF-8**, and add the following information to the end of the line:

   .. code-block::

      consoleblank=600 console=tty0 console=ttyAMA0,115200

#. To allow user **root** to log in to the BMS using a serial port, check whether the **/etc/securetty** configuration file contains **ttyAMA0**. If not, add it.
