:original_name: en-us_topic_0083737011.html

.. _en-us_topic_0083737011:

Injecting User Data
===================

Application Scenarios
---------------------

You can inject user data to configure BMSs.

-  Use scripts to simplify BMS configuration.
-  Use scripts to initialize BMS OSs.
-  Upload scripts to BMSs at creation time.
-  Use scripts for other purposes.

Constraints
-----------

-  Linux:

   -  The image that is used to create BMSs must have Cloud-Init installed.
   -  The user data to be injected must be less than or equal to 32 KB.
   -  User data uploaded as text can contain only ASCII characters. User data uploaded as a file can contain any characters, and the file size must be less than or equal to 32 KB.
   -  The image that is used to create BMSs must be a public image, a private image created based on a public image, or a private image with Cloud-Init installed.
   -  The script format must comply with user data script specifications for Linux BMSs.
   -  DHCP must be enabled for the VPC, and port 80 must be enabled for the security group in the outbound direction.

-  Windows:

   -  The image that is used to create BMSs must have Cloudbase-Init installed.
   -  The user data to be injected must be less than or equal to 32 KB.
   -  User data uploaded as text can contain only ASCII characters. User data uploaded as a file can contain any characters, and the file size must be less than or equal to 32 KB.
   -  The image that is used to create BMSs must be a public image, a private image created based on a public image, or a private image with Cloudbase-Init installed.
   -  DHCP must be enabled for the VPC, and port 80 must be enabled for the security group in the outbound direction.

Procedure
---------

#. Create a user data script. The format must comply with user data script specifications. For details, see :ref:`Helpful Links <en-us_topic_0083737011__section1753215178819>`.

#. When creating a BMS, set **Advanced Settings** to **Configure now**, and paste the content of the user data script to the **User Data** text box or upload the user data file.


   .. figure:: /_static/images/en-us_image_0158637172.png
      :alt: **Figure 1** Injecting user data

      **Figure 1** Injecting user data

#. The created BMS automatically runs Cloud-Init or Cloudbase-Init to read the user data script upon startup.

User Data Scripts of Linux BMSs
-------------------------------

User data scripts of Linux BMSs are customized by using the open-source Cloud-Init architecture. This architecture uses BMS metadata as the data source for automatically configuring the BMSs. The script types are compatible with open-source Cloud-Init. For details about Cloud-Init, see http://cloudinit.readthedocs.io/en/latest/topics/format.html.

-  Script execution time: A user data script is executed after the time when the status of the target BMS changes to **Running** and before the time when **/etc/init** is executed.

   .. note::

      By default, the scripts are executed as user **root**.

-  Script type: user-data scripts and Cloud-Config data scripts

   .. table:: **Table 1** Linux BMS script types

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | ``-``                 | User-Data Script                                                                                                                                    | Cloud-Config Data                                                                                                         |
      +=======================+=====================================================================================================================================================+===========================================================================================================================+
      | Description           | Scripts, such as Shell and Python scripts, are used for custom configurations.                                                                      | Methods pre-defined in Cloud-Init, such as the Yum source and SSH key, are used for configuring certain BMS applications. |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Format                | A script must be started with **#!**, for example, **#!/bin/bash** and **#!/usr/bin/env python**.                                                   | The first line must be **#cloud-config**, and no space is allowed in front of it.                                         |
      |                       |                                                                                                                                                     |                                                                                                                           |
      |                       | When the BMS is started for the first time, the script will be executed at the rc.local-like level, indicating a low priority in the boot sequence. |                                                                                                                           |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Constraint            | Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.                                                      | Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.                            |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Frequency             | The script is executed only once when the BMS is started for the first time.                                                                        | The execution frequency varies depending on the applications installed on the BMS.                                        |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

-  How can I view the user data injected into a Linux BMS?

   #. Log in to the BMS.

   #. Run the following command to view the user data as user **root**:

      **curl** **http://169.254.169.254/openstack/latest/user_data**

-  Examples

   This section describes how to inject scripts in different formats into Linux BMSs and view script execution results.

   **Example 1: Inject a User-Data script.**

   When creating a BMS, set **User Data** to **As Text** and enter the user data script content.

   .. code-block::

      #!/bin/bash
      echo "Hello, the time is now $(date -R)" | tee /root/output.txt

   After the BMS is created, start it and run the **cat** *[file]* command to check the script execution result.

   .. code-block:: console

      [root@XXXXXXXX ~]# cat /root/output.txt
      Hello, the time is now Mon, 16 Jul 2016 16:03:18+0800

   **Example 2: Inject a Cloud-Config Data script.**

   When creating a BMS, set **User Data** to **As Text** and enter the user data script content.

   .. code-block::

      #cloud-config
      bootcmd:
      - echo 192.168.1.130 us.archive.ubuntu.com >> /etc/hosts

   After the BMS is created, start it and run the **cat** **/etc/hosts** command to check the script execution result.


   .. figure:: /_static/images/en-us_image_0158665921.png
      :alt: **Figure 2** Viewing the execution result

      **Figure 2** Viewing the execution result

User Data Scripts of Windows BMSs
---------------------------------

User data scripts of Windows BMSs are customized by using the open-source Cloudbase-Init architecture. This architecture uses BMS metadata as the data source for initializing and automatically configuring the BMSs. The script types are compatible with open-source Cloudbase-Init. For details about Cloudbase-Init, see https://cloudbase-init.readthedocs.io/en/latest/userdata.html.

-  Script type: batch-processing program scripts and PowerShell scripts

   .. table:: **Table 2** Windows BMS script types

      +------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
      | ``-``      | Batch-Processing Program Script                                                                                                             | PowerShell Script                                                                                                                        |
      +============+=============================================================================================================================================+==========================================================================================================================================+
      | Format     | The script must be started with **rem cmd**, which is the first line of the script. No space is allowed at the beginning of the first line. | The script must be started with **#ps1**, which is the first line of the script. No space is allowed at the beginning of the first line. |
      +------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
      | Constraint | Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.                                              | Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.                                           |
      +------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

-  How can I view the user data injected into a Windows BMS?

   #. Log in to the BMS.

   #. Enter the following URL in the address box of a browser and view the injected user data:

      **http://169.254.169.254/openstack/latest/user_data**

-  Examples

   This section describes how to inject scripts in different formats into Windows BMSs and view script execution results.

   **Example 1: Inject a batch-processing program script.**

   When creating a BMS, set **User Data** to **As Text** and enter the user data script content.

   .. code-block::

      rem cmd
      echo "Hello, BAT Test" > C:\1111.txt

   After the BMS is created, start it and check the script execution result. In this example, a text file named **1111** is added to disk C:\\.


   .. figure:: /_static/images/en-us_image_0158694649.png
      :alt: **Figure 3** Text file 1111.txt

      **Figure 3** Text file 1111.txt

   To view the user data injected into the Windows BMS, log in at http://169.254.169.254/openstack/latest/user_data.


   .. figure:: /_static/images/en-us_image_0158694650.png
      :alt: **Figure 4** Viewing user data in 1111.txt

      **Figure 4** Viewing user data in 1111.txt

   **Example 2: Inject a PowerShell script.**

   When creating a BMS, set **User Data** to **As Text** and enter the user data script content.

   .. code-block::

      #ps1
      echo "Hello, Powershell Test" > C:\aaaa.txt

   After the BMS is created, start it and check the script execution result. In this example, a text file named **aaaa** is added to disk C:\\.


   .. figure:: /_static/images/en-us_image_0158694651.png
      :alt: **Figure 5** Text file aaaa.txt

      **Figure 5** Text file aaaa.txt

   To view the user data injected into the Windows BMS, log in at http://169.254.169.254/openstack/latest/user_data.


   .. figure:: /_static/images/en-us_image_0158694652.jpg
      :alt: **Figure 6** Viewing user data in aaaa.txt

      **Figure 6** Viewing user data in aaaa.txt

Case 1
------

This case illustrates how to inject user data so as to simplify BMS configuration.

In this example, vim is configured to enable syntax highlighting, display line numbers, and set the tab stop to **4**. Configuration file **.vimrc** is created and injected into the **/root/.vimrc** directory during BMS creation. After the BMS is created, vim is automatically configured based on your requirements. This helps to improve BMS configuration efficiency, especially when you are creating ECSs in a batch.

The script is as follows:

.. code-block::

   #cloud-config
   write_files:
     - path: /root/.vimrc
       content: |
         syntax on
         set tabstop=4
         set number

Case 2
------

This case illustrates how to inject user data so as to reset the password for logging in to a Linux BMS.

In this example, the password of user **root** will be reset to ``"******".``

.. note::

   The new password must meet the password complexity requirements listed in :ref:`Table 3 <en-us_topic_0083737011__table17998105810568>`.

.. _en-us_topic_0083737011__table17998105810568:

.. table:: **Table 3** Password requirements

   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Requirements                                                                                                                                     | Example Value         |
   +=======================+==================================================================================================================================================+=======================+
   | Password              | -  Consists of 8 to 26 characters.                                                                                                               | Test12$@              |
   |                       | -  Must contain at least three of the following character types:                                                                                 |                       |
   |                       |                                                                                                                                                  |                       |
   |                       |    -  Uppercase letters                                                                                                                          |                       |
   |                       |    -  Lowercase letters                                                                                                                          |                       |
   |                       |    -  Digits                                                                                                                                     |                       |
   |                       |    -  Special characters ``!@$%^-_=+[]{}:,./?``                                                                                                  |                       |
   |                       |                                                                                                                                                  |                       |
   |                       | -  Cannot contain the username or the username spelled backwards.                                                                                |                       |
   |                       | -  Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows BMSs.) |                       |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

The script is as follows (retain the indentation in the following script):

.. code-block::

   #cloud-config
   chpasswd:
     list: |
       root:******
     expire: False

After the BMS is created, you can use the new password to log in to it. To ensure system security, change the password of user **root** after logging in to the BMS for the first time.

Case 3
------

This case illustrates how to inject user data so as to create a user on a Windows BMS and set a password for the user.

In this example, the user's username is **abc**, its password is **\*****\***, and the user is added to the **administrators** user group.

.. note::

   The new password must meet the password complexity requirements listed in :ref:`Table 4 <en-us_topic_0083737011__table82807424619>`.

.. _en-us_topic_0083737011__table82807424619:

.. table:: **Table 4** Password requirements

   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Requirements                                                                                                                                     | Example Value         |
   +=======================+==================================================================================================================================================+=======================+
   | Password              | -  Consists of 8 to 26 characters.                                                                                                               | Test12$@              |
   |                       | -  Must contain at least three of the following character types:                                                                                 |                       |
   |                       |                                                                                                                                                  |                       |
   |                       |    -  Uppercase letters                                                                                                                          |                       |
   |                       |    -  Lowercase letters                                                                                                                          |                       |
   |                       |    -  Digits                                                                                                                                     |                       |
   |                       |    -  Special characters ``!@$%^-_=+[]{}:,./?``                                                                                                  |                       |
   |                       |                                                                                                                                                  |                       |
   |                       | -  Cannot contain the username or the username spelled backwards.                                                                                |                       |
   |                       | -  Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows BMSs.) |                       |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

The script is as follows:

.. code-block::

   rem cmd
   net user abc ****** /add
   net localgroup administrators abc /add

After the BMS is created, you can use its username and password to log in to it.

Case 4
------

This case illustrates how to inject user data so as to update system software packages for a Linux BMS and enable the HTTPd service. After the user data is injected, you can use the HTTPd service.

The script is as follows:

.. code-block::

   #!/bin/bash
   yum update -y
   service httpd start
   chkconfig httpd on

Case 5
------

This case illustrates how to inject user data so as to assign the user **root** permission for remotely logging in to a Linux BMS. After injecting the file, you can log in to the BMS as user **root** in SSH key authentication mode.

The script is as follows:

.. code-block::

   #cloud-config
   disable_root: false
   runcmd:
   - sed -i 's/^PermitRootLogin.*$/PermitRootLogin without-password/' /etc/ssh/sshd_config
   - sed -i '/^KexAlgorithms.*$/d' /etc/ssh/sshd_config
   - service sshd restart

.. _en-us_topic_0083737011__section1753215178819:

Helpful Links
-------------

For more information about user data injection cases, visit the official Cloud-init/Cloudbase-init website:

-  https://cloudinit.readthedocs.io/en/latest/

-  https://cloudbase-init.readthedocs.io/en/latest/
