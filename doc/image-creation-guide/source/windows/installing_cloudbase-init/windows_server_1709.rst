:original_name: en-us_topic_0108489935.html

.. _en-us_topic_0108489935:

Windows Server 1709
===================

#. Download the Cloudbase-Init installation package as instructed in :ref:`Preparing Hardware and Software <en-us_topic_0081116571>`.

#. Upload the package to the host and generate an ISO file.

   Upload the installation package to the host.

   .. code-block:: console

      [root@server nl]# ll
      total 4390172
      -rw-r--r--. 1 root root    41070592  Sep 26 07:33 CloudbaseInitSetup_0_9_11_x64.msi
      -rw-r--r--. 1 qemu qemu  4413020160  Sep 26 02:36

   Run the following command in the directory where the installation package is stored:

   **mkisofs -L -R -J -T -V system-sp2 -o** *software*\ **.iso** **CloudbaseInitSetup_0_9_11_x64.msi**

#. Mount the generated ISO file to the VM and install Cloudbase-Init.

   a. On virt-manager, choose **View** > **Details**.

   b. In the navigation pane on the left, choose **IDE CDROM 1**. In the right pane, click **Disconnect**.

   c. Click **Connect**.

   d. Select the local ISO file and click **Open** in the upper right corner.

      |image1|

   e. Confirm the settings and click **Apply**.

#. Copy the **CloudbaseInitSetup_0_9_11_x64.msi** installation package to drive C on the VM.

   a. Log in to the VM, click **Start**, enter **cmd** in the **Type here to search** box to open the command-line interface (CLI).

   b. Enter **D:**.

   c. Run the **xcopy CloudbaseInitSetup_0_9_11_x64.msi C:\\** command to copy the file.

      |image2|

#. Install Cloudbase-Init.

   a. Enter **C:**.

   b. Run the **CloudbaseInitSetup_0_9_11_x64.msi** command and press **Enter** to start the installation.

      The default installation path of Cloudbase-Init is:

      C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init

#. Edit the Cloudbase-Init configuration file **cloudbase-init.conf**.

   Configure the file as instructed in :ref:`5 <en-us_topic_0108488467__en-us_topic_0103266721_li80183372211>`.

.. |image1| image:: /_static/images/en-us_image_0110262981.png
.. |image2| image:: /_static/images/en-us_image_0110263254.png
