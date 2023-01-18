:original_name: en-us_topic_0086739692.html

.. _en-us_topic_0086739692:

(Optional) Configuring Automatic Windows Update
===============================================

You can manually configure Windows Server so that you will be reminded about important Windows updates.

Windows Server 2012 R2 and Windows Server 2016
----------------------------------------------

#. Log in to the Windows VM.
#. Click |image1| in the lower left corner to start Server Manager.
#. In the navigation pane on the left, choose **Local Server**. In the right pane, locate **Windows Update** and click the link that follows it.
#. On the **Windows Update** page, click **Install updates automatically**.

   .. note::

      Determine whether to enable automatic Windows update based on the site requirements. Do not interrupt the update until it is finished.

Windows Server 1709
-------------------

#. Log in to the Windows VM.
#. In the CLI, enter **regedit** to open the registry.
#. Modify registry entries.

   -  In the **Registry Editor** window, choose **HKEY_LOCAL_MACHINE** > **SOFTWARE** > **Policies** > **Microsoft** > **Windows** > **WindowsUpdate** > **AU** and add the following information:

      .. code-block::

         [HKEY_LOCAL_MACHINE/SOFTWARE/Policies/Microsoft/Windows/WindowsUpdate/AU]
         "NoAutoUpdate"=dword:00000000
         "AUOptions"=dword:00000002
         "ScheduledInstallDay"=dword:00000000
         "UseWUServer"=dword:00000001

   -  In the **Registry Editor** window, choose **HKEY_LOCAL_MACHINE** > **SOFTWARE** > **Policies** > **Microsoft** > **Windows** > **WindowsUpdate** and add the following information:

      .. code-block::

         [HKEY_LOCAL_MACHINE/SOFTWARE/Policies/Microsoft/Windows/WindowsUpdate]
         "WUServer"="http://winupdate.otc-service.com"
         "WUStatusServer"="http://winupdate.otc-service.com"
         "TargetGroupEnabled"=dword:00000001
         "TargetGroup"="reg"

.. |image1| image:: /_static/images/en-us_image_0098735721.png
