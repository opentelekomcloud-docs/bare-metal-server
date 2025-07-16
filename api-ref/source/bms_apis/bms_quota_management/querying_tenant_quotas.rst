:original_name: en-us_topic_0131920833.html

.. _en-us_topic_0131920833:

Querying Tenant Quotas
======================

Function
--------

This API is used to query the quotas of all resources for a specified tenant, including used quotas.

URI
---

GET /v1/{project_id}/baremetalservers/limits

:ref:`Table 1 <en-us_topic_0131920833__table23262209>` lists the parameters.

.. _en-us_topic_0131920833__table23262209:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                   |
   |                       |                       |                                                                                                             |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying the quotas of a tenant (project ID: bbf1946d374b44a0a2a95533562ba954)

.. code-block:: text

   GET https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/limits

Response Parameters
-------------------

+-----------+--------+--------------------------------------------------------------------------------------------------+
| Parameter | Type   | Description                                                                                      |
+===========+========+==================================================================================================+
| absolute  | Object | Specifies tenant quotas. For details, see :ref:`Table 2 <en-us_topic_0131920833__table7714075>`. |
+-----------+--------+--------------------------------------------------------------------------------------------------+

.. note::

   Value **-1** indicates that the quantity is unlimited.

.. _en-us_topic_0131920833__table7714075:

.. table:: **Table 2** **absolute** data structure

   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | Parameter               | Type                  | Description                                                                                      |
   +=========================+=======================+==================================================================================================+
   | maxTotalInstances       | Integer               | Specifies the maximum number of BMSs you can create.                                             |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxTotalCores           | Integer               | Specifies the maximum number of CPU cores you can use.                                           |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxTotalRAMSize         | Integer               | Specifies the maximum memory (MB) you can use.                                                   |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxTotalKeypairs        | Integer               | Specifies the maximum number of SSH key pairs you can use.                                       |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxServerMeta           | Integer               | Specifies the maximum length of the metadata you can use.                                        |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxServerGroups         | Integer               | Specifies the maximum number of server groups.                                                   |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxServerGroupMembers   | Integer               | Specifies the maximum number of BMSs in a server group.                                          |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalServerGroupsUsed   | Integer               | Specifies the number of used server groups.                                                      |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxSecurityGroups       | Integer               | Specifies the maximum number of security groups you can use.                                     |
   |                         |                       |                                                                                                  |
   |                         |                       | .. note::                                                                                        |
   |                         |                       |                                                                                                  |
   |                         |                       |    The quota limit complies with the VPC quota limit.                                            |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxSecurityGroupRules   | Integer               | Specifies the maximum number of security group rules that you can configure in a security group. |
   |                         |                       |                                                                                                  |
   |                         |                       | .. note::                                                                                        |
   |                         |                       |                                                                                                  |
   |                         |                       |    The quota limit complies with the VPC quota limit.                                            |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxTotalFloatingIps     | Integer               | Specifies the maximum number of EIPs you can use.                                                |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | maxImageMeta            | Integer               | Specifies the maximum length of the image metadata.                                              |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalInstancesUsed      | Integer               | Specifies the number of the used BMSs.                                                           |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalCoresUsed          | Integer               | Specifies the number of used CPU cores.                                                          |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalRAMUsed            | Integer               | Specifies the used memory (MB).                                                                  |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalSecurityGroupsUsed | Integer               | Specifies the number of used security groups.                                                    |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | totalFloatingIpsUsed    | Integer               | Specifies the number of used EIPs.                                                               |
   +-------------------------+-----------------------+--------------------------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "absolute": {
           "maxServerMeta": 128,
           "maxPersonality": 5,
           "maxImageMeta": 128,
           "maxPersonalitySize": 10240,
           "maxSecurityGroupRules": 20,
           "maxTotalKeypairs": 100,
           "totalRAMUsed": 799836,
           "totalInstancesUsed": 21,
           "maxSecurityGroups": 10,
           "totalFloatingIpsUsed": 0,
           "maxTotalCores": -1,
           "totalSecurityGroupsUsed": 1,
           "maxTotalFloatingIps": 10,
           "maxTotalInstances": 100,
           "totalCoresUsed": 148,
           "maxTotalRAMSize": -1,
           "maxServerGroups": -1,
           "maxServerGroupMembers": -1,
           "totalServerGroupsUsed": 1
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
