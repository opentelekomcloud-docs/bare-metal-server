:original_name: en-us_topic_0108489937.html

.. _en-us_topic_0108489937:

Windows Server 1709
===================

#. .. _en-us_topic_0108489937__en-us_topic_0103266724_li646115083510:

   Download **bms-network_config.rar** of the required version as instructed in :ref:`Software <en-us_topic_0081116771>`.

   Decompress the package to the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\LocalScripts\\** directory.

   a. Enter **D:**.

   b. Run the **xcopy bms-network-config.conf "C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\LocalScripts"\\** command.

      .. note::

         You can press **Tab** to complete the command.

      |image1|

      |image2|

   .. note::

      The value of **bsdtar_path** in the **bms-network-config.conf** file is **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\bin\\bsdtar.exe** by default. If Cloudbase-Init is installed in a non-default directory, set this parameter to the directory where **bsdtar.exe** is actually stored.

#. Use a text editor (such as Notepad) to open the Cloudbase-Init configuration file in the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\conf** directory and check the path specified by **local_scripts_path**. Cloudbase-Init will execute the scripts from this path.

   |image3|

#. Copy **bms-network-config.py** to the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\LocalScripts** directory based on the value of parameter **local_scripts_path** in the Cloudbase-Init configuration file. For details, see :ref:`1 <en-us_topic_0108489937__en-us_topic_0103266724_li646115083510>`.

   The default path of Cloudbase-Init is recommended. If you store the script file in another directory, change the value of parameter **local_scripts_path** in the Cloudbase-Init configuration file.

.. |image1| image:: /_static/images/en-us_image_0110263278.png
.. |image2| image:: /_static/images/en-us_image_0110263399.png
.. |image3| image:: /_static/images/en-us_image_0110264988.png
