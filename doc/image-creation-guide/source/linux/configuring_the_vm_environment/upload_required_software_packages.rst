:original_name: en-us_topic_0000001194038234.html

.. _en-us_topic_0000001194038234:

Upload Required Software Packages
=================================

Scenario
--------

Three methods are available for uploading required software packages.

Procedure
---------

-  Method 1: If the VM can communicate with the host, run the **scp** command to upload software packages to the VM. (This method is recommended. You can learn how to use the **scp** command by running **scp -help**.)

   For example, you can run the following command (the file name is an example only):

   **scp** **fsp@**\ *xxx.xxx.xxx.xxx*\ **:/home/fsp/network-config-1.0-1.x86_64.rpm /home**

   The command indicates **scp** *Username*\ **@**\ *Host IP address*/*User-defined directory*/*File name*/*VM directory*.

-  Method 2: If the VM can communicate with the host and you can log in to the VM using Xshell, use Xftp to transfer software packages to the VM.

-  Method 3: If the VM cannot communicate with the host, use the virtual CD-ROM drive to mount software packages.

   **Step 1: Create an ISO file on the host.**

   Perform the following operations in the Linux terminal.

   -  Run the **mkdir /root/software** command to create a directory.
   -  Put **network-config** and the SDI driver package to the **software** directory.
   -  Run the **cd /root** command, and then run the **mkisofs -L -R -J -T -V system-sp2 -o defindsoftware.iso /root/software** command to create an ISO file.
   -  Run the **ll** command. The **defindsoftware.iso** displayed in the command output is the created ISO file.

   **Step 2: Use virt-manager to mount the ISO file.**

   #. On virt-manager, choose **View** > **Details**.

   #. In the navigation pane on the left, choose **IDE CDROM 1**. In the right pane, perform the operations specified in the following figure.

      |image1|

   #. Click **Browse Local** and select the **/root** directory.

   #. Locate and double-click the **defindsoftware.iso** file. In the displayed dialog box, click **OK**.

      |image2|

   #. Choose **View** > **Console**, and select the VM.

   #. After logging in to the VM, open the terminal and run **lsblk** to check whether the ISO file is mounted. For example, the ISO file can be mounted in the **/run/media/suse/system-sp2** directory.

   #. Run the **cd /run/media/suse/system-sp2** command to copy the ISO file to a directory, for example, **/home**. If the ISO is not mounted, run the **mount /dev/sr0** */home* command to manually mount the ISO file to the **/home** directory. */home* is an example only.

.. |image1| image:: /_static/images/en-us_image_0286527865.png
.. |image2| image:: /_static/images/en-us_image_0286527866.png
