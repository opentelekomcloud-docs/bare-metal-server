:original_name: en-us_topic_0100489892.html

.. _en-us_topic_0100489892:

Cloud-Init 0.7.5
================

#. Add the following key-value pair with an empty line above and below it:

   .. code-block::

      no_ssh_fingerprints: true

#. Set **ssh_pwauth**. This parameter specifies whether to enable password login in SSH mode. The value **true** indicates that the password login in SSH mode is enabled, and the value **false** indicates that the function is disabled.

   .. code-block::

      ssh_pwauth: true

#. Set **disable_root** to **false**. This parameter specifies whether to allow SSH login of user **root**.

   .. code-block::

      disable_root: false

#. Add **preserve_hostname: false**.

   .. code-block::

      preserve_hostname: false

#. Use the number sign (#) to comment out the following statements:

   .. code-block::

      mount_default_fields: [~, ~, 'auto', 'defaults,nofail', '0', '2']
      resize_rootfs_tmp: /dev
      ssh_deletekeys:   0

#. Modify **ssh_genkeytypes** as follows:

   .. code-block::

      ssh_genkeytypes: ['rsa', 'dsa']

#. Modify **syslog_fix_perms** as follows:

   .. code-block::

      syslog_fix_perms: root:root

#. Add the following statements:

   .. code-block::

      network:
         config: disabled
      datasource_list: [ OpenStack ]

   .. important::

      For Ubuntu 14.04, the following line does not need to be added:

      .. code-block::

         datasource_list: [ OpenStack ]

#. Add the following statement after **- final-message** in **cloud_final_modules**:

   .. code-block::

      - power-state-change

#. Check and modify the information in **system info** to make it consistent with the following content:

   .. code-block::

      system_info:
         default_user:
           name: root   // User name for OS login
            lock_passwd: False   // True indicates that login using a password is disabled. Note that some OSs use value 1 to disable the password login.
           gecos: redhat
           groups: [audio, cdrom, dialout, floppy]   // (optional) Add the user to other groups that have been configured in etc/group.
            sudo: ["ALL=(ALL) NOPASSWD:ALL"]  //Current user has all the root rights.
            shell: /bin/bash   //Execute shell in bash mode.
         distro: sles
         paths:
            cloud_dir: /var/lib/cloud/
            templates_dir: /etc/cloud/templates/
            upstart_dir: /etc/init/
         ssh_svcname: sshd

   In the preceding command, change the value of **distro** based on the OS, such as **distro: sles**, **distro: rhel**, **distro: ubuntu**, **distro: debian**, and **distro: fedora**.

#. (Optional) For Ubuntu 14.04, perform the following operations:

   a. Use the vi editor to open the **/etc/init/cloud-init-local.conf** configuration file and modify the following configuration items:

      .. code-block::

         # cloud-init - the initial cloud-init job
         #   crawls metadata service, emits cloud-config
         start on mounted MOUNTPOINT=/ and mounted MOUNTPOINT=/run and stopped bms-network_config

   b. Run the following commands to configure the OpenStack source:

      **dpkg-reconfigure cloud-init**

      |image1|

      Run the **vim /etc/cloud/cloud.cfg.d/90_dpkg.cfg** command to open the configuration file and check whether the items are correctly configured in the file.

      .. code-block::

         # to update this file, run dpkg-reconfigure cloud-init
         datasource_list: [ OpenStack ]
         ~
         ~
         ~

      If the configuration file content is consistent with the preceding command output, the configuration is successful.

.. |image1| image:: /_static/images/en-us_image_0110232057.png
