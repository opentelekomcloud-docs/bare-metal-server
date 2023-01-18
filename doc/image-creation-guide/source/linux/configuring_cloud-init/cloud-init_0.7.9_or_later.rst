:original_name: en-us_topic_0100489894.html

.. _en-us_topic_0100489894:

Cloud-Init 0.7.9 or later
=========================

#. Add the following key-value pair with an empty line above and below it:

   .. code-block::

      no_ssh_fingerprints: true

#. Set **ssh_pwauth** to **false** or **0**, indicating that password login in SSH mode is disabled.

   .. code-block::

      ssh_pwauth: false

#. Set **disable_root** to **false**. This parameter specifies whether to allow SSH login of user **root**.

   .. code-block::

      disable_root: true

#. Add **preserve_hostname: false**.

   .. code-block::

      preserve_hostname: false

#. (Optional) Use the number sign (#) to comment out the following statements (skip this step if the statements do not exist):

   .. code-block::

      mount_default_fields: [~, ~, 'auto', 'defaults,nofail', '0', '2']
      resize_rootfs_tmp: /dev
      ssh_deletekeys:   0

#. Modify **ssh_genkeytypes** as follows (add it if it does not exist):

   .. code-block::

      ssh_genkeytypes: ['rsa', 'dsa']

#. Modify **syslog_fix_perms** as follows (add it if it does not exist):

   .. code-block::

      syslog_fix_perms: root:root

#. Add the following statements:

   .. code-block::

      network:
         config: disabled
      datasource_list: [ OpenStack ]
      datasource:
        OpenStack:
          metadata_urls: ['http://169.254.169.254']
          max_wait: 120
          timeout: 10
          retries: 5

#. (Optional) In **/etc/cloud/cloud.cfg**, set **apply_network_config** to **False**.

   This step is only for Cloud-Init 18.3 or later.

   |image1|

#. Add the following content after **- final-message** in **cloud_final_modules**:

   .. code-block::

      - power-state-change

#. Modify **system_info** as follows:

   .. code-block::

      system_info:
         distro: rhel
         default_user:
            name: linux  //Username for OS login
            lock_passwd: True   //True indicates that login using a password is disabled. Note that some OSs use value 1 to disable the password login.

   In the preceding command, change the value of **distro** based on the OS, such as **distro: sles**, **distro: rhel**, **distro: ubuntu**, **distro: debian**, and **dustro: fedora**.

#. (Optional) For SUSE 12 SP1 and SUSE 12 SP2, modify **[Unit]** in the **/usr/lib/systemd/system/cloud-init-local.service** file.

   **vi /usr/lib/systemd/system/cloud-init-local.service**

   Ensure that **[Unit]** is configured as follows:

   .. code-block::

      [Unit]
      Description=Initial cloud-init job (pre-networking)
      DefaultDependencies=no
      Wants=network-pre.target
      Wants=local-fs.target
      After=local-fs.target
      Before=network-pre.target
      Before=shutdown.target
      Before=basic.target
      Conflicts=shutdown.target
      # Other distros use Before=sysinit.target. There is not a clearly identified
      # reason for usage of basic.target instead.

#. (Optional) For Ubuntu 16.04, run the following command to configure the OpenStack source:

   **dpkg-reconfigure cloud-init**

   |image2|

   Run the **vim /etc/cloud/cloud.cfg.d/90_dpkg.cfg** command to open the configuration file and check whether the items are correctly configured in the file.

   .. code-block::

      # to update this file, run dpkg-reconfigure cloud-init
      datasource_list: [ OpenStack ]
      ~
      ~
      ~

   If the configuration file content is consistent with the preceding command output, the configuration is successful.

.. |image1| image:: /_static/images/en-us_image_0000001212466429.png
.. |image2| image:: /_static/images/en-us_image_0000001166468632.png
