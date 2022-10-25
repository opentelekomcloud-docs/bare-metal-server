:original_name: en-us_topic_0060384661.html

.. _en-us_topic_0060384661:

Deleting an SSH Key Pair (Native OpenStack API)
===============================================

Function
--------

This interface is used to delete a specified SSH key pair based on the key pair name.

URI
---

DELETE /v2.1/{project_id}/os-keypairs/{keypair_name}

:ref:`Table 1 <en-us_topic_0060384661__table155384213575>` lists the parameters.

.. _en-us_topic_0060384661__table155384213575:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keypair_name          | Yes                   | Specifies the key pair name.                                                                                                                          |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the key pair name by calling the :ref:`Querying SSH Key Pairs (Native OpenStack API) <en-us_topic_0060384658>` API.                    |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   None

-  Example request

   .. code-block:: text

      DELETE https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs/keypair-test

Response
--------

N/A

Returned Values
---------------

Normal values

+-----------------+----------------------------------------------------------------------+
| Returned Values | Description                                                          |
+=================+======================================================================+
| 204             | The server has processed the request but did not return any content. |
+-----------------+----------------------------------------------------------------------+

For details about other returned values, see :ref:`Status Codes <en-us_topic_0053158690>`.

Error Codes
-----------

See :ref:`Error Codes <en-us_topic_0107541808>`.
