:original_name: en-us_topic_0053536938.html

.. _en-us_topic_0053536938:

Logging In to a BMS Using an SSH Key Pair
=========================================

Scenarios
---------

This section describes how to log in to a Linux BMS using an SSH key pair from a Windows or Linux PC.

Prerequisites
-------------

-  The BMS must be in **Running** state.
-  You have obtained the private key file used during BMS creation.
-  You have bound an EIP to the BMS. For details, see :ref:`Binding an EIP to a BMS <en-us_topic_0053655291>`.
-  You have configured the inbound rules of the security group. For details, see :ref:`Adding Security Group Rules <en-us_topic_0053536889>`.
-  The network connection between the login tool (such as PuTTY) and the target BMS is normal. For example, the default port 22 is not blocked by the firewall.

Logging In to the Linux BMS from a Windows PC
---------------------------------------------

You can use the following methods to log in to a Linux BMS from a local PC running Windows:

**Method 1: Use PuTTY to log in to the BMS.**

Before logging in to the BMS using PuTTY, ensure that the private key file has been converted to .ppk format.

#. Check whether the private key file has been converted to **.ppk** format.

   -  If yes, go to step :ref:`7 <en-us_topic_0053536938__li693703913264>`.
   -  If no, go to step :ref:`2 <en-us_topic_0053536938__li11816141811202>`.

#. .. _en-us_topic_0053536938__li11816141811202:

   Visit the following website and download PuTTY and PuTTYgen:

   https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

   .. note::

      PuTTYgen is a private key generator, which is used to create a key pair that consists of a public key and a private key for PuTTY.

#. Run PuTTYgen.

#. In the **Actions** area, click **Load** and import the private key file that you stored when creating the BMS.

   Ensure that the private key file is in the format of **All files (*.*)**.

#. Click **Save private key**.

#. .. _en-us_topic_0053536938__li194442401260:

   Save the converted private key, for example, **kp-123.ppk**, to your local PC.

#. .. _en-us_topic_0053536938__li693703913264:

   Double-click **PUTTY.EXE**. The **PuTTY Configuration** page is displayed.


   .. figure:: /_static/images/en-us_image_0080956622.png
      :alt: **Figure 1** PuTTY Configuration

      **Figure 1** PuTTY Configuration

#. Choose **Connection** > **Data**. Enter the image username in **Auto-login username**.

   .. note::

      Contact the operation administrator to obtain the image username.

#. Choose **Connection** > **SSH** > **Auth**. In the last configuration item **Private key file for authentication**, click **Browse** and select the .ppk private key in step :ref:`6 <en-us_topic_0053536938__li194442401260>`.

#. Choose **Session** and enter the EIP of the BMS in the box under **Host Name (or IP address)**.

#. Click **Open**.

   Log in to the BMS.

**Method 2: Use Xshell to log in to the BMS.**

#. Start the Xshell tool.

#. Run the following command to remotely log in to the BMS through SSH:

   **ssh** *Username*\ **@**\ *EIP*

   Example:

   **ssh** **root@192.168.0.1**

#. (Optional) If the system displays the **SSH Security Warning** dialog box, click **Accept & Save**.

#. Select **Public Key** and click **Browse** beside the user key text box.

#. In the user key dialog box, click **Import**.

#. Select the locally stored key file and click **Open**.

#. Click **OK** to log in to the BMS.

Logging In to the Linux BMS from a Linux PC
-------------------------------------------

Perform the following operations to log in to a Linux BMS from a local PC running Linux: The following procedure uses private key file **KeyPair-ee55.pem** as an example to describe how to log in to the BMS.

#. On the Linux CLI, run the following command to change operation permissions:

   **chmod** **400** **/**\ *path*/*KeyPair-ee55*

   .. note::

      In the preceding command, **path** refers to the path under which the key file is stored.

#. Run the following command to log in to the BMS:

   **ssh** **-i** **/**\ *path*/*KeyPair-ee55* *xxx*\ **@**\ *EIP of the BMS*

   .. note::

      -  In the preceding command, *path* refers to the path under which the key file is stored.
      -  *xxx* indicates the username of the BMS image. Contact the operation administrator to obtain the username.
