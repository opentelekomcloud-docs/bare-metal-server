:original_name: en-us_topic_0081116632.html

.. _en-us_topic_0081116632:

SUSE 12 SP2/SUSE 12 SP3/SUSE 15/Oracle Linux 7/Red Hat 7/CentOS 7/CentOS 8
==========================================================================

#. .. _en-us_topic_0081116632__en-us_topic_0094568857_li1344312814509:

   Check whether the Cloud-init services will automatically start when the system starts.

   **systemctl status cloud-init-local**

   **systemctl status cloud-init**

   **systemctl status cloud-config**

   **systemctl status cloud-final**

#. **enabled** indicates that the service will automatically start.

   |image1|

   Otherwise, run the following commands to enable automatic startup for them.

   **systemctl enable cloud-init-local**

   **systemctl enable cloud-init**

   **systemctl enable cloud-config**

   **systemctl enable cloud-final**

#. Run the following commands to start Cloud-Init:

   **systemctl start cloud-init-local**

   **systemctl start cloud-init**

   **systemctl start cloud-config**

   **systemctl start cloud-final**

#. Run the commands in :ref:`1 <en-us_topic_0081116632__en-us_topic_0094568857_li1344312814509>` to check whether the Cloud-Init status is **active**.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0110253503.png
.. |image2| image:: /_static/images/en-us_image_0000001429481705.png
