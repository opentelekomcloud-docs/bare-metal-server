:original_name: en-us_topic_0083745263.html

.. _en-us_topic_0083745263:

Cloud-Init
==========

What Is Cloud-Init?
-------------------

Cloud-Init is an open-source cloud initialization program, which initializes specific configurations, such as the host name, key, and user data, of a newly created BMS.

By default, Cloud-Init has been installed for all public images.

Impact on IMS
-------------

To ensure that BMSs you create using private images support customized configurations, you must install Cloud-Init or Cloudbase-Init when you create private images.

-  For Windows OSs, download and install Cloudbase-Init.
-  For Linux OSs, download and install Cloud-Init.

After Cloud-Init or Cloudbase-Init is installed in an image, Cloud-Init or Cloudbase-Init will automatically initialize the BMS that created from the image. For details about how to install Cloud-Init and Cloudbase-Init, see *Bare Metal Server Private Image Creation Guide*.

Impact on BMS
-------------

-  When you create a BMS, if Cloud-Init has been installed in the image you select, you can initialize the BMS by injecting customized configurations (such as the BMS login password) into it. For details, see :ref:`Injecting User Data <en-us_topic_0083737011>`.
-  For a BMS with Cloud-Init installed, you can view the BMS metadata and configure and manage the BMS. For more information, see :ref:`Retrieving Metadata <en-us_topic_0096279463>`.

Notes
-----

-  If Cloud-Init has been installed, enable DHCP in the VPC to which the BMS belongs.
-  If Cloud-Init has been installed, ensure that security group rules in the outbound direction meet the following requirements so that you can access the metadata service:

   -  Protocol: TCP
   -  Port Range: 80
   -  Destination: 169.254.0.0/16

   .. note::

      If you use the default security group rule in the outbound direction, the preceding requirements have been met. The default outbound security group rule is as follows:

      -  Protocol: ANY
      -  Port Range: ANY
      -  Destination: 0.0.0.0/16
