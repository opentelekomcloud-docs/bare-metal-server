:original_name: en-us_topic_0081116561.html

.. _en-us_topic_0081116561:

EulerOS/OpenEuler
=================

#. .. _en-us_topic_0081116561__en-us_topic_0094568894_li13637754115911:

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

#. Run the commands in :ref:`1 <en-us_topic_0081116561__en-us_topic_0094568894_li13637754115911>` to check whether the Cloud-Init status is **active**.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0110253555.png
.. |image2| image:: /_static/images/en-us_image_0000001379117300.png
