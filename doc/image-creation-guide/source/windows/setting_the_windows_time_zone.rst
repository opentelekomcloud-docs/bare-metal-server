:original_name: en-us_topic_0085894430.html

.. _en-us_topic_0085894430:

Setting the Windows Time Zone
=============================

Linux uses the time of the motherboard CMOS chip as the Coordinated Universal Time (UTC) and determines the system time based on the configured time zone. However, Windows uses the CMOS time as the system time directly without converting it based on the time zone. You need to perform the following steps:

#. Log in to the Windows VM.
#. Click |image1| in the lower left corner, choose **Windows PowerShell**, and enter **regedit.exe** to open the registry.
#. In the displayed **Registry Editor** window, choose **HKEY_LOCAL_MACHINE** > **SYSTEM** > **CurrentControlSet** > **Control** > **TimeZoneInformation**.
#. In the right pane, right-click a blank area and choose **New** > **DWORD (32-bit) Value** to add a REG_DWORD code. Set its name to **RealTimeIsUniversal** and value to **1**.

   .. note::

      If the operations cannot be performed by using a mouse, you can use the keyboard instead.

.. |image1| image:: /_static/images/en-us_image_0172483701.png
