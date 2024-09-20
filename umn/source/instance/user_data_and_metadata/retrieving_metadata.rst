:original_name: en-us_topic_0096279463.html

.. _en-us_topic_0096279463:

Retrieving Metadata
===================

Introduction
------------

The BMS metadata includes BMS basic information on the cloud platform, such as the BMS ID, hostname, and network information. The BMS metadata can be retrieved using compatible OpenStack and EC2 APIs listed in :ref:`Table 1 <en-us_topic_0096279463__en-us_topic_0042400609_table273552371680>`.

.. _en-us_topic_0096279463__en-us_topic_0042400609_table273552371680:

.. table:: **Table 1** BMS metadata types

   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Metadata Type         | Metadata Item                          | Description                                                                                                                                                      |
   +=======================+========================================+==================================================================================================================================================================+
   | OpenStack type        | /meta_data.json                        | This interface is used to query BMS metadata.                                                                                                                    |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | For the key fields in the BMS metadata, see :ref:`Table 2 <en-us_topic_0096279463__table2373623012315>`.                                                         |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /password                              | This interface is used to query the BMS password.                                                                                                                |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | If a key pair is selected during the creation of a Windows BMS, Cloudbase-Init is used to save the ciphertext password when the BMS is initialized.              |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /user_data                             | This interface is used to query BMS user data.                                                                                                                   |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | This metadata allows you to specify scripts and configuration files for initializing BMSs. For details, see :ref:`Injecting User Data <en-us_topic_0083737011>`. |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | For password-authenticated Linux BMSs, save the password injection script.                                                                                       |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /network_data.json                     | This interface is used to query network information of a BMS.                                                                                                    |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /securitykey                           | This interface is used to obtain temporary security credentials: Access Key ID (AK) and Secret Access Key (SK).                                                  |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | Before obtaining temporary AK/SK on a BMS, you need to create an agency for BMS on IAM and assign required resource permissions to BMS.                          |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | EC2 type              | /meta-data/hostname                    | This interface is used to query the host name of a BMS.                                                                                                          |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | To remove the suffix **.novalocal** from a BMS, see:                                                                                                             |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | :ref:`Is the BMS Host Name with Suffix novalocal Normal? <en-us_topic_0166937671>`                                                                               |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/instance-type               | This interface is used to query the flavor name of a BMS.                                                                                                        |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/local-ipv4                  | This interface is used to query the fixed IP address of a BMS.                                                                                                   |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | If there are multiple NICs, only the IP address of the primary NIC is displayed.                                                                                 |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/placement/availability-zone | This interface is used to query AZ information about a BMS.                                                                                                      |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/public-ipv4                 | This interface is used to query the EIP of a BMS.                                                                                                                |
   |                       |                                        |                                                                                                                                                                  |
   |                       |                                        | If there are multiple NICs, only the EIP of the primary NIC is displayed.                                                                                        |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/public-keys/0/openssh-key   | This interface is used to query the public key of a BMS.                                                                                                         |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /user-data                             | This interface is used to query BMS user data.                                                                                                                   |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                       | /meta-data/security-groups             | This interface is used to query the name of the security group of the BMS.                                                                                       |
   +-----------------------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0096279463__table2373623012315:

.. table:: **Table 2** Metadata key fields

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                         |
   +=======================+=======================+=====================================================================================+
   | uuid                  | String                | Specifies the BMS ID.                                                               |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+
   | availability_zone     | String                | Specifies the AZ where the BMS is located.                                          |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+
   | meta                  | Dict                  | Specifies the metadata information, including the image name, image ID, and VPC ID. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+
   | hostname              | String                | Specifies the hostname of the BMS.                                                  |
   |                       |                       |                                                                                     |
   |                       |                       | To remove the suffix **.novalocal** from a BMS, see:                                |
   |                       |                       |                                                                                     |
   |                       |                       | :ref:`Is the BMS Host Name with Suffix novalocal Normal? <en-us_topic_0166937671>`  |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+
   | vpc_id                | String                | Specifies the ID of the VPC where the BMS is located.                               |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------+

The following describes the URI and methods of using the supported BMS metadata.

Prerequisites
-------------

-  You have logged in to the BMS.
-  Security group rules in the outbound direction meet the following requirements:

   -  Protocol: TCP
   -  Port Range: 80
   -  Remote End: 169.254.0.0/16

   .. note::

      If you use the default security group rules in the outbound direction, the preceding requirements are met, and the metadata can be accessed. The default outbound security group rule is as follows:

      -  Protocol: Any
      -  Port Range: Any
      -  Remote End: 0.0.0.0/16

Metadata (OpenStack Metadata API)
---------------------------------

This interface is used to query BMS metadata.

-  URI

   /169.254.169.254/openstack/latest/meta_data.json

-  Method

   Supports GET requests.

-  Example

   The following describes how to use the cURL tool to query the BMS metadata:

   **curl** **http://169.254.169.254/openstack/latest/meta_data.json**

   .. code-block::

      {
          "random_seed": "rEocCViRS+dNwlYdGIxJHUp+00poeUsAdBFkbPbYQTmpNwpoEb43k9z+96TyrekNKS+iLYDdRNy4kKGoNPEVBCc05Hg1TcDblAPfJwgJS1okqEtlcofUhKmL3K0fto+5KXEDU3GNuGwyZXjdVb9HQWU+E1jztAJjjqsahnU+g/tawABTVySLBKlAT8fMGax1mTGgArucn/WzDcy19DGioKPE7F8ILtSQ4Ww3VClK5VYB/h0x+4r7IVHrPmYX/bi1Yhm3Dc4rRYNaTjdOV5gUOsbO3oAeQkmKwQ/NO0N8qw5Ya4l8ZUW4tMav4mOsRySOOB35v0bvaJc6p+50DTbWNeX5A2MLiEhTP3vsPrmvk4LRF7CLz2J2TGIM14OoVBw7LARwmv9cz532zHki/c8tlhRzLmOTXh/wL36zFW10DeuReUGmxth7IGNmRMQKV6+miI78jm/KMPpgAdK3vwYF/GcelOFJD2HghMUUCeMbwYnvijLTejuBpwhJMNiHA/NvlEsxJDxqBCoss/Jfe+yCmUFyxovJ+L8oNkTzkmtCNzw3Ra0hiKchGhqK3BIeToV/kVx5DdF081xrEA+qyoM6CVyfJtEoz1zlRRyoo9bJ65Eg6JJd8dj1UCVsDqRY1pIjgzE/Mzsw6AaaCVhaMJL7u7YMVdyKzA6z65Xtvujz0Vo=",
          "uuid": "ca9e8b7c-f2be-4b6d-a639-f10b4d994d04",
          "availability_zone": "lt-test-1c",
          "hostname": "bms-ddd4-l00349281.novalocal",
          "launch_index": 0,
          "meta": {
              "metering.image_id": "3a64bd37-955e-40cd-ab9e-129db56bc05d",
              "metering.imagetype": "gold",
              "metering.resourcespeccode": "physical.s3.small",
              "metering.cloudServiceType": "service.type.ec2",
              "image_name": "CentOS 7.6 64bit",
              "os_bit": "64",
              "vpc_id": "3b6c201f-aeb3-4bce-b841-64756e66cb49",
              "metering.resourcetype": "1",
              "cascaded.instance_extrainfo": "pcibridge:2",
              "os_type": "Linux",
              "charging_mode": "0"
          },
          "project_id": "6e8b0c94265645f39c5abbe63c4113c6",
          "name": "ecs-ddd4-l00349281"
      }

User Data (OpenStack Metadata API)
----------------------------------

This interface is used to query BMS user data. The value is configured when you create a BMS. It cannot be changed after the configuration.

-  URI

   /169.254.169.254/openstack/latest/user_data

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/openstack/latest/user_data**

   .. code-block::

      ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==

   .. note::

      If user data is not injected during BMS creation, the query result is 404.


      .. figure:: /_static/images/en-us_image_0166931790.png
         :alt: **Figure 1** 404 Not Found

         **Figure 1** 404 Not Found

Network Data (OpenStack Metadata API)
-------------------------------------

This interface is used to query network information of a BMS.

-  URI

   /openstack/latest/network_data.json

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/openstack/latest/network_data.json**

   .. code-block::

      {
          "services": [{
              "type": "dns",
              "address": "100.125.1.250"
          },
          {
              "type": "dns",
              "address": "100.125.21.250"
          }],
          "networks": [{
              "network_id": "67dc10ce-441f-4592-9a80-cc709f6436e7",
              "type": "ipv4_dhcp",
              "link": "tap68a9272d-71",
              "id": "network0"
          }],
          "links": [{
              "type": "cascading",
              "vif_id": "68a9272d-7152-4ae7-a138-3ef53af669e7",
              "ethernet_mac_address": "fa:16:3e:f7:c1:47",
              "id": "tap68a9272d-71",
              "mtu": null
          }]
      }

Security Key (OpenStack Metadata API)
-------------------------------------

This interface is used to obtain temporary security credentials: Access Key ID (AK) and Secret Access Key (SK).

.. note::

   -  To obtain temporary AK/SK on a BMS, you need to create an agency for BMS on IAM and assign required resource permissions to BMS.
   -  The temporary AK/SK pair expires an hour later but is updated 10 minutes ahead of the expiration time. During the 10 minutes, both the new and old temporary AK/SK pairs can be used.
   -  When using temporary AK/SK, add **'X-Security-Token':securitytoken** in the message header. **securitytoken** is the value returned when a call is made to the API.

-  URI

   /openstack/latest/securitykey

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/openstack/latest/securitykey**

User Data (EC2 Compatible API)
------------------------------

This interface is used to query BMS user data. The value is configured when you create a BMS. It cannot be changed after the configuration.

-  URI

   /169.254.169.254/latest/user-data

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/user-data**

   .. code-block::

      ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==

Hostname (EC2 Compatible API)
-----------------------------

This interface is used to query the name of the host accommodating a BMS. The **.novalocal** suffix will be added later.

-  URI

   /169.254.169.254/latest/meta-data/hostname

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/hostname**

   .. code-block::

      bms-test.novalocal

Instance Type (EC2 Compatible API)
----------------------------------

This interface is used to query the flavor name of a BMS.

-  URI

   /169.254.169.254/latest/meta-data/instance-type

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/instance-type**

   .. code-block::

      physical.i7n.28xlarge.4

Local IPv4 (EC2 Compatible API)
-------------------------------

This interface is used to query the fixed IP address of a BMS. If there are multiple NICs, only the IP address of the primary NIC is displayed.

-  URI

   /169.254.169.254/latest/meta-data/local-ipv4

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/local-ipv4**

   .. code-block::

      192.1.1.2

Availability Zone (EC2 Compatible API)
--------------------------------------

This interface is used to query AZ information about a BMS.

-  URI

   /169.254.169.254/latest/meta-data/placement/availability-zone

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/placement/availability-zone**

   .. code-block::

      az1.dc1

Public IPv4 (EC2 Compatible API)
--------------------------------

This interface is used to query the EIP of a BMS. If there are multiple NICs, only the EIP of the primary NIC is displayed.

-  URI

   /169.254.169.254/latest/meta-data/public-ipv4

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/public-ipv4**

   .. code-block::

      46.1.1.2

Public Keys (EC2 Compatible API)
--------------------------------

This interface is used to query the public key of a BMS.

-  URI

   /169.254.169.254/latest/meta-data/public-keys/0/openssh-key

-  Method

   Supports GET requests.

-  Example

   **curl** **http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key**

   .. code-block::

      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI5Fw5k8Fgzajn1zJwLoV3+wMP+6CyvsSiIc/hioggSnYu/AD0Yqm8vVO0kWlun1rFbdO+QUZKyVr/OPUjQSw4SRh4qsTKf/+eFoWTjplFvd1WCBZzS/WRenxIwR00KkczHSJro763+wYcwKieb4eKRxaQoQvoFgVjLBULXAjH4eKoKTVNtMXAvPP9aMy2SLgsJNtMb9ArfziAiblQynq7UIfLnN3VclzPeiWrqtzjyOp6CPUXnL0lVPTvbLe8sUteBsJZwlL6K4i+Y0lf3ryqnmQgC21yW4Dzu+kwk8FVT2MgWkCwiZd8gQ/+uJzrJFyMfUOBIklOBfuUENIJUhAB Generated-by-Nova
