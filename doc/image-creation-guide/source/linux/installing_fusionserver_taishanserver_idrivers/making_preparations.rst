:original_name: en-us_topic_0131700230.html

.. _en-us_topic_0131700230:

Making Preparations
===================

#. Determine the .zip driver packages to be used.

   Examples:

   -  CentOS 7.6: FusionServer iDriver-CentOS7.6-Driver-V116.zip
   -  RHEL 7.3: FusionServer iDriver-RHEL7.3-Driver-V116.zip
   -  Ubuntu 16.04: FusionServer iDriver-Ubuntu16.04-Driver-V116.zip
   -  EulerOS 2.8 ARM: TaiShanServer iDriver-EulerOS2.8-Driver-V103.zip
   -  CentOS 7.6 ARM: TaiShanServer iDriver-CentOS7.6-Driver-V112.zip

#. Obtain the installation packages. (Example for installing V5 server drivers: CentOS 7.6; examples for installing TaiShan server drivers: EulerOS 2.8 ARM and CentOS 7.6 ARM)

   -  CentOS 7.6

      Download and decompress the **FusionServer iDriver-CentOS7.6-Driver-V116.zip** driver package to obtain the **onboard_driver_CentOS7.6.iso** file. Decompress **onboard_driver_CentOS7.6.iso** to obtain the **NIC-X710_X722_XL710_XXV710-CentOS7.6-i40e-2.15.9-1-x86_64.rpm**, **RAID-3008IR_3008IT_3408IT_3416IT-CentOS7.6-mpt3sas-27.00.00.00-1-x86_64.rpm**, and **RAID-3004iMR_3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-1-x86_64.rpm** files.

      The **NIC-X710_X722_XL710_XXV710-CentOS7.6-i40e-2.15.9-1-x86_64.rpm**, **RAID-3008IR_3008IT_3408IT_3416IT-CentOS7.6-mpt3sas-27.00.00.00-1-x86_64.rpm**, and **RAID-3004iMR_3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-1-x86_64.rpm** files are used to install LOM drivers, mpt3 drivers, and megaraid_sas drivers of V5 servers, respectively.

   -  EulerOS 2.8 ARM

      Download and decompress the **TaiShanServer iDriver-EulerOS2.8-Driver-V103.zip** driver package to obtain **onboard_driver_EulerOS2.8.iso**. Decompress **onboard_driver_EulerOS2.8.iso** to **obtain NIC-IN200-EulerOS2.8-hinic-2.4.1.0-aarch64.rpm**, which is used to install the Hi1822 standard card driver. However, the Hi1822 driver has been installed in :ref:`Installing the Hi1822 Driver <en-us_topic_0197320063>`. Therefore, you can skip this step.

   -  CentOS 7.6 ARM

      Download and decompress the **TaiShanServer iDriver-CentOS7.6-Driver-V112.zip** driver package to obtain **onboard_driver_CentOS7.6.iso**. Decompress the **onboard_driver_CentOS7.6.iso** file to obtain the **RAID-3108_3408iMR_3416iMR_3508_3516-CentOS7.6-megaraid_sas-07.716.01.00-aarch64.rpm** and **NIC-Hi1822-CentOS7.6-hinic-3.9.0.8-aarch64.rpm** files for installing the megaraid_sas and Hi1822 drivers. The Hi1822 (hinic) driver has been installed in :ref:`Installing the Hi1822 Driver <en-us_topic_0197320063>`. Therefore, you do not need to install it again.
