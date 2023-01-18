:original_name: en-us_topic_0100489893.html

.. _en-us_topic_0100489893:

Cloud-Init 0.7.6
================

#. Add the following key-value pair with an empty line above and below it:

   .. code-block::

      no_ssh_fingerprints: true

#. set **users** to **default**.

   .. code-block::

      users:
           - default

#. Modify the following fields:

   .. code-block::

      disable_root: True
      preserve_hostname: false
      syslog_fix_perms: root:root

#. Configure **ssh_pwauth**. This parameter specifies whether to enable password login in SSH mode.

   .. code-block::

      ssh_pwauth: false

#. Use the number sign (#) to comment out the following statements:

   .. code-block::

      mount_default_fields: [~, ~, 'auto', 'defaults', '0', '2']
      manual_cache_clean: true

#. Add **network** statements.

   .. code-block::

      network:
        config: disabled
      datasource_list: [ OpenStack ]

   For SUSE 11 SP4, you also need to add **growpart** statements.

   .. code-block::

      growpart:
        mode: false

   .. important::

      For Debian 8.6, the following line does not need to be added:

      .. code-block::

         datasource_list: [ OpenStack ]

#. Add the following statement after **- final-message** in **cloud_final_modules**:

   .. code-block::

      - power-state-change

#. Check and modify the information in **system info** to make it consistent with the following content:

   .. code-block::

      system_info:
         distro: sles
         default_user:
            name: linux  //Username for OS login
            lock_passwd: True   //True indicates that login using a password is disabled. Note that some OSs use value 1 to disable the password login.
           gecos: redhat
      groups: [adm, audio, cdrom, dialout, dip, floppy, lxd, netdev, plugdev, sudo, video]   // (Optional) Add the user to other groups that have been configured in etc/group.
            sudo: ["ALL=(ALL) NOPASSWD:ALL"]  //Current user has all the root rights.
            shell: /bin/bash   //Execute shell in bash mode.
          paths:
            cloud_dir: /var/lib/cloud/
            templates_dir: /etc/cloud/templates/
          ssh_svcname: sshd

   In the preceding command, change the value of **distro** based on the OS, such as **distro: sles**, **distro: rhel**, **distro: ubuntu**, **distro: debian**, and **dustro: fedora**.

#. Use the number sign (#) to comment out the following statement:

   .. code-block::

      ssh_genkeytypes: ['rsa', 'dsa']

#. (Optional) For Debian 8.6, perform the following operations:

   a. Run the following commands to configure the OpenStack source:

      **dpkg-reconf igure cloud-init**

      |image1|

      Run the **vim /etc/cloud/cloud.cfg.d/90_dpkg.cfg** command to open the configuration file and check whether the items are correctly configured in the file.

      .. code-block::

         # to update this file, run dpkg-reconf igure cloud-init
         datasource_list: [ OpenStack ]
         ~
         ~
         ~

      If the configuration file content is consistent with the preceding command output, the configuration is successful.

#. (Optional) For EulerOS 2.2 and EulerOS 2.3, perform the following operations:

   Check whether the line shown in the following figure has been commented out using the number sign (#) in the **/etc/pam.d/su** configuration file. If the line has been commented out, skip this step.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0125274824.png
.. |image2| image:: /_static/images/en-us_image_0110232075.png
