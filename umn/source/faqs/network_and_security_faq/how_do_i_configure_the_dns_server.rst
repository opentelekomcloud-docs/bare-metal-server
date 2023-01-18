:original_name: en-us_topic_0118945920.html

.. _en-us_topic_0118945920:

How Do I Configure the DNS Server?
==================================

When installing Agent on a BMS, ensure that the DNS server of the BMS runs properly. This section describes how to configure the DNS server and how to verify the DNS server status.

Linux
-----

#. Log in to the BMS as user **root**.

#. Run the following command to edit the **resolv.conf** file:

   **vi /etc/resolv.conf**

#. Press **i** to enter editing mode and enter **nameserver** *DNS server IP address* before existing **nameserver** configurations.

   The format is as follows:

   .. code-block::

      nameserver 100.125.4.25

#. Press **Esc** and enter **:wq** to save the change and exit.

#. Run the following commands to restart the network:

   **rcnetwork restart**

   **service network restart**

   **/etc/init.d/network restart**

Windows
-------

The following steps use Windows Server 2012 R2 as an example to describe how to configure the DNS server for Windows:

#. Log in to the BMS as user **Administrator**.

#. Click |image1| in the lower left corner to start **Control Panel**.

#. Choose **Network and Internet** > **Network and Sharing Center**. Then, click the NIC for which you are to configure the DNS server, such as **Ethernet 3**.


   .. figure:: /_static/images/en-us_image_0177079630.png
      :alt: **Figure 1** Network and Sharing Center

      **Figure 1** Network and Sharing Center

#. Click **Properties**. :ref:`Figure 2 <en-us_topic_0118945920__fig18672112218013>` shows the **Ethernet 3 Status**.

   .. _en-us_topic_0118945920__fig18672112218013:

   .. figure:: /_static/images/en-us_image_0177079750.png
      :alt: **Figure 2** Ethernet 3 Status

      **Figure 2** Ethernet 3 Status

#. In the displayed **Ethernet 3 Status** dialog box, select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.


   .. figure:: /_static/images/en-us_image_0177080622.png
      :alt: **Figure 3** Ethernet 3 Properties

      **Figure 3** Ethernet 3 Properties

#. In the displayed **Internet Protocol Version 4 (TCP/IPv4) Properties** dialog box, select **Use the following DNS server addresses:** and configure the required parameters shown in :ref:`Figure 4 <en-us_topic_0118945920__fig5487194145010>`.

   The DNS server IP address is 100.125.4.25. After completing the configuration, click **OK**.

   .. _en-us_topic_0118945920__fig5487194145010:

   .. figure:: /_static/images/en-us_image_0177079125.png
      :alt: **Figure 4** Configuring the DNS server

      **Figure 4** Configuring the DNS server

#. After completing the configuration, click |image2|, select **Windows PowerShell**, and enter the **ipconfig /all** command. The configured IP address is displayed in **DNS Servers**.

.. |image1| image:: /_static/images/en-us_image_0177077692.png
.. |image2| image:: /_static/images/en-us_image_0177081710.png
