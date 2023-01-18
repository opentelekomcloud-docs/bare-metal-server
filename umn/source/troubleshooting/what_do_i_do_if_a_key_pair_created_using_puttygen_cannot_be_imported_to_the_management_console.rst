:original_name: en-us_topic_0084166750.html

.. _en-us_topic_0084166750:

What Do I Do If a Key Pair Created Using PuTTYgen Cannot Be Imported to the Management Console?
===============================================================================================

Symptom
-------

When a key pair created using PuTTYgen was imported to the management console, the system displayed a message indicating that importing the public key failed.

Possible Causes
---------------

The format of the public key content does not meet system requirements.

Storing a public key by clicking **Save public key** of PuTTYgen will change the format of the public key content. Such a key cannot be imported to the management console.

Solution
--------

Use the locally stored private key and **PuTTY Key Generator** to restore the format of the public key content. Then, import the public key to the management console.

#. Double-click **puttygen.exe**. The **PuTTY Key Generator** window is displayed.


   .. figure:: /_static/images/en-us_image_0157339711.png
      :alt: **Figure 1** PuTTY Key Generator

      **Figure 1** PuTTY Key Generator

#. Click **Load** and select the private key.

   The system automatically loads the private key and restores the format of the public key content in **PuTTY Key Generator**. The content in the red box in :ref:`Figure 2 <en-us_topic_0084166750__fig184661439153519>` is the public key with the format meeting system requirements.

   .. _en-us_topic_0084166750__fig184661439153519:

   .. figure:: /_static/images/en-us_image_0157361001.png
      :alt: **Figure 2** Restoring the format of the public key content

      **Figure 2** Restoring the format of the public key content

#. Copy the public key content to a .txt file and save the file in a local directory.

#. Import the public key to the management console.

   a. Log in to the management console.

   b. Under **Computing**, click **Bare Metal Server**.

      The BMS console is displayed.

   c. In the navigation tree, choose **Key Pair**.

   d. On the right side of the page, click **Import Key Pair**.

   e. Copy the public key content in the .txt file to **Public Key Content** and click **OK**.
