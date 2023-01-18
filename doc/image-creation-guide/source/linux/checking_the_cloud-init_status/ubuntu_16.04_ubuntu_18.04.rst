:original_name: en-us_topic_0081116732.html

.. _en-us_topic_0081116732:

Ubuntu 16.04/Ubuntu 18.04
=========================

#. .. _en-us_topic_0081116732__en-us_topic_0094568752_li17316337259:

   Run the following commands:

   **systemctl status cloud-init**

   **systemctl status cloud-init-local**

   **systemctl status cloud-config**

   **systemctl status cloud-final**

   As shown in the following figure, **enable** indicates that automatic startup has been enabled for the service.

   |image1|

#. If automatic startup is not enabled for Cloud-Init services, run the following commands to enable it:

   **systemctl enable cloud-init**

   **systemctl enable cloud-init-local**

   **systemctl enable cloud-config**

   **systemctl enable cloud-final**

#. Run the following commands to start Cloud-Init:

   **systemctl start cloud-init-local**

   **systemctl start cloud-init**

   **systemctl start cloud-config**

   **systemctl start cloud-final**

#. Run the commands in :ref:`1 <en-us_topic_0081116732__en-us_topic_0094568752_li17316337259>` to check whether the Cloud-Init status is **active**.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0110253665.png
.. |image2| image:: /_static/images/en-us_image_0000001379202056.png
