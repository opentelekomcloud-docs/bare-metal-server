:original_name: en-us_topic_0112790033.html

.. _en-us_topic_0112790033:

Configuring a NIC (Ubuntu)
==========================

This section uses Ubuntu 16.04 LTS (Xenial Xerus x86_64) as an example to describe how to configure a NIC added to or deleted from a BMS.

.. note::

   -  The configuration methods of other Ubuntu OSs are similar to that of Ubuntu 16.04 LTS (Xenial Xerus x86_64).

   -  If the network is disconnected after a NIC is added and the BMS is restarted, run the following command:

      **ifup** **bond0.**\ *vlan*

      *vlan* indicates the VLAN used by the NIC.

      If the network is still disconnected, add the NIC again.

Add a NIC
---------

#. .. _en-us_topic_0112790033__li1558174719483:

   Obtain information about the NIC to be added.

   .. table:: **Table 1** NIC information

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                                       | Example Value         |
      +=======================+===================================================================================================================================+=======================+
      | VLAN and MAC address  | Specifies the VLAN information and MAC address of the NIC. To obtain them, perform the following operations:                      | 2847                  |
      |                       |                                                                                                                                   |                       |
      |                       | a. In the BMS list, click the name of the target BMS.                                                                             | fa:16:3e:a2:aa:65     |
      |                       |                                                                                                                                   |                       |
      |                       | b. .. _en-us_topic_0112790033__li58541779231:                                                                                     |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    Click the **NICs** tab, locate the row that contains the NIC to be added, and click |image1| to expand details.                |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Obtain the values of **VLAN** and **MAC Address**.                                                                             |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Gateway               | Specifies the gateway address of the NIC. To obtain them, perform the following operations:                                       | 192.168.1.1           |
      |                       |                                                                                                                                   |                       |
      |                       | a. .. _en-us_topic_0112790033__li32431027104614:                                                                                  |                       |
      |                       |                                                                                                                                   |                       |
      |                       |    On the NIC details page in :ref:`2 <en-us_topic_0112790033__li58541779231>`, obtain the subnet information.                    |                       |
      |                       |                                                                                                                                   |                       |
      |                       | b. On the BMS details page, click the link following **VPC** to switch to the VPC list.                                           |                       |
      |                       |                                                                                                                                   |                       |
      |                       | c. Click the name of the VPC to which the BMS belongs to go to the VPC details page.                                              |                       |
      |                       |                                                                                                                                   |                       |
      |                       | d. Click the **Subnets** tab and obtain the gateway address of the subnet in :ref:`1 <en-us_topic_0112790033__li32431027104614>`. |                       |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Use a key or password to log in to the BMS as user **root**.

#. Check whether the **/etc/network/interfaces.d/** directory contains the **/etc/network/interfaces.d/70-cloud-init.cfg** file.

   -  If yes, go to step :ref:`5 <en-us_topic_0112790033__li27700107517>`.
   -  If no, go to step :ref:`4 <en-us_topic_0112790033__li05281426185416>`.

#. .. _en-us_topic_0112790033__li05281426185416:

   Run the following commands to generate the **/etc/network/interfaces.d/70-cloud-init.cfg** file and set the file permissions:

   **touch** **/etc/network/interfaces.d/70-cloud-init.cfg**

   **chmod** **644** **/etc/network/interfaces.d/70-cloud-init.cfg**

#. .. _en-us_topic_0112790033__li27700107517:

   Run the following command to edit the **/etc/network/interfaces.d/70-cloud-init.cfg** file and add information about the NIC to be added to the file:

   **vim** **/etc/network/interfaces.d/70-cloud-init.cfg**

   Edit the file as follows:

   .. code-block::

      auto bond0.2847
      iface bond0.2847 inet dhcp
      mtu 8888
      hwaddress fa:16:3e:a2:aa:65
      vlan-raw-device bond0

   The required information has been obtained in step :ref:`1 <en-us_topic_0112790033__li1558174719483>`.

   -  *bond0.2847*: indicates the name of the NIC to be added. **bond0** is a fixed value and the number following it is the VLAN information of the NIC.
   -  *hwaddress*: indicates the MAC address of the NIC to be added.
   -  *vlan-raw-device*: The default value **bond0** is used.

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. Run the following command to start the added NIC:

   **ifup** **bond0.**\ *vlan*

   For example, to start bond0.2847, run the **ifup bond0.2847** command.

#. Run the following command to check the status of the NIC device:

   **ip** **link**

   |image2|

#. Ping the gateway from the new network device to check whether the network connectivity is normal.

   Use the gateway address obtained from :ref:`1 <en-us_topic_0112790033__li1558174719483>`.

   |image3|

Delete a NIC
------------

#. .. _en-us_topic_0112790033__li960312341080:

   Obtain the VLAN and MAC address of the VPC NIC to be deleted.

#. Use a key or password to log in to the BMS as user **root**.

#. Locate the network device based on the VLAN information and run the following commands to stop and delete the device:

   .. code-block::

      root@ubuntu:~# ip link | grep 2847
      9: bond0.2847@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8888 qdisc noqueue state UP mode DEFAULT group default qlen 1000
      root@ubuntu:~# ifconfig bond0.2847 down
      root@ubuntu:~# ip link delete bond0.2847

#. Check whether the BMS OS has been reinstalled after the NIC is added to the BMS.

   -  If no, go to step :ref:`5 <en-us_topic_0112790033__li4483427910>`.
   -  If yes, go to step :ref:`9 <en-us_topic_0112790033__li9305111119230>`.

#. .. _en-us_topic_0112790033__li4483427910:

   Run the following command to copy the **/etc/network/interfaces.d/70-cloud-init.cfg** file to generate the **/etc/network/interfaces.d/70-cloud-init.cfg.bak** file to back up the network configuration:

   **cp** **-p** **/etc/network/interfaces.d/70-cloud-init.cfg** **/etc/network/interfaces.d/70-cloud-init.cfg.bak**

#. Run the following command to edit **/etc/network/interfaces.d/70-cloud-init.cfg**, locate the NIC to be deleted based on the VLAN and MAC address obtained from :ref:`1 <en-us_topic_0112790033__li960312341080>`, and delete the NIC information from the file:

   **vim** **/etc/network/interfaces.d/70-cloud-init.cfg**

   .. code-block::

      # The following information needs to be deleted:
      auto bond0.2847
      iface bond0.2847 inet dhcp
      mtu 8888
      hwaddress fa:16:3e:a2:aa:65
      vlan-raw-device bond0

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. After the NIC is deleted, if the **/etc/network/interfaces.d/70-cloud-init.cfg** file contains no NIC information, run the following command to delete the **/etc/network/interfaces.d/70-cloud-init.cfg** file:

   **rm** **/etc/network/interfaces.d/70-cloud-init.cfg**

#. Check whether other NICs run properly. If they run properly, run the following command to delete the **/etc/network/interfaces.d/70-cloud-init.cfg.bak** file:

   **rm** **/etc/network/interfaces.d/70-cloud-init.cfg.bak**

#. .. _en-us_topic_0112790033__li9305111119230:

   Run the following command to copy the **/etc/network/interfaces.d/50-cloud-init.cfg** file to generate the **/etc/network/interfaces.d/50-cloud-init.cfg.bak** file to back up the network configuration:

   **cp** **-p** **/etc/network/interfaces.d/50-cloud-init.cfg** **/etc/network/interfaces.d/50-cloud-init.cfg.bak**

#. Run the following command to edit **/etc/network/interfaces.d/50-cloud-init.cfg**, locate the NIC to be deleted based on the VLAN and MAC address obtained from :ref:`1 <en-us_topic_0112790033__li960312341080>`, and delete the NIC information from the file:

   **vim** **/etc/network/interfaces.d/50-cloud-init.cfg**

   .. code-block::

      # The following information needs to be deleted:
      auto bond0.2847
      iface bond0.2847 inet dhcp
      mtu 8888
      hwaddress fa:16:3e:a2:aa:65
      vlan-raw-device bond0

   After the modification, press **Esc**, enter **:wq**, save the configuration, and exit.

#. Check whether other NICs run properly. If they run properly, run the following command to delete the **/etc/network/interfaces.d/50-cloud-init.cfg.bak** file:

   **rm** **/etc/network/interfaces.d/50-cloud-init.cfg.bak**

.. |image1| image:: /_static/images/en-us_image_0112916295.png
.. |image2| image:: /_static/images/en-us_image_0112917155.png
.. |image3| image:: /_static/images/en-us_image_0112917313.png
