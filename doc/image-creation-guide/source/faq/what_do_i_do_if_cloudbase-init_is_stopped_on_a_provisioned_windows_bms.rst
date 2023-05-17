:original_name: en-us_topic_0100601386.html

.. _en-us_topic_0100601386:

What Do I Do If Cloudbase-Init Is Stopped on a Provisioned Windows BMS?
=======================================================================

.. note::

   If you cannot log in to or perform operations on BMC, contact O&M administrators.

Symptom
-------

If Cloudbase-Init is stopped after a Windows BMS is provisioned, and information "Failed to find trace ID description from Cloudbase-Init because the component triggering the trace is not installed or has been damaged. You can install or recover the component." is displayed, you need to reinstall Cloudbase-Init.

Solution
--------

#. .. _en-us_topic_0100601386__en-us_topic_0094568819_lad720047c3cc4890aaa7cb995434aa91:

   Log in to the BMS using BMC and back up the .conf files in the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\** directory and all the files in the **LocalScripts** directory.

#. Download Cloudbase-Init from the official website.

   https://cloudbase.it/cloudbase-init/#download

#. Click **Remote Control** on the BMC host management page.

   The remote control window is displayed.

#. Click |image1| in the upper toolbar. Select **Directory** and click **Browse**.

   A dialog box is displayed.

#. Select the Cloudbase-Init package and click **Connect** to upload it to the BMS. The CD-ROM drive read and install the Cloudbase-Init.

#. Copy the files you backed up in step :ref:`1 <en-us_topic_0100601386__en-us_topic_0094568819_lad720047c3cc4890aaa7cb995434aa91>` to the new Cloudbase-Init directory.

#. Restart the BMS and check whether Cloudbase-Init runs properly.

.. |image1| image:: /_static/images/en-us_image_0094568749.png
