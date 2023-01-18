:original_name: en-us_topic_0104580828.html

.. _en-us_topic_0104580828:

How Do I Change the SID of a Windows Server 2012 BMS?
=====================================================

Scenarios
---------

A Security Identifier (SID) is a unique value that identifies a user, group, or computer account (administrator account). When an account is created for the first time, a unique SID is assigned to each account on the network. A SID is determined by the computer name, current time, and CPU use time of the current user-mode thread.

A complete SID contains:

-  User and group security description
-  48-bit ID authority
-  Revision level
-  Variable sub-authority values

An example SID is S-1-5-21-287469276-4015456986-3235239863-500.

+----------------------+-------------+--------------------------------------------+------------------------------------+-----------------------------------+
| S                    | 1           | 5                                          | 21-287469276-4015456986-3235239863 | 500                               |
+----------------------+-------------+--------------------------------------------+------------------------------------+-----------------------------------+
| The string is a SID. | SID version | SID authority, which is NT in this example | SID sub-authorities                | Accounts and groups in the domain |
+----------------------+-------------+--------------------------------------------+------------------------------------+-----------------------------------+

Currently, all the Windows Server 2012 BMSs have the same SID. In the cluster deployment scenario, you need to change the SID of the BMSs to ensure that each BMS uses a unique SID.

Procedure
---------

#. Log in to the BMS OS.

#. .. _en-us_topic_0104580828__li7621152616481:

   Click |image1| in the lower left corner, choose **Windows PowerShell**, and run the **whoami /user** command to query the SID.


   .. figure:: /_static/images/en-us_image_0165312996.png
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

#. In the **System Preparation Tool 3.14** dialog box, configure parameters and click **OK**.


   .. figure:: /_static/images/en-us_image_0165324194.png
      :alt: **Figure 3** System Preparation Tool settings

      **Figure 3** System Preparation Tool settings

#. After the configuration is complete, the BMS automatically restarts. You need to encapsulate and decompress the package again. After the BMS restarts, you need to reset the password for the Windows OS. Contact the customer service.

#. Log in to the BMS OS and check the SID using the method in :ref:`2 <en-us_topic_0104580828__li7621152616481>`.


   .. figure:: /_static/images/en-us_image_0165334109.png
      :alt: **Figure 4** Querying the new SID

      **Figure 4** Querying the new SID

   As shown in the preceding figure, the SID has been changed successfully.

.. |image1| image:: /_static/images/en-us_image_0165313006.png
