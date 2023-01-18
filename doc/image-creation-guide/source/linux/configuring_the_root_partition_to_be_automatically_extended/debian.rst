:original_name: en-us_topic_0123559504.html

.. _en-us_topic_0123559504:

Debian
======

.. note::

   For Debian, you only need to install growroot.

#. Run the **apt-get install cloud-initramfs-growroot** command to install growroot.

#. Run the following command to check whether cloud-initramfs-growroot has been installed:

   **dpkg -l \| grep cloud-initramfs-growroot**

   If information similar to the following is displayed, growroot is installed successfully:

   .. code-block::

      root@bms:/home/bzqd# dpkg -l | grep cloud-initramfs-growroot
      ii cloud-initrramfs-growroot      0.18.debian5     all     automatically resize the root partition on first boot
