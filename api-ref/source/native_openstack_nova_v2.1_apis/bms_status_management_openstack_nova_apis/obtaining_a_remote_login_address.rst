:original_name: en-us_topic_0000002340222796.html

.. _en-us_topic_0000002340222796:

Obtaining a Remote Login Address
================================

Function
--------

This API is used to obtain the address for remotely logging in to a BMS.

URL
---

POST /v2.1/{project_id}/servers/{server_id}/action

:ref:`Table 1 <en-us_topic_0000002340222796__en-us_topic_0108366160_table31631432103712>` lists the parameters.

.. _en-us_topic_0000002340222796__en-us_topic_0108366160_table31631432103712:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | server_id             | Yes                   | Specifies the BMS ID.                                                                                                                                 |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | You can obtain the BMS ID from the BMS console or by calling the API :ref:`Querying BMSs <en-us_topic_0000002340063012>`.                             |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Message
---------------

-  Request parameters

   +---------------------+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter           | Mandatory | Type   | Description                                                                                                                                                           |
   +=====================+===========+========+=======================================================================================================================================================================+
   | os-getSerialConsole | Yes       | Object | Specifies the action to obtain a BMS remote login address. For details, see :ref:`Table 2 <en-us_topic_0000002340222796__en-us_topic_0108366160_table3521155775514>`. |
   +---------------------+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0000002340222796__en-us_topic_0108366160_table3521155775514:

   .. table:: **Table 2** **os-getSerialConsole** data structure

      +-----------+-----------+--------+----------------------------------------------------+
      | Parameter | Mandatory | Type   | Description                                        |
      +===========+===========+========+====================================================+
      | type      | Yes       | String | Specifies the object. Set the value to **serial**. |
      +-----------+-----------+--------+----------------------------------------------------+

-  Example request

   Obtaining the remote login address of a BMS (ID: 47e9be4e-a7b9-471f-92d9-ffc83814e07a)

   .. code-block:: text

      POST https://{ECS Endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action

   ::

      {
          "os-getSerialConsole": {
              "type": "serial"
          }
      }

Response Message
----------------

-  Response parameters

   None

-  Example response

   ::

      {
          "console": {
              "url": "https://baremetal-consoleproxy.az1.dc1.domainname.com:8003/?token=040134bb-9195-4029-9a62-550bce390258",
              type": "serial"
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
