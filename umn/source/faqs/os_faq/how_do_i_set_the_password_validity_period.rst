:original_name: en-us_topic_0079122353.html

.. _en-us_topic_0079122353:

How Do I Set the Password Validity Period?
==========================================

If you cannot log in to a BMS due to password expiry, contact the operation administrator.

If you can log in to the BMS, perform the following operations to set the password validity period:

#. .. _en-us_topic_0079122353__li96511055152412:

   Log in to the BMS OS and run the following command to query the password validity period:

   **vi /etc/login.defs**

   The value of parameter **PASS_MAX_DAYS** indicates the password validity period.

#. Run the following command to change the value of parameter **PASS_MAX_DAYS** in :ref:`1 <en-us_topic_0079122353__li96511055152412>`:

   **chage -M** *99999 user_name*

   *99999* is the validity period of the password, and *user_name* is a system user.

   You are advised to set the password validity period as needed and change it on a regular basis.

#. Run **vi /etc/login.defs** to verify that the configuration has taken effect.


   .. figure:: /_static/images/en-us_image_0284616148.png
      :alt: **Figure 1** Configuration verification

      **Figure 1** Configuration verification
