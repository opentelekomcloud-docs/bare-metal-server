:original_name: en-us_topic_0081116782.html

.. _en-us_topic_0081116782:

Configuring the VNC Service
===========================

#. Run the following command to check whether VNC Server has been installed on the host:

   **rpm -qa \| grep tigervnc-server**

   Command output:

   .. code-block::

      tigervnc-server-1.1.0-5.e16.x86_64

   -  If no command output is displayed or the command output shows that VNC Server is not installed, go to :ref:`2 <en-us_topic_0081116782__en-us_topic_0094568903_li7428171213133>`.
   -  If the command output shows that VNC Server has been installed, go to :ref:`3 <en-us_topic_0081116782__en-us_topic_0094568903_li1289141120137>`.

#. .. _en-us_topic_0081116782__en-us_topic_0094568903_li7428171213133:

   (Optional) Install tigervnc-server.

   a. Run the **lsblk** command (the OS ISO file must have been mounted to the BMC virtual CD-ROM drive. If not, mount the ISO file in the same way as you mount it during OS installation).

      .. note::

         If you cannot log in to or perform operations on BMC, contact O&M administrators.

   b. Locate the block device whose **name** is **sr0** and **type** is **rom**, and check whether any directories are mounted to the mount point. If no, run the following command:

      **mount /dev/sr0 /mnt**

   c. Enter the **/etc/yum.repos.d** directory where the configuration is stored and back up all **.repo** files. Use vim to create a **.repo** file, for example **tiger.repo**. The file content is as follows:

      .. code-block::

         [rhel-local]
         baseurl=file:///mnt
         enabled=1
         gpgcheck=0

      Save the file and run the following commands:

      **yum repolist**

      **yum install tigervnc-server**

#. .. _en-us_topic_0081116782__en-us_topic_0094568903_li1289141120137:

   Run the following command to start the VNC service:

   **vncserver**

   Configure the VNC login password of user **root** as prompted.

   The command output contains **Log file is /root/.vnc/rhel:1.log**. **1** indicates that the first VNC virtual desktop is allocated to you.

#. Run the following command to check whether the Xvnc process exists:

   **ps -ef \| grep Xvnc**

   |image1|

   The process ID is **36069**, port number is **5901**, and virtual desktop number is **1**.

#. Run the following command to check the VNC virtual desktop of the current user:

   **vncserver -list**

   |image2|

   The current user has three virtual desktops, 1, 5, and 2.

#. Connect VNC Viewer on the local Windows with VNC Server on the host to remotely log in to the host.

   Choose **Options** > **Expert** > **ColorLevel** to set **ColorLevel** to **rgb222** if the version of VNC Viewer is 5.3.2 when you install it for the first time.

#. Run the following command to add a virtual desktop for the current user:

   **vncserver :**\ *6*

   Run the **vncserver -list** command to check whether the virtual desktop is added successfully. As shown in the following figure, the virtual desktop 6 is added successfully.

   |image3|

.. |image1| image:: /_static/images/en-us_image_0110275803.png
.. |image2| image:: /_static/images/en-us_image_0094568763.png
.. |image3| image:: /_static/images/en-us_image_0094568860.png
