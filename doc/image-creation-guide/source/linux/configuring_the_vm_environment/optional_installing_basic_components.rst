:original_name: en-us_topic_0000001194198214.html

.. _en-us_topic_0000001194198214:

(Optional) Installing Basic Components
======================================

Scenario
--------

This section is only necessary for Debian. For other OSs, skip this section. The basic components include vim, dkms, linux--headers-*xxx*-common, and linux-headers-*xxx*-amd64.

Procedure
---------

#. Install vim.

   a. Configure the apt source.

      Run the **vi /etc/apt/sources.list** command to add the apt sources. The content to be added varies depending on the Debian OS version. The following uses Debian 8.6 as an example.

      .. code-block::

         deb http://mirrors.ustc.edu.cn/debian jessie main contrib non-free
         deb-src http://mirrors.ustc.edu.cn/debian jessie main contrib non-free
         deb http://mirrors.ustc.edu.cn/debian jessie-proposed-updates main contrib non-free
         deb-src http://mirrors.ustc.edu.cn/debian jessie-proposed-updates main contrib non-free
         deb http://mirrors.ustc.edu.cn/debian jessie-updates main contrib non-free
         deb-src http://mirrors.ustc.edu.cn/debian jessie-updates main contrib non-free

      Enter **:wq!** to save the file. Then, run the **apt update** command.

   b. Run the **apt-get install vim** command to install vim.

#. Run the **apt-get install dkms** command to install dkms.

#. Run the **apt-get install** **linux--headers-**\ *xxx*\ **-common** command to install **linux--headers-**\ *xxx*\ **-common**.

   *xxx* indicates the kernel version number. For example, if the kernel version of Debain 8.6 is 3.16.0-4, run the **apt-get install linux--headers-3.16.0-4-common** command.

#. Run the **apt-get install** **linux-headers-**\ *xxx*\ **-amd64** command to install **linux-headers-**\ *xxx*\ **-amd64**.

   *xxx* indicates the kernel version number. For example, if the kernel version of Debain 8.6 is 3.16.0-4, run the **apt-get install** **linux-headers-3.16.0-4-amd64** command.

#. Delete configuration items from the **/etc/network/interfaces** file.

   Run the **vi /etc/network/interfaces** command. If the configuration of eth0 exists, delete the last two lines.

   .. code-block::

      ...
      # The loopback network interface
      auto lo
      iface lo inet loopback

      # The primary network interface
      # The following configuration items need to be deleted:
      allow-hotplug eth0
      iface eth0 inet dhcp

   Enter **:wq!** to save the file.
