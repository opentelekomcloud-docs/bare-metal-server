:original_name: en-us_topic_0053537015.html

.. _en-us_topic_0053537015:

Logging In to a BMS Using an SSH Password
=========================================

Scenarios
---------

This section describes how to log in to a Linux BMS using an SSH password from a Windows or Linux PC.

Prerequisites
-------------

-  The BMS must be in **Running** state.
-  You have bound an EIP to the BMS. For details, see :ref:`Binding an EIP to a BMS <en-us_topic_0053655291>`.
-  You have configured the inbound rules of the security group. For details, see :ref:`Adding Security Group Rules <en-us_topic_0053536889>`.
-  The network connection between the login tool (such as PuTTY) and the target BMS is normal. For example, the default port 22 is not blocked by the firewall.
-  By default, login to a Linux BMS using an SSH password is disabled. If you want to use this function, log in to the BMS (see :ref:`Logging In to a BMS Using an SSH Key Pair <en-us_topic_0053536938>`) and enable the function. For details, see :ref:`How Do I Set SSH Configuration Items? <en-us_topic_0096201996>`

Log In to a BMS from a Windows PC
---------------------------------

You can use the following methods to log in to a Linux BMS from a local PC running Windows (for example, use PuTTY):

.. note::

   Download PuTTY from https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html.

#. Run PuTTY.
#. In the navigation pane on the left, choose **Session**, enter the EIP of the BMS in the text box under **Host Name (or IP address)**, and select **SSH** for **Connection type**.
#. Choose **Windows** > **Translation** and select **UTF-8** from the **Received data assumed to be in which character set:** drop-down list box.
#. Click **Open**.
#. Enter username **root** and the password you set to log in to the BMS.

Log In to a BMS from a Linux PC
-------------------------------

To log in to a Linux BMS from a Linux PC, run the following command:

**ssh** *EIP of the BMS*
