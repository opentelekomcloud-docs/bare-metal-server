:original_name: en-us_topic_0083745257.html

.. _en-us_topic_0083745257:

Overview
========

What Is an Image?
-----------------

An image is a template of the BMS running environment. It contains an OS and runtime environment, and some pre-installed applications. An image file is equivalent to a copy file that contains all data in the system disk.

Image Types
-----------

Images can be classified into public images, private images, and shared images.

.. table:: **Table 1** Image types

   +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Image Type    | Description                                                                                                                                                                                                                                                        |
   +===============+====================================================================================================================================================================================================================================================================+
   | Public image  | A public image is provided by the cloud platform and is available to all users. It contains an OS and preinstalled public applications.                                                                                                                            |
   +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Private image | A private image is created by a user and is available only to the user who created it. It contains an OS, pre-installed public applications, and the user's private applications. Using a private image to create BMSs frees you from repeatedly configuring BMSs. |
   +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Shared image  | A shared image is a private image other users share with you.                                                                                                                                                                                                      |
   +---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Public Images
-------------

Public images are provided by the system. These images are available to all users, compatible with BMSs and most mainstream OSs, and are pre-installed with necessary plug-ins. Public images available to you vary depending on the BMS flavor you selected. For details, see :ref:`OSs Supported by Different Types of BMSs <en-us_topic_0263802108>`.

**Characteristics**

-  OS types: Linux and Windows OSs that are updated and maintained periodically
-  Pre-installed software: plug-ins that BMS storage, networks, and basic functions depend on

   .. caution::

      These plug-ins are necessary for BMSs to run properly. Do not delete or modify any of them. Otherwise, basic BMS functions will be affected.

   .. table:: **Table 2** Pre-installed software

      +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Software                         | Description                                                                                                                                                              |
      +==================================+==========================================================================================================================================================================+
      | Cloud-Init                       | Cloud-Init is an open-source cloud initialization program, which initializes specific configurations, such as the host name, key, and user data, of a newly created BMS. |
      +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | bms-network-config               | This plug-in is used to automatically configure BMS networks during BMS provisioning and restore the BMS network when the network is interrupted due to faults.          |
      +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | SDI iNIC frontend driver plug-in | This plug-in is installed in the image so that EVS disks can be attached to BMSs. In this way, BMSs can be booted from EVS disks, facilitating quick BMS provisioning.   |
      +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Compatibility: compatible with server hardware
-  Security: highly stable and licensed
-  Restrictions: no restrictions on usage

Private Images
--------------

A private image contains an OS, preinstalled public applications, and a user's private applications. You can use a private image to create BMSs without having to repeatedly configure them.

**Characteristics**

-  Compatibility: Private images can be used to deploy servers that are of the same model as the source BMS and may fail to deploy servers of other models.
-  Functions: You can create and delete private images, as well as create BMSs and reinstall the BMS OS using private images.
-  Restrictions: You can create a maximum of 50 private images.

Shared Images
-------------

A shared image is a private image other users share with you.

Application Scenarios
---------------------

-  Deploying software environments in a batch

   Prepare a BMS with an OS, the partition arrangement you prefer, and software installed to create a private image. You can use the image to create batch clones of your custom BMS.

-  Backing up a BMS

   Create an image from a BMS to back up the BMS. If the software of the BMS becomes faulty, you can use the image to restore the BMS.
