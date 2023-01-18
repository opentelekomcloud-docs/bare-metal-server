:original_name: en-us_topic_0081116781.html

.. _en-us_topic_0081116781:

Red Hat 6/CentOS 6/Oracle Linux 6
=================================

#. Run the following command:

   **chkconfig --list \| grep cloud**

   As shown in the following figure, **on** indicates that automatic startup has been enabled for the service.

   |image1|

#. If automatic startup is not enabled for Cloud-Init services, run the following commands to enable it:

   **chkconfig cloud-init on**

   **chkconfig cloud-init-local on**

   **chkconfig cloud-config on**

   **chkconfig cloud-final on**

.. |image1| image:: /_static/images/en-us_image_0110253618.png
