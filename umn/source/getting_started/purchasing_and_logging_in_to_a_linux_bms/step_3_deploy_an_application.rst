:original_name: en-us_topic_0083745261.html

.. _en-us_topic_0083745261:

Step 3: Deploy an Application
=============================

This section describes how to deploy an application on a BMS.

Install and Start Nginx
-----------------------

#. Run the **yum install nginx** command to install Nginx and enter **y** as prompted.

   If the information shown in the following figure is displayed, Nginx is installed successfully.

   |image1|

#. Enter **systemctl start nginx.service** to start Nginx.

   .. note::

      This command applies to CentOS 7.4 64-bit, which is used as an example.

#. Enter **wget http://127.0.0.1** to test Nginx.

   |image2|

Access the Default Web Page
---------------------------

Open a browser and enter http://*BMS EIP* in the address box. If the Nginx welcome page is displayed, Nginx is installed successfully.

.. |image1| image:: /_static/images/en-us_image_0177728508.png
.. |image2| image:: /_static/images/en-us_image_0177729189.png
