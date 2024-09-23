:original_name: en-us_topic_0000002024654874.html

.. _en-us_topic_0000002024654874:

How Do I Check Whether a Physical Server Is Running Properly?
=============================================================

#. Log in to the OS as **root** and check the software installation path.

   **cat /etc/ascend_install.info**

   Information similar to the following should be displayed:

   .. code-block::

      Driver_Install_Path_Param=/usr/local/Ascend

#. Go to the driver installation directory and use **upgrade-tool** to check the file system version of the physical server.

   **cd** */usr/local/Ascend/*\ driver/tools/

   **./upgrade-tool --device_index -1 --system_version**

   If information similar to the following is returned, the physical server is running properly:

   |image1|

.. |image1| image:: /_static/images/en-us_image_0000002022646860.png
