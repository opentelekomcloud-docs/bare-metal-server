:original_name: en-us_topic_0000001239038183.html

.. _en-us_topic_0000001239038183:

(Optional) Configuring the GRUB Timeout
=======================================

Scenario
--------

For Ubuntu 14.04 or Debian, you need to set the GRUB timeout to prevent system login failures caused by unexpected power-off. For other OSs, skip this section.

Procedure
---------

#. Use the vi editor to open the **/etc/default/grub** file and appendix **GRUB_RECORDFAIL_TIMEOUT=10** to the **GRUB_CMDLINE_LINUX** field.

   .. code-block::

      GRUB_DEFAULT=0
      #GRUB_HIDDEN_TIMEOUT=0
      GRUB_HIDDEN_TIMEOUT_QUIET=true
      GRUB_TIMEOUT=2
      GRUB_DISTRIBUTOR='lsb_release -i -s 2> /dev/null || echo Debian'
      GRUB_CMDLINE_LINUX_DEFAULT=""
      GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0"
      GRUB_RECORDFAIL_TIMEOUT=10

#. Run the following commands to update the configuration:

   **grub-mkconfig -o /boot/grub/grub.cfg**
