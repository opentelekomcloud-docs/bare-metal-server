:original_name: en-us_topic_0108495465.html

.. _en-us_topic_0108495465:

Configuring the SID
===================

.. important::

   This is the last step for VM configuration. Due to the Cloudbase-Init mechanism, after the VM used to create an image is restarted, a random password is generated, and the VM cannot be logged in. Therefore, confirm the VM configuration before performing operations in this section.

A Security Identifier (SID) is a unique value that identifies a user, group, or computer account.

Only Windows Server 2016 requires SID configuration during image creation. For how to configure a SID for Windows Server 2012 R2, see Bare Metal Server User Guide.

#. Log in to the Windows VM.

#. .. _en-us_topic_0108495465__en-us_topic_0103210577_li7701709389:

   Click |image1| in the lower left corner, choose **Windows PowerShell**, and run the **whoami /user** command to check the SID.


   .. figure:: /_static/images/en-us_image_0172481937.png
      :alt: **Figure 1** Querying the original SID

      **Figure 1** Querying the original SID

#. Modify the Cloudbase-Init configuration files.

   a. Open the **cloudbase-init.conf** and **cloudbase-init-unattend.con** files.

      File directory: **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\conf**

   b. Add **first_logon_behaviour=no** to both files.

      .. code-block::

         [DEFAULT]
         username=Administrator
         groups=Administrators
         first_logon_behaviour=no
         netbios_host_name_compatibility=false
         metadata_services=cloudbaseinit.metadata.services.httpser
         inject_user_password=true
         ...

   c. Delete **cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin** from the **cloudbase-init-unattend.conf** configuration file.


      .. figure:: /_static/images/en-us_image_0143437269.png
         :alt: **Figure 2** Modifying the configuration file

         **Figure 2** Modifying the configuration file

#. Open the CLI and run the following command to open the Sysprep window:

   .. code-block::

      C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf>
      C:\Windows\System32\Sysprep\sysprep.exe /unattend:Unattend.xml

#. Configure the parameters shown in the following figure.


   .. figure:: /_static/images/en-us_image_0143437309.png
      :alt: **Figure 3** System Preparation Tool settings

      **Figure 3** System Preparation Tool settings

#. After the configuration is complete, the BMS automatically restarts. You need to encapsulate and decompress the system again. Log in to the VM and query the SID as instructed in :ref:`2 <en-us_topic_0108495465__en-us_topic_0103210577_li7701709389>`.


   .. figure:: /_static/images/en-us_image_0172481974.png
      :alt: **Figure 4** Viewing the new SID

      **Figure 4** Viewing the new SID

   As shown in the preceding figure, the SID has been changed successfully.

.. |image1| image:: /_static/images/en-us_image_0172481934.png
