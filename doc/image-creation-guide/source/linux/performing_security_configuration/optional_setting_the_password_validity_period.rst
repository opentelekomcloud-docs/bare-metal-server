:original_name: en-us_topic_0000001194043100.html

.. _en-us_topic_0000001194043100:

(Optional) Setting the Password Validity Period
===============================================

#. Check the password validity period.

   **vi /etc/login.defs**

   The value of parameter **PASS_MAX_DAYS** is the password validity period.

#. Change the value of parameter **PASS_MAX_DAYS**.

   **chage -M** *99999 user_name*

   *99999* is the password validity period, and *user_name* is a system user.

   Configure the password validity period as needed and change it on a regular basis.

#. Run **vi /etc/login.defs** to verify that the configuration has taken effect.

   |image1|

.. |image1| image:: /_static/images/en-us_image_0285808887.png
