:original_name: en-us_topic_0053158679.html

.. _en-us_topic_0053158679:

Querying Details About BMSs (Native OpenStack API)
==================================================

Function
--------

This API is used to query details about BMSs.

Constraints
-----------

-  The query result returned by this interface includes both ECS and BMS details. You need to filter out the BMS details using the flavor used to create the BMSs or the tags added to the BMSs during BMS creation.
-  If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.

URI
---

GET /v2.1/{project_id}/servers/detail{?changes-since={changes-since}&image={image}&flavor={flavor}&name={name}&status={status}&limit={limit}&marker={marker}&tags={tags}&not-tags={not-tags}&reservation_id={reservation_id}&sort_key={sort_key}&sort_dir={sort_dir}}

:ref:`Table 1 <en-us_topic_0053158679__table0524112565>` lists the parameters.

.. _en-us_topic_0053158679__table0524112565:

.. table:: **Table 1** Parameter description

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Mandatory             | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | project_id            | Yes                   | Specifies the project ID.                                                                                                                             |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | For how to obtain the project ID, see `Obtaining Required Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Request
-------

-  Request parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================================================================================================================================================================================================================+
   | changes-since   | No              | String          | Specifies the timestamp of the last BMS status update. The parameter is in ISO 8601 time format, for example, **2013-06-09T06:42:18Z**.                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | image           | No              | String          | Specifies the image ID.                                                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    If the image is used as the search criteria, other search criteria and pagination criteria are not supported. If both the image and other search criteria are used, the BMS details are filtered out by image. If the image is not used as the search criteria, this interface has no restrictions.                                                                                 |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flavor          | No              | String          | Specifies the flavor ID.                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | You can obtain the flavor ID from the BMS console or using the :ref:`Querying BMS Flavors (Native OpenStack API) <en-us_topic_0053158684>` API.                                                                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name            | No              | String          | Specifies the BMS name. This parameter supports fuzzy matching.                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | For example, the regular expression **?name=bob** will return both **bob** and **bobb**. To obtain only **bob**, you can use a regular expression matching the basic database syntax, such as MySQL or PostgreSQL (official website: https://www.postgresql.org/docs/9.2/static/functions-matching.html).                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | status          | No              | String          | Specifies the BMS status.                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **ACTIVE**: Running, Stopping, Deleting                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **BUILD**: Creating                                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ERROR**: Faulty                                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 | -  **HARD_REBOOT**: Forcibly Restarting                                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 | -  **REBOOT**: Restarting                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **DELETED**: Deleted                                                                                                                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | Specifies the number of BMSs displayed on each page.                                                                                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | marker          | No              | String          | Specifies the BMS ID to which the marker corresponds. The query will start from the next ID.                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | tags            | No              | String          | Queries the BMSs with specified tags.                                                                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | not-tags        | No              | String          | Queries the BMSs with tags not containing the specified value. The value is a list of tag keys.                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |    For example, an existing tag is **a.b**. After the tag function upgrade, query the tag using "not-tags=a".                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | reservation_id  | No              | String          | Specifies the reserved ID, which can be used to query BMSs created in a batch.                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Added in micro version 2.26.                                                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_key        | No              | String          | Specifies the BMS sorting attribute, which can be the BMS UUID (**uuid**), BMS status (**vm_state**), BMS name (**display_name**), BMS task status (**task_state**), power status (**power_state**), creation time (**created_at**), last time when the BMS is updated (**updated_at**), and AZ (**availability_zone**). You can specify multiple **sort_key** and **sort_dir** pairs. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | The default sorting is the reverse order by **created_at**.                                                                                                                                                                                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | sort_dir        | No              | String          | Specifies the sorting direction.                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **asc**: The query results are displayed in ascending order.                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **desc** (default value): The query results are displayed in descending order.                                                                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Example request

   -  With no optional parameter

      ::

         https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail

   -  With an optional parameter

      ::

         https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail?tags=__type_baremetal

   -  With multiple optional parameters

      ::

         https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/detail?tags=__type_baremetal&name=bms-test01

Response
--------

-  Response parameters

   +-----------+------------------+----------------------------------------------------------------------------------------------------------+
   | Parameter | Type             | Description                                                                                              |
   +===========+==================+==========================================================================================================+
   | servers   | Array of objects | Specifies details about the BMS. For details, see :ref:`Table 2 <en-us_topic_0053158707__table6149040>`. |
   +-----------+------------------+----------------------------------------------------------------------------------------------------------+

-  Example response

   ::

      {
          "servers": [
      {
                  "tenant_id": "c685484a8cc2416b97260938705deb64",
                  "addresses": {
                      "08a7715f-7de6-4ff9-a343-95ba4209f24a": [
      {
                              "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:0e:c4:77",
                              "OS-EXT-IPS:type": "fixed",
                              "addr": "192.168.0.107",
                              "version": 4
                          }
                      ]
                  },
                  "metadata": {
                      "op_svc_userid": "1311c433dd9b408886f57d695c229cbe"
                  },
                  "OS-EXT-STS:task_state": null,
                  "OS-DCF:diskConfig": "MANUAL",
                  "OS-EXT-AZ:availability_zone": "az-dc-1",
                  "links": [
      {
                          "rel": "self",
                          "href": "https://openstack.example.com/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                      },
      {
                          "rel": "bookmark",
                          "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd"
                          }
                  ],
                  "OS-EXT-STS:power_state": 1,
                  "id": "95bf2490-5428-432c-ad9b-5e3406f869dd",
                  "os-extended-volumes:volumes_attached": [
      {
                          "id": "dfa375b5-9856-44ad-a937-a4802b6434c3"
                      },
      {
                          "id": "bb9f1b27-843b-4561-b62e-ca18eeaec417"
                      },
      {
                          "id": "86e801c3-acc6-465d-890c-d43ba493f553"
                      },
      {
                          "id": "0994d3ac-3c6a-495c-a439-c597a4f08fa6"
                          }
                  ],
                  "OS-EXT-SRV-ATTR:host": "bms.az1",
                  "image": {
                      "links": [
      {
                              "rel": "bookmark",
                              "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/images/1a6635d8-afea-4f2b-abb6-27a202bad319"
                          }
                      ],
                      "id": "1a6635d8-afea-4f2b-abb6-27a202bad319"
                  },
                  "OS-SRV-USG:terminated_at": null,
                  "accessIPv4": "",
                  "accessIPv6": "",
                  "created": "2017-05-24T06:14:05Z",
                  "hostId": "e9c3ee0fcc58ab6085cf30df70b5544eab958858fb50d925f023e53e",
                  "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova004@2",
                  "key_name": "KeyPair-JX",
                  "flavor": {
                      "links": [
      {
                              "rel": "bookmark",
                              "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.83.medium"
                          }
                      ],
                      "id": "physical.83.medium"
                  },
                  "security_groups": [
      {
                          "name": "0011b620-4982-42e4-ad12-47c95ca495c4"
                          }
                  ],
                  "config_drive": "",
                  "OS-EXT-STS:vm_state": "active",
                  "OS-EXT-SRV-ATTR:instance_name": "instance-0000ebd3",
                  "user_id": "1311c433dd9b408886f57d695c229cbe",
                  "name": "bms",
                  "progress": 0,
                  "OS-SRV-USG:launched_at": "2017-05-25T03:40:25.066078",
                  "updated": "2017-05-25T03:40:25Z",
                  "status": "ACTIVE"
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
