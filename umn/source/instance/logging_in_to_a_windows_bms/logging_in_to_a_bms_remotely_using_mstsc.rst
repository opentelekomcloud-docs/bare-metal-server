:original_name: en-us_topic_0079188786.html

.. _en-us_topic_0079188786:

Logging In to a BMS Remotely Using MSTSC
========================================

Scenarios
---------

This section describes how to log in to a Windows BMS using MSTSC (a remote login tool) from your local PC.

Prerequisites
-------------

-  The BMS must be in **Running** state.
-  You have obtained the password for logging in to the Windows BMS. For details, see :ref:`Obtaining the Password of a Windows BMS <en-us_topic_0140749073>`.
-  You have bound an EIP to the BMS. For details, see :ref:`Binding an EIP to a BMS <en-us_topic_0053655291>`.
-  You have configured the inbound rules of the security group. For details, see :ref:`Adding Security Group Rules <en-us_topic_0053536889>`.
-  The network connection between the login tool and the target BMS is normal. For example, the default port 3389 is not blocked by the firewall.

Procedure
---------

The following procedure describes how to log in to a Windows BMS using **mstsc.exe**.

#. On the local PC, click **Start**.
#. In the **Search programs and files** text box, enter **mstsc.exe**.
#. Enter the EIP and username of the Windows BMS, click **Connect**, enter the password as prompted, and click **OK**.
