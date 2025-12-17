:original_name: en-us_topic_0129082263.html

.. _en-us_topic_0129082263:

Querying Details About BMSs
===========================

Function
--------

This API is used to query BMSs by filters and display details about the BMSs.

The information that can be queried includes the BMS billing mode and whether the BMS is frozen.

URI
---

GET /v1/{project_id}/baremetalservers/detail

:ref:`Table 1 <en-us_topic_0129082263__table32475667>` lists the parameters.

.. _en-us_topic_0129082263__table32475667:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                 |
   +=======================+=======================+=============================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                   |
   |                       |                       |                                                                                                             |
   |                       |                       | For details about how to obtain the project ID, see :ref:`Obtaining a Project ID <en-us_topic_0171277624>`. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================================================================================================================================================================================================================+
   | flavor          | No              | String          | Specifies the BMS flavor ID.                                                                                                                                                                                                                                                                                                              |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name            | No              | String          | Specifies the BMS name.                                                                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | status          | No              | String          | Specifies the BMS status.                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **ACTIVE**: Running, Stopping, Deleting                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 | -  **BUILD**: Creating                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **ERROR**: Faulty                                                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 | -  **HARD_REBOOT**: Forcibly Restarting                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 | -  **REBOOT**: Restarting                                                                                                                                                                                                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | Specifies the number of BMSs displayed on each page. The default value is **25** and the maximum value is **1000**.                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | offset          | No              | Integer         | This API is a pagination query API. **offset** indicates the page number (the start page number is **1**). The returned value contains the number of BMSs and details about the BMSs.                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  If **offset** is specified:                                                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |    BMSs are displayed by page based on the **limit** value. By default, the **limit** value is **1000**. The BMSs and total number of BMSs on the **offset** page are displayed. The maximum number of BMSs is the value of **limit**. If the number of BMSs is less than the value of **limit**, the actual number of BMSs is displayed. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  If **offset** is not specified:                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |    -  If **limit** is specified: The BMSs and total number of BMSs are displayed. The maximum number of BMSs is the value of **limit**. If the number of BMSs is less than the value of **limit**, the actual number of BMSs is displayed.                                                                                                |
   |                 |                 |                 |    -  If **limit** is not specified: 25 BMSs are displayed on each page. Details about the BMSs on the first page are displayed. If the number of BMSs is less than 25, the actual number of BMSs is displayed.                                                                                                                           |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | tags            | No              | String          | Specifies the BMS tag. The value can be:                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **\__type_baremetal**: internal tag of the system                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 | -  Other custom tags                                                                                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | reservation_id  | No              | String          | Specifies the reserved ID, which can be used to query BMSs created in a batch.                                                                                                                                                                                                                                                            |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Example Request
---------------

Querying BMSs bound to all enterprise projects of the user

.. code-block:: text

   GET https://{BMS Endpoint}/v1/bbf1946d374b44a0a2a95533562ba954/baremetalservers/detail?offset=1&limit=2&enterprise_project_id=all_granted_eps

Response Parameters
-------------------

+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                  |
+=======================+=======================+==============================================================================================================+
| servers               | List data structure   | Specifies details about BMSs. For details, see :ref:`Querying Details About a BMS <en-us_topic_0113746489>`. |
|                       |                       |                                                                                                              |
|                       |                       | The returned details vary depending on the query level.                                                      |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------+
| count                 | Integer               | Specifies the number of BMSs that match the filters.                                                         |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------+

Example Response
----------------

::

   {
       "count": 2,
       "servers": [
           {
               "id": "b544be62-1b3b-4982-ad98-572b002ac23b",
               "name": "bms-test1",
               "addresses": {
                   "5849fdf1-9d79-4589-80c2-fe557990c417": [
                       {
                           "version": "4",
                           "addr": "192.168.1.63",
                           "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:3a:8d:f1",
                           "OS-EXT-IPS:port_id": "c79d2813-94c9-4135-973e-cbf5d23e78e6",
                           "OS-EXT-IPS:type": "fixed"
                       }
                   ]
               },
               "flavor": {
                   "disk": "9309",
                   "vcpus": "32",
                   "ram": "193047",
                   "id": "physical.s1.medium.ondemand",
                   "name": "physical.s1.medium.ondemand"
               },
               "accessIPv4": "",
               "accessIPv6": "",
               "status": "ACTIVE",
               "progress": 0,
               "hostId": "cd243addb5d2c64e89218180b7a3ed95abe6882e81c337cc563137df",
               "updated": "2018-09-10T01:20:58Z",
               "created": "2018-09-06T09:29:27Z",
               "metadata": {
                   "baremetalPortIDList": "[c79d2813-94c9-4135-973e-cbf5d23e78e6]",
                   "chargingMode": "0"
               },
               "tags": [
                   "__type_baremetal"
               ],
               "description": "bms-test1",
               "locked": false,
               "config_drive": "",
               "tenant_id": "bbf1946d374b44a0a2a95533562ba954",
               "user_id": "0c50494c5816425eb05c40b5e81ab65a",
               "key_name": "$key_name",
               "OS-EXT-STS:power_state": 1,
               "OS-EXT-STS:vm_state": "active",
               "OS-EXT-SRV-ATTR:host": "bms.dc1",
               "OS-EXT-SRV-ATTR:instance_name": "instance-0014bdc2",
               "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova002@2",
               "OS-DCF:diskConfig": "MANUAL",
               "OS-EXT-AZ:availability_zone": "az-dc-1",
               "os:scheduler_hints": {},
               "OS-EXT-SRV-ATTR:root_device_name": "/dev/vda",
               "OS-EXT-SRV-ATTR:ramdisk_id": "",
               "enterprise_project_id": "0",
               "OS-SRV-USG:launched_at": "2018-09-06T09:30:36.000000",
               "OS-EXT-SRV-ATTR:kernel_id": "",
               "OS-EXT-SRV-ATTR:launch_index": 0,
               "host_status": "UP",
               "OS-EXT-SRV-ATTR:reservation_id": "r-qjad3fv0",
               "OS-EXT-SRV-ATTR:hostname": "bms-test1",
               "sys_tags": [
                   {
                       "key": "_sys_enterprise_project_id",
                       "value": "0"
                   }
               ]
           },
           {
               "id": "a1541cfc-8ac3-43e9-a70d-b8d4b395b256",
               "name": "bms_test2",
               "addresses": {
                   "5849fdf1-9d79-4589-80c2-fe557990c417": [
                       {
                           "version": "4",
                           "addr": "192.168.1.50",
                           "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8f:38:2c",
                           "OS-EXT-IPS:port_id": "460aa585-9f83-4719-9527-fc39ebaca9aa",
                           "OS-EXT-IPS:type": "fixed"
                       }
                   ]
               },
               "flavor": {
                   "disk": "9309",
                   "vcpus": "32",
                   "ram": "193047",
                   "id": "physical.s1.medium",
                   "name": "physical.s1.medium"
               },
               "accessIPv4": "",
               "accessIPv6": "",
               "status": "SHUTOFF",
               "hostId": "cd243addb5d2c64e89218180b7a3ed95abe6882e81c337cc563137df",
               "updated": "2018-09-06T10:00:25Z",
               "created": "2018-08-30T12:40:47Z",
               "metadata": {
                   "metering.order_id": "CS18083020422CNV9",
                   "baremetalPortIDList": "[460aa585-9f83-4719-9527-fc39ebaca9aa]",
                   "metering.product_id": "00301-167001-0--0",
                   "chargingMode": "1"
               },
               "tags": [
                   "__type_baremetal",
                   "_sys_enterprise_project_id=9dd1131d-71fd-40fe-8f14-3fe6b6b5ef8b",
                   "key1=value1",
                   "three=3",
                   "two=2"
               ],
               "description": "bms_test2",
               "locked": false,
               "config_drive": "",
               "tenant_id": "bbf1946d374b44a0a2a95533562ba954",
               "user_id": "3fc5ab2b0c544979abcaafd86edd80e6",
               "key_name": "$key_name",
               "OS-EXT-STS:power_state": 4,
               "OS-EXT-STS:vm_state": "stopped",
               "OS-EXT-SRV-ATTR:host": "bms.dc1",
               "OS-EXT-SRV-ATTR:instance_name": "instance-0014581b",
               "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova002@2",
               "OS-DCF:diskConfig": "MANUAL",
               "OS-EXT-AZ:availability_zone": "az-dc-1",
               "os:scheduler_hints": {},
               "OS-EXT-SRV-ATTR:root_device_name": "/dev/vda",
               "OS-EXT-SRV-ATTR:ramdisk_id": "",
               "enterprise_project_id": "0",
               "OS-SRV-USG:launched_at": "2018-08-30T12:42:10.000000",
               "OS-EXT-SRV-ATTR:kernel_id": "",
               "OS-EXT-SRV-ATTR:launch_index": 0,
               "host_status": "UP",
               "OS-EXT-SRV-ATTR:reservation_id": "r-i5w3yc9a",
               "OS-EXT-SRV-ATTR:hostname": "bms-test2",
               "sys_tags": [
                   {
                       "key": "_sys_enterprise_project_id",
                       "value": "0"
                   }]
           }
       ]
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
