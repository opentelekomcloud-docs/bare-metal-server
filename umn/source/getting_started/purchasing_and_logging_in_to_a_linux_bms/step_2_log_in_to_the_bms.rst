:original_name: en-us_topic_0140737435.html

.. _en-us_topic_0140737435:

Step 2: Log In to the BMS
=========================

Scenarios
---------

After you create a BMS, you can log in to it using multiple methods. This section describes the procedure to log in to a BMS using an SSH key pair. For more login modes, see :ref:`Linux BMS Login Methods <en-us_topic_0053536931>` or :ref:`Windows BMS Login Methods <en-us_topic_0097289761>`.

Procedure
---------

The following steps describe how to log in to a BMS using an SSH key pair through PuTTY.

#. Log in to the Cloud Server Console.
#. In the navigation pane, choose **Bare Metal Server**.
#. In the upper left corner, click |image1| and select a region.
#. In the BMS list, locate **bms-7676-nginx**. Record the EIP of the BMS and perform the following steps:

   a. Check whether the private key file has been converted to **.ppk** format.

      -  If yes, go to step :ref:`4.g <en-us_topic_0140737435__en-us_topic_0053536938_li693703913264>`.
      -  If no, go to step :ref:`4.b <en-us_topic_0140737435__en-us_topic_0053536938_li11816141811202>`.

   b. .. _en-us_topic_0140737435__en-us_topic_0053536938_li11816141811202:

      Visit the following website and download PuTTY and PuTTYgen:

      https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

      .. note::

         PuTTYgen is a private key generator, which is used to create a key pair that consists of a public key and a private key for PuTTY.

   c. Run PuTTYgen.

   d. In the **Actions** area, click **Load** and import the private key file that you stored when creating the BMS.

      Ensure that the private key file is in the format of **All files (*.*)**.

   e. Click **Save private key**.

   f. .. _en-us_topic_0140737435__en-us_topic_0053536938_li194442401260:

      Save the converted private key, for example, **kp-123.ppk**, to your local PC.

   g. .. _en-us_topic_0140737435__en-us_topic_0053536938_li693703913264:

      Double-click **PUTTY.EXE**. The **PuTTY Configuration** page is displayed.


      .. figure:: /_static/images/en-us_image_0080956622.png
         :alt: **Figure 1** PuTTY Configuration

         **Figure 1** PuTTY Configuration

   h. Choose **Connection** > **Data**. Enter the image username in **Auto-login username**.

      .. note::

         Contact the operation administrator to obtain the image username.

   i. Choose **Connection** > **SSH** > **Auth**. In the last configuration item **Private key file for authentication**, click **Browse** and select the .ppk private key in step :ref:`4.f <en-us_topic_0140737435__en-us_topic_0053536938_li194442401260>`.

   j. Choose **Session** and enter the EIP of the BMS in the box under **Host Name (or IP address)**.

   k. Click **Open**.

      Log in to the BMS.

.. |image1| image:: /_static/images/en-us_image_0149174576.png
