:original_name: en-us_topic_0068279730.html

.. _en-us_topic_0068279730:

How Do I Configure the Static Host Name of a BMS?
=================================================

Symptom
-------

The static host name of a Linux BMS is user-defined and injected on the console during the BMS creation. You can use the console or run the **hostname** command to change the host name of a BMS. However, if you restart the BMS, its host name will be automatically changed to the user-defined one injected on the console.

Automatically Updating the Host Name (Recommended)
--------------------------------------------------

Change the host name of the BMS on the console and enable automatic host name synchronization in the BMS OS. In this way, after the BMS is restarted, it automatically synchronizes the host name from the console.

This method has the following restrictions:

-  The host name contains a maximum of 63 characters.
-  Special characters except hyphens (-), underscores (_), and periods (.) are not supported.
-  Uppercase letters are not supported.
-  This method does not apply to Windows BMSs.

#. Log in to the management console, click **Bare Metal Server** under **Computing**.

#. Click the name of the BMS whose name is to be changed.

#. On the displayed page, click |image1| next to **Name**, enter a new name that meets the preceding requirements, and click |image2| to save the change.

#. .. _en-us_topic_0068279730__li1574320984514:

   Log in to the BMS OS and run the following command to enable automatic hostname synchronization:

   **vi /opt/huawei/network_config/bms-network-config.conf**

   Set the value of **auto_synchronize_hostname** to **True**.

   .. code-block::

      auto_synchronize_hostname = True

   Press **Esc** and enter **:wq** to save and exit the file.

#. Log in to the management console again. Locate the row that contains the BMS, click **More** in the **Operation** column, and select **Restart**.

   After about 10 minutes, verify that the BMS is restarted and its hostname is automatically updated.

   .. note::

      If you set the value of **auto_synchronize_hostname** in step :ref:`4 <en-us_topic_0068279730__li1574320984514>` to **False**, the host name configured during BMS creation will be retained.

Manually Updating the Host Name
-------------------------------

To make the changed host name take effect even after the BMS is stopped or restarted, save the changed name into configuration files.

For example, if the changed host name is *new_hostname*, perform the following steps:

#. Modify the **/etc/hostname** configuration file.

   a. Run the following command to edit the **/etc/hostname** configuration file:

      **sudo vim /etc/hostname**

   b. Change the host name to *new_hostname*.

   c. Run the following command to save and exit the configuration file:

      **:wq**

#. (Optional) For Red Hat Enterprise Linux, CentOS, and Fedora 6, modify the configuration file **/etc/sysconfig/network**.

   a. Run the following command to edit the **/etc/sysconfig/network** configuration file:

      **sudo vim /etc/sysconfig/network**

   b. Change the **HOSTNAME** value to *new_hostname*.

      **HOSTNAME=**\ *new_hostname*

   c. Run the following command to save and exit the configuration file:

      **:wq**

#. Modify the **/etc/cloud/cloud.cfg** configuration file.

   a. Run the following command to edit the **/etc/cloud/cloud.cfg** configuration file:

      **sudo vim /etc/cloud/cloud.cfg**

   b. Use either of the following methods to modify the configuration file:

      -  Method 1: Change the **preserve_hostname** parameter value or add the **preserve_hostname** parameter to the configuration file.

         If **preserve_hostname: false** is already available in the **/etc/cloud/cloud.cfg** configuration file, change it to **preserve_hostname: true**.

         If **preserve_hostname: false** is unavailable in the **/etc/cloud/cloud.cfg** configuration file, add **preserve_hostname: true** before **cloud_init_modules**.

      -  Method 2: Delete or comment out the following content:

         **update_hostname**

   c. Run the following command to save and exit the configuration file:

      **:wq**

#. Change the BMS network configuration script **bms-network-config.conf**.

   The value of parameter **enable_preserve_hostname** in the **bms-network-config.conf** file is **False** by default, indicating that the host name is updated each time the board resets. To disable this function, change its value to **True**.

   a. Run the following command to edit the configuration script **bms-network-config.conf**:

      **sudo vim /opt/huawei/network_config/bms-network-config.conf**

   b. Set the value of **enable_preserve_hostname** to **True**.

      **enable_preserve_hostname: True**

   c. Run the following command to save and exit the configuration file:

      **:wq!**

#. (Optional) For SUSE, modify the configuration file **/etc/sysconfig/network/dhcp**.

   a. Run the following command to edit the **/etc/sysconfig/network/dhcp** configuration file:

      **sudo vim /etc/sysconfig/network/dhcp**

   b. Set the value of **DHCLIENT_SET_HOSTNAME** to **no** to ensure that DHCP does not automatically allocate host names.

      **DHCLIENT_SET_HOSTNAME="no"**

   c. Run the following command to save and exit the configuration file:

      **:wq**

#. Run the following command to restart the BMS:

   **sudo reboot**

#. Run the following command to check whether the static host name is changed:

   **sudo hostname**

   If the changed host name *new_hostname* is displayed in the command output, the host name is changed and the new name permanently takes effect.

.. |image1| image:: /_static/images/en-us_image_0284616146.png
.. |image2| image:: /_static/images/en-us_image_0284616147.png
