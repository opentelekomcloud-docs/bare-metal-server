:original_name: en-us_topic_0083157921.html

.. _en-us_topic_0083157921:

How Can I Handle the Eight-Hour Difference Between the Windows BMS and Local Time
=================================================================================

Cause
-----

Linux uses the time of the motherboard CMOS chip as the Coordinated Universal Time (UTC) and determines the system time based on the configured time zone. However, Windows uses the CMOS time as the system time directly without converting it based on the time zone.

Solution
--------

#. Log in to the Windows BMS.

#. Click |image1| in the lower left corner, choose **Windows PowerShell**, and enter **regedit.exe** to open the registry.

#. In the displayed **Registry Editor** window, choose **HKEY_LOCAL_MACHINE** > **SYSTEM** > **CurrentControlSet** > **Control** > **TimeZoneInformation**.

#. In the right pane, right-click a blank area and choose **New** > **DWORD (32-bit) Value** to add a REG_DWORD code. Set its name to **RealTimeIsUniversal** and value to **1**.


   .. figure:: /_static/images/en-us_image_0284616150.png
      :alt: **Figure 1** Adding a code

      **Figure 1** Adding a code

#. After the modification, restart the BMS.

   After the BMS restarts, its system time is consistent with the local time.

.. |image1| image:: /_static/images/en-us_image_0284616149.png
