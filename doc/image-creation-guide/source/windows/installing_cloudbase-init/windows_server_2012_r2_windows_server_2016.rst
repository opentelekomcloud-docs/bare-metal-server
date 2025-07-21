:original_name: en-us_topic_0108488467.html

.. _en-us_topic_0108488467:

Windows Server 2012 R2/Windows Server 2016
==========================================

#. Download the Cloudbase-Init installation package as instructed in :ref:`Software <en-us_topic_0081116771>`.

#. Upload the package to the host and generate an ISO file.

   Upload the installation package to the host.

   .. code-block:: console

      [root@server nl]# ll
      total 4390172
      -rw-r--r--. 1 root root    41070592  Sep 26 07:33 CloudbaseInitSetup_x64.msi
      -rw-r--r--. 1 qemu qemu  4413020160  Sep 26 02:36 cn_windows_server_2012_r2_x64_dvd_2707961.iso

   Run the following command in the directory where the installation package is stored:

   **mkisofs -L -R -J -T -V system-sp2 -o** *software*\ **.iso** **CloudbaseInitSetup_x64.msi**

#. Mount the generated ISO file to the VM and install Cloudbase-Init.

   a. On virt-manager, choose **View** > **Details**.

   b. In the navigation pane on the left, choose **IDE CDROM 1**. In the right pane, click **Disconnect**.

   c. Click **Connect**.

   d. Select the local ISO file and click **Open** in the upper right corner.

      |image1|

   e. Confirm the settings and click **Apply**.

      |image2|

#. Install Cloudbase-Init.

   Double-click the Cloudbase-Init installation package in the CD-ROM drive. The default installation path of Cloudbase-Init is:

   C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init

#. .. _en-us_topic_0108488467__en-us_topic_0103266721_li80183372211:

   Edit the Cloudbase-Init configuration file **cloudbase-init.conf**.

   Use a text editor (such as Notepad) to open the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\conf** file and edit the file as follows:

   a. Create user **Administrator** and add it to a group.

      .. code-block::

         username=Administrator
         groups=Administrators

   b. Configure **hostname** and modify the following parameter (if it does not exist, add it):

      .. code-block::

         netbios_host_name_compatibility=false

   c. Locate and modify **logging_serial_port_settings** as follows:

      .. code-block::

         logging_serial_port_settings=COM1,115200,N,8

   d. Add parameter **metadata_services** and configure the loaded services as follows:

      .. code-block::

         metadata_services=cloudbaseinit.metadata.services.httpservice.HttpService,cloudbaseinit.metadata.services.configdrive.ConfigDriveService

   e. Add parameter **plugins** to configure the plugins that will be loaded. Separate different plugins with commas (,). The information in bold is the keyword of each plugin.

      -  Mandatory plugins:

         .. code-block::

            plugins=cloudbaseinit.plugins.common.localscripts.LocalScriptsPlugin,cloudbaseinit.plugins.common.mtu.MTUPlugin,cloudbaseinit.plugins.windows.createuser.CreateUserPlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPlugin,cloudbaseinit.plugins.common.sshpublickeys.SetUserSSHPublicKeysPlugin,cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin,cloudbaseinit.plugins.windows.licensing.WindowsLicensingPlugin

         Plugin functions:

         -  **LocalScriptsPlugin**: sets the scripts.
         -  **MTUPlugin**: sets the MTU network ports.
         -  **CreateUserPlugin**: creates a user.
         -  **SetUserPasswordPlugin**: sets the password.
         -  **SetUserSSHPublicKeysPlugin**: sets the private key.
         -  **SetHostNamePlugin**: sets the hostname.
         -  **ExtendVolumesPlugin**: expands disk space.
         -  **UserDataPlugin**: injects user data.
         -  **WindowsLicensingPlugin**: activates Windows instances.

      -  Optional plugins:

         .. code-block::

            plugins=cloudbaseinit.plugins.windows.winrmlistener.ConfigWinRMListenerPlugin,cloudbaseinit.plugins.windows.winrmcertificateauth.ConfigWinRMCertificateAuthPlugin

         Plugin functions:

         -  **ConfigWinRMListenerPlugin**: sets listening to remote login.
         -  **ConfigWinRMCertificateAuthPlugin**: sets remote login without the password authentication.

         .. caution::

            The WinRM plug-ins use weak cryptographic algorithms, which may cause security risks. So, you are not advised to load the plug-ins.

.. |image1| image:: /_static/images/en-us_image_0110262607.png
.. |image2| image:: /_static/images/en-us_image_0110262857.png
