:original_name: en-us_topic_0126150310.html

.. _en-us_topic_0126150310:

Reinstalling the BMS OS
=======================

Function
--------

This API is used to reinstall the BMS OS. The OS of BMSs supporting quick provisioning can be reinstalled using the original image without any change to the data disks. Password and key pair injection are supported during OS reinstallation.

.. note::

   To check whether a BMS is quickly provisioned, use the :ref:`Querying Details About Flavors and Extended Flavor Information <en-us_topic_0131326852>` API.

   This is an asynchronous API. Calling the API successfully indicates that the task is delivered successfully. To check whether the task is successful, use the :ref:`Querying Task Statuses <en-us_topic_0118696596>` API.

Constraints
-----------

-  For BMSs created from private images, ensure that Cloud-Init (for Linux) or Cloudbase-Init (for Windows) has been installed for the image. If an image without Cloud-Init or Cloudbase-Init is used, this API cannot inject a key pair or password. Cloud-Init or Cloudbase-Init has been installed for public images by default.
-  You are not allowed to perform other operations when reinstalling the OS. Otherwise, reinstalling the OS will fail.
-  You can reinstall the OS only on a BMS that is stopped or for which OS reinstallation has failed.
-  An encrypted password will be used as the value of **user_data** for Linux images.

URI
---

POST /v1/{project_id}/baremetalservers/{server_id}/reinstallos

:ref:`Table 1 <en-us_topic_0126150310__table55945983>` lists the parameters.

.. _en-us_topic_0126150310__table55945983:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                            |
   +=======================+=======================+========================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                              |
   |                       |                       |                                                                                                                                        |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`.                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                  |
   |                       |                       |                                                                                                                                        |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the :ref:`Querying BMSs (Native OpenStack API) <en-us_topic_0053158693>`. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +--------------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Mandatory | Type   | Description                                                                                                                  |
   +==============+===========+========+==============================================================================================================================+
   | os-reinstall | Yes       | Object | Specifies the operation of reinstalling the BMS OS. For details, see :ref:`Table 2 <en-us_topic_0126150310__table32200631>`. |
   +--------------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0126150310__table32200631:

   .. table:: **Table 2** **os-reinstall** field data structure description

      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                     |
      +=================+=================+=================+=================================================================================================================================================================================================================================================================+
      | adminpass       | No              | String          | Specifies the initial login password of the BMS administrator account.                                                                                                                                                                                          |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 | The Linux administrator is **root**, and the Windows administrator is **Administrator**.                                                                                                                                                                        |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 | Recommended password complexity requirements are as follows:                                                                                                                                                                                                    |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 | -  The password contains 8 to 26 characters.                                                                                                                                                                                                                    |
      |                 |                 |                 | -  Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters ``!@$%^-_=+[{}]:,./?``                                                                                                        |
      |                 |                 |                 | -  The password cannot contain the username or the username in reverse.                                                                                                                                                                                         |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 | .. note::                                                                                                                                                                                                                                                       |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 |    -  For Windows BMSs, the password cannot contain more than two consecutive characters in the username.                                                                                                                                                       |
      |                 |                 |                 |    -  For Linux BMSs, **user_data** can be used to inject a password. In this case, **adminpass** is invalid.                                                                                                                                                   |
      |                 |                 |                 |    -  Either **adminpass** or **keyname** can be set.                                                                                                                                                                                                           |
      |                 |                 |                 |    -  If both **adminpass** and **keyname** are empty, **user_data** in metadata must be set.                                                                                                                                                                   |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | keyname         | No              | String          | Specifies the key pair name.                                                                                                                                                                                                                                    |
      |                 |                 |                 |                                                                                                                                                                                                                                                                 |
      |                 |                 |                 | You can create a key pair using the :ref:`Creating and Importing an SSH Key Pair (Native OpenStack API) <en-us_topic_0060384660>` API, or query existing key pairs using the :ref:`Querying SSH Key Pairs (Native OpenStack API) <en-us_topic_0060384658>` API. |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | userid          | No              | String          | Specifies the user ID. You can obtain the user ID from **My Credential** on the management console.                                                                                                                                                             |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | metadata        | No              | Object          | Specifies the BMS metadata. For details, see :ref:`Table 3 <en-us_topic_0126150310__table9120223>`.                                                                                                                                                             |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0126150310__table9120223:

   .. table:: **Table 3** **metadata** field data structure description

      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                              |
      +=================+=================+=================+==========================================================================================================================================================+
      | BYOL            | No              | String          | Specifies whether a user has the license of an image.                                                                                                    |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | -  If this parameter is set to **true**, the license file delivered with the image is used, indicating that BYOL is used.                                |
      |                 |                 |                 | -  If this parameter is set to a value other than **true**, BYOL is not used, and the license file provided by the cloud platform must be used.          |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | The default value is not **true**, indicating that BYOL is not used.                                                                                     |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | user_data       | No              | String          | Specifies the Linux image root password injected during the BMS OS reinstallation. It is a user-defined initial password.                                |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | Note: The password change script must be encoded using Base64.                                                                                           |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | Recommended password complexity requirements are as follows:                                                                                             |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | -  Contains 8 to 26 characters.                                                                                                                          |
      |                 |                 |                 | -  Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters ``!@$%^-_=+[{}]:,./?`` |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | An example is as follows:                                                                                                                                |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | -  Use a plaintext password (risky in security), for example, **cloud.1234**.                                                                            |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |    ::                                                                                                                                                    |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |       #!/bin/bash                                                                                                                                        |
      |                 |                 |                 |       echo 'root:Cloud.1234' | chpasswd ;                                                                                                                |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | -  Use a password.                                                                                                                                       |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |    ::                                                                                                                                                    |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |       #!/bin/bash                                                                                                                                        |
      |                 |                 |                 |       echo 'root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig/GpOkLcOhab9smJoLKYm/Tf9Hcwa6DpiPDhdHfGEAPajFmLZa0YDd910' | chpasswd -e               |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | -  This script must be encoded using Base64.                                                                                                             |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | where, **$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig** is the ciphertext password, which can be generated as follows:                             |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | #. Generate an encrypted salt value.                                                                                                                     |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |    .. code:: console                                                                                                                                     |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |       [root@test linux]# python -c "import crypt, getpass, pwd;print crypt.mksalt()"                                                                     |
      |                 |                 |                 |       $6$V6azyeLwcD3CHlpY                                                                                                                                |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | #. Generate a ciphertext password based on the salt value.                                                                                               |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |    .. code:: console                                                                                                                                     |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 |       [root@test linux]# python -c "import crypt, getpass, pwd;print crypt.crypt('Cloud.1234','\$6\$V6azyeLwcD3CHlpY')"                                  |
      |                 |                 |                 |        $6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig/GpOkLcOhab9smJoLKYm/Tf9Hcwa6DpiPDhdHfGEAPajFmLZa0YDd910                                        |
      |                 |                 |                 |                                                                                                                                                          |
      |                 |                 |                 | #. After the ciphertext is generated, the password change script must be encoded using Base64.                                                           |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example request

   .. code-block:: text

      POST https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/cf2a8b97-b5c6-47ef-9714-eb27adf26e5b/reinstallos

   ::

      {
          "os-reinstall": {
              "keyname": "KeyPair-350b",
              "userid": "7e25b1da389f4697a79df3a0e5bd494e",
              "metadata": {
                    "user_data":  "IyEvYmluL2Jhc2gKZWNobyAncm9vdDokNiR0Y0pZamUkNGhhUHlNZFR4VWVHc2dTMWFmL1NsMm4vbXZzdy5wSFdjbTVBc084OWFhUFhGNXUvVnJ5OXJiYmZZSW45SmZac2k3SlRmd2Z6djJPbTBHRFZUZTd6RDEnIHwgY2hwYXNzd2QgLWU7"
              }
          }
      }

Response
--------

-  Response parameters

.. table:: **Table 4** Normal response

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================+
   | job_id                | String                | Specifies the task ID returned after a task command is issued. The task ID can be used to query the execution status of the task.         |
   |                       |                       |                                                                                                                                           |
   |                       |                       | For details about how to query the task execution status based on **job_id**, see :ref:`Querying Task Statuses <en-us_topic_0118696596>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 5** Abnormal response

   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Type                      | Description                                                                                                                                                |
   +===========+===========================+============================================================================================================================================================+
   | error     | Dictionary data structure | Specifies the error returned when a task submission encounters an exception. For details, see :ref:`Table 6 <en-us_topic_0126150310__table6409189311151>`. |
   +-----------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0126150310__table6409189311151:

.. table:: **Table 6** **error** data structure

   ========= ====== ============================
   Parameter Type   Description
   ========= ====== ============================
   message   String Specifies the error message.
   code      String Specifies the error code.
   ========= ====== ============================

Example Response
----------------

-  Normal response

.. code-block::

   {
       "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
   }

Returned Values
---------------

Normal values

=============== ============================================
Returned Values Description
=============== ============================================
200             The request has been successfully processed.
=============== ============================================

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
