:original_name: en-us_topic_0218670457.html

.. _en-us_topic_0218670457:

SUSE/Red Hat/CentOS/Oracle Linux/Ubuntu/Debian
==============================================

You can install Cloud-Init in either of the following ways: :ref:`(Recommended) Install Cloud-Init Using the Official Installation Package <en-us_topic_0218670457__en-us_topic_0217827710_section9013470154018>` and :ref:`Install Cloud-Init Using the Official Source Code Package and pip <en-us_topic_0218670457__en-us_topic_0217827710_section124220553610>`.

.. _en-us_topic_0218670457__en-us_topic_0217827710_section9013470154018:

(Recommended) Install Cloud-Init Using the Official Installation Package
------------------------------------------------------------------------

The method of installing Cloud-Init on a VM varies depending on the OS. Perform the installation operations as user **root**.

The following describes how to install Cloud-Init on VMs running SUSE, CentOS, Debian, and Ubuntu. For other OS types, install the required type of Cloud-Init. For example, you need to install coreos-cloudinit on VMs running CoreOS.

-  SUSE Linux

   Paths for obtaining the Cloud-Init installation package for SUSE Linux

   `http://ftp5.gwdg.de/pub/opensuse/repositories/Cloud:/Tools/ <http://ftp5.gwdg.de/pub/opensuse/repositories/Cloud:/Tools>`__

   http://download.opensuse.org/repositories/Cloud:/Tools/

   .. note::

      Select the required repo installation package in the provided paths.

   Take SUSE Enterprise Linux Server 12 as an example. Perform the following steps to install Cloud-Init:

   #. Run the following command to install the network installation source for SUSE Enterprise Linux Server 12:

      **zypper ar http://ftp5.gwdg.de/pub/opensuse/repositories/Cloud:/Tools/SLE_12_SP3/Cloud:Tools.repo**

   #. Run the following command to update the network installation source:

      **zypper refresh**

   #. Run the following command to install Cloud-Init:

      **zypper install cloud-init**

   #. Run the following commands to enable Cloud-Init to automatically start upon system boot:

      -  SUSE 11

         **chkconfig cloud-init-local on; chkconfig cloud-init on; chkconfig cloud-config on; chkconfig cloud-final on**

         **service cloud-init-local status; service cloud-init status; service cloud-config status; service cloud-final status**

      -  SUSE 12 and openSUSE 12/13/42

         **systemctl enable cloud-init-local.service cloud-init.service cloud-config.service cloud-final.service**

         **systemctl status cloud-init-local.service cloud-init.service cloud-config.service cloud-final.service**

      .. important::

         For SUSE and openSUSE, perform the following steps to disable dynamic change of the VM name:

         a. Run the following command to open the **dhcp** file using the vi editor:

            **vi** **etc/sysconfig/network/dhcp**

         b. Change the value of **DHCLIENT_SET_HOSTNAME** in the **dhcp** file to **no**.

-  CentOS

   :ref:`Table 1 <en-us_topic_0218670457__en-us_topic_0217827710_table859383892814>` lists the Cloud-Init installation paths for CentOS. Select an address from the following table and download the EPEL release package.

   .. _en-us_topic_0218670457__en-us_topic_0217827710_table859383892814:

   .. table:: **Table 1** Cloud-Init installation package addresses

      +---------+----------+--------------------------------------------------------------------------+
      | OS Type | Version  | How to Obtain                                                            |
      +=========+==========+==========================================================================+
      | CentOS  | 6 32-bit | https://archives.fedoraproject.org/pub/archive/epel/6/i386/Packages/e/   |
      +---------+----------+--------------------------------------------------------------------------+
      |         | 6 64-bit | https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/Packages/e/ |
      +---------+----------+--------------------------------------------------------------------------+
      |         | 7 64-bit | https://archives.fedoraproject.org/pub/archive/epel/7/x86_64/Packages/e/ |
      +---------+----------+--------------------------------------------------------------------------+

   Run the following commands to install Cloud-Init on a VM running CentOS 6.5 64-bit (example):

   **yum install https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/Packages/e/epel-release-**\ *xx-xx*\ **.noarch.rpm**

   **yum install cloud-init**

   .. note::

      *xx-xx* indicates the version of Extra Packages for Enterprise Linux (EPEL) release required by the OS.

-  Debian

   Before installing Cloud-Init, ensure that the network installation source address has been configured for the OS by checking whether the **/etc/apt/sources.list** file contains the installation source address of the software package. If the file does not contain the address, configure the address by following the instructions on the Debian official website.

   Run the following commands to install Cloud-Init:

   **apt-get update**

   **apt-get install** **cloud-init**

   After Cloud-Init is installed in the Debian OS, run the following commands to install the vlan and ifenslave services:

   **apt-get install vlan**

   **apt-get install ifenslave**

-  Ubuntu

   Before installing Cloud-Init, ensure that the network installation source address has been configured for the OS by checking whether the **/etc/apt/sources.list** file contains the installation source address of the software package. If the file does not contain the address, configure the address by following the instructions on the Ubuntu official website.

   Run the following commands to install Cloud-Init:

   **apt-get update**

   **apt-get install** **cloud-init**

   After Cloud-Init is installed in the Ubuntu OS, perform the following operations to install tools and services:

   #. Install the SSH service.

      For x86, run the following commands:

      **apt-get install openssh-client**

      **apt-get install openssh-server**

      For ARM64, run the following commands:

      **apt install openssh-client**

      **apt install openssh-server**

   #. Install dkms.

      To ensure that SDI drivers can run properly, you need to install dkms for Ubuntu.

      Run the following command to install the tool:

      **apt-get install dkms**

      Then, run the following command:

      **vi /usr/sbin/dkms**

      Go to line 283 (press **shift** and **:** to enter the CLI mode. Then, type **283** and press **Enter**) and modify this line as follows:

      .. code-block::

         invoke_command "$mkinitrd -f $initrd_dir/$initrd $1" "$mkinitrd" background

   #. Install the vlan and ifenslave services.

      **apt-get install vlan**

      **apt-get install ifenslave**

   #. Install the ifupdown service.

      **apt-get install ifupdown**

.. _en-us_topic_0218670457__en-us_topic_0217827710_section124220553610:

Install Cloud-Init Using the Official Source Code Package and pip
-----------------------------------------------------------------

The following operations use Cloud-Init 0.7.9 as an example to describe how to install Cloud-Init.

#. Download the **cloud-init-0.7.9.tar.gz** source code package (version 0.7.9 is recommended) and upload it to the **/home/** directory of the VM.

   Download **cloud-init-0.7.9.tar.gz** from the following path:

   https://launchpad.net/cloud-init/trunk/0.7.9/+download/cloud-init-0.7.9.tar.gz

#. Create a **pip.conf** file in the **~/.pip/** directory and edit the following content:

   .. note::

      If the **~/.pip/** directory does not exist, run the **mkdir ~/.pip** command to create it.

   .. code-block::

      [global]
      index-url  = https://<$mirror>/simple/
      trusted-host = <$mirror>

   .. note::

      Replace *<$mirror>* with a public network PyPI source.

      Public network PyPI source: https://pypi.python.org/

#. Run the following command to install the downloaded Cloud-Init source code package (select **--upgrade** as needed during installation):

   **pip install [--upgrade] /home/cloud-init-0.7.9.tar.gz**

#. Run the **cloud-init -v** command. Cloud-Init is installed successfully if the following information is displayed:

   .. code-block::

      cloud-init 0.7.9

#. Enable Cloud-Init to automatically start upon system boot.

   -  If the OS uses SysVinit to manage automatic start of services, run the following commands:

      **chkconfig --add cloud-init-local; chkconfig --add cloud-init; chkconfig --add cloud-config; chkconfig --add cloud-final**

      **chkconfig cloud-init-local on; chkconfig cloud-init on; chkconfig cloud-config on; chkconfig cloud-final on**

      **service cloud-init-local status; service cloud-init status; service cloud-config status; service cloud-final status**

   -  If the OS uses Systemd to manage automatic start of services, run the following commands:

      **systemctl enable cloud-init-local.service cloud-init.service cloud-config.service cloud-final.service**

      **systemctl status cloud-init-local.service cloud-init.service cloud-config.service cloud-final.service**

.. important::

   If you install Cloud-Init using the official source code package and pip, pay attention to the following:

   #. Add user **syslog** to the **adm** group during the installation. If user **syslog** exists, add it to the **adm** group. For some OSs (such as CentOS and SUSE), user **syslog** may not exist. Run the following commands to create user **syslog** and add it to the **adm** group:

      **useradd syslog**

      **groupadd adm**

      **usermod -g adm syslog**

   #. Change the value of **distro** in **system_info** in the **/etc/cloud/cloud.cfg** file based on the OS release version, such as **distro: ubuntu**, **distro: sles**, **distro: debian**, and **distro: fedora**.
