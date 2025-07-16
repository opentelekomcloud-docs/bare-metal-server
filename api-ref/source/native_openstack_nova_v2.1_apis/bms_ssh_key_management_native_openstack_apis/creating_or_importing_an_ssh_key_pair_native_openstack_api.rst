:original_name: en-us_topic_0000002340222820.html

.. _en-us_topic_0000002340222820:

Creating or Importing an SSH Key Pair (Native OpenStack API)
============================================================

Function
--------

This API is used to create an SSH key pair or import a public key to generate a key pair.

After an SSH key pair is generated, download the private key to a local directory. Then, you can use this private key to log in to the BMS. For BMS security purposes, a private key can be downloaded only once. Keep it secure.

URI
---

POST /v2.1/{project_id}/os-keypairs

:ref:`Table 1 <en-us_topic_0000002340222820__en-us_topic_0060384660_table137043339568>` lists the parameters.

.. _en-us_topic_0000002340222820__en-us_topic_0060384660_table137043339568:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. note::

   When creating an SSH key pair, you only need to configure **name**. When importing a public SSH key, you must also configure **public_key**.

+-----------+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Mandatory | Type   | Description                                                                                                                                                 |
+===========+===========+========+=============================================================================================================================================================+
| keypair   | Yes       | Object | Specifies the created or imported SSH key pair. For details, see :ref:`Table 2 <en-us_topic_0000002340222820__en-us_topic_0060384660_table44094886105534>`. |
+-----------+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002340222820__en-us_topic_0060384660_table44094886105534:

.. table:: **Table 2** **keypair** data structure

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                          |
   +=================+=================+=================+======================================================================================================================+
   | public_key      | No              | String          | Specifies the imported public key. The maximum size of the imported public key is 1024 bytes.                        |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | Note: If the length of the public key to be imported exceeds 1024 bytes, the public key import to the BMS will fail. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | name            | Yes             | String          | Specifies the key pair name.                                                                                         |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | The new key pair name cannot be the same as an existing one.                                                         |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+

Example Request
---------------

Creating or importing an SSH key pair (name: keypair-7d7c3650-dabe-4eb0-b904-5c464453c043) with the public key **ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC9mC3WZN9UGLxgPBpP7H5jZMc6pKwOoSgre8yun6REFktn/Kz7DUt9jaR1UJyRzHxITfCfAIgSxPdGqB/oF1suMyWgu5i0625vavLB5z5kC8Hq3qZJ9zJO1poE1kyD+htiTtPWJ88e12xuH2XB/CZN9OpEiF98hAagiOE0EnOS5Q== Generated by Nova\\n**

.. code-block:: text

   POST https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs

::

   {
       "keypair": {
           "name": "keypair-7d7c3650-dabe-4eb0-b904-5c464453c043",
           "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC9mC3WZN9UGLxgPBpP7H5jZMc6pKwOoSgre8yun6REFktn/Kz7DUt9jaR1UJyRzHxITfCfAIgSxPdGqB/oF1suMyWgu5i0625vavLB5z5kC8Hq3qZJ9zJO1poE1kyD+htiTtPWJ88e12xuH2XB/CZN9OpEiF98hAagiOE0EnOS5Q== Generated by Nova\n"
       }
   }

Response Parameters
-------------------

+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Type   | Description                                                                                                                             |
+===========+========+=========================================================================================================================================+
| keypair   | Object | Specifies the SSH key pair. For details, see :ref:`Table 3 <en-us_topic_0000002340222820__en-us_topic_0060384660_table11390225105534>`. |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002340222820__en-us_topic_0060384660_table11390225105534:

.. table:: **Table 3** **keypair** data structure

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                         |
   +=======================+=======================+=====================================================================================================+
   | fingerprint           | String                | Specifies fingerprint information about the key pair.                                               |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | name                  | String                | Specifies the key pair name.                                                                        |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | public_key            | String                | Specifies the public key.                                                                           |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | private_key           | String                | Specifies the private key.                                                                          |
   |                       |                       |                                                                                                     |
   |                       |                       | -  The information about the private key is contained in the response for creating an SSH key.      |
   |                       |                       | -  The information about the private key is not contained in the response for importing an SSH key. |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | user_id               | String                | Specifies the ID of the user owning the key pair.                                                   |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "keypair": {
           "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC9mC3WZN9UGLxgPBpP7H5jZMc6pKwOoSgre8yun6REFktn/Kz7DUt9jaR1UJyRzHxITfCfAIgSxPdGqB/oF1suMyWgu5i0625vavLB5z5kC8Hq3qZJ9zJO1poE1kyD+htiTtPWJ88e12xuH2XB/CZN9OpEiF98hAagiOE0EnOS5Q== Generated by Nova\n",
           "user_id": "f882feb345064e7d9392440a0f397c25",
           "name": "keypair-7d7c3650-dabe-4eb0-b904-5c464453c043",
           "fingerprint": "35:9d:d0:c3:4a:80:d3:d8:86:f1:ca:f7:df:c4:f9:d8"
       }
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
