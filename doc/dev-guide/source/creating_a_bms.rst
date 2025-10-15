:original_name: en-us_topic_0113607320.html

.. _en-us_topic_0113607320:

Creating a BMS
==============

Scenario
--------

Create a BMS with EVS disks.

Restrictions and Limitations
----------------------------

File injection is not supported.

Involved APIs
-------------

When creating a BMS, you need to perform operations such as querying the flavor, querying the AZ, and creating EVS disks. The following APIs are required:

-  Querying AZs
-  Querying BMS flavors
-  Querying images
-  Creating an EVS disk
-  Querying VPCs
-  Querying a security group
-  Querying subnets
-  Creating a BMS

Procedure
---------

#. Query the AZ where the BMS resides.

   -  API information

      URI format: GET /v2/{project_id}/os-availability-zone

      For details, see section "Querying AZs" in the *Elastic Cloud Server API Reference*.

   -  Example request

      GET https://{ECS Endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/os-availability-zone

   -  Example response

      .. code-block::

         {
             "availabilityZoneInfo": [
                 {
                     "zoneState": {
                         "available": true
                     },
                     "hosts": null,
                     "zoneName": "az-dc-1"
                 },
                 {
                     "zoneState": {
                         "available": true
                     },
                     "hosts": null,
                     "zoneName": "az-dc-2"
                 }
             ]
         }

#. Query the BMS flavor.

   -  API information

      URI format: GET /v2/{project_id}/flavors/detail

      For details, see section "Querying BMS Flavors (Native OpenStack API)" in the *Bare Metal Server API Reference*.

      .. note::

         BMS flavors have prefix **physical.**

   -  Example request

      GET https://{ECS Endpoint}/v2/384627f84f384e9eb4463492be39a950/flavors/detail

   -  Example response

      .. code-block::

         {
             "flavors": [
                  "name": "physical.o2.medium",
                     "links": [
                         {
                             "href": "https://compute.region.eu-de.otc-tsi.de/v2/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                             "rel": "self"
                         },
                         {
                             "href": "https://compute.region.eu-de.otc-tsi.de/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                             "rel": "bookmark"
                         }
                     ],
                     "ram": 321725,
                     "OS-FLV-DISABLED:disabled": false,
                     "vcpus": 56,
                     "swap": "",
                     "os-flavor-access:is_public": true,
                     "rxtx_factor": 1,
                     "OS-FLV-EXT-DATA:ephemeral": 0,
                     "disk": 3725,
                     "id": "physical.o2.medium"
             ]
         }

#. Query images.

   -  API information

      URI format: GET /v2/images

      For details, see section "Querying Images (Native OpenStack API)" in the *Image Management API Reference*.

   -  Example request

      GET https://{IMS Endpoint}/v2/images

   -  Example response

      .. code-block::

         {
             "images": [
                 {
                     "status": "queued",
                     "name": "test",
                     "tags": [
                         "test",
                         "image"
                     ],
                     "container_format": "bare",
                     "created_at": "2014-12-16T01:22:05Z",
                     "disk_format": "qcow2",
                     "updated_at": "2014-12-16T01:22:05Z",
                     "visibility": "private",
                     "self": "/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90",
                     "min_disk": 1,
                     "protected": false,
                     "id": "4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90",
                     "file": "/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90/file",
                     "owner": "aed2c611711548a4a9c16fb8fe166af4",
                     "min_ram": 1024,
                     "schema": "/v2/schemas/image"
                 },
                 {
                     "status": "active",
                     "name": "cirros",
                     "tags": [
                         "new"
                     ],
                     "container_format": "bare",
                     "created_at": "2014-12-11T03:53:43Z",
                     "size": 13147648,
                     "disk_format": "qcow2",
                     "updated_at": "2014-12-15T20:02:12Z",
                     "visibility": "private",
                     "self": "/v2/images/5155a22a-834e-4ffe-a95d-ed9665a8ed76",
                     "min_disk": 0,
                     "protected": false,
                     "id": "5155a22a-834e-4ffe-a95d-ed9665a8ed76",
                     "file": "/v2/images/5155a22a-834e-4ffe-a95d-ed9665a8ed76/file",
                     "checksum": "d972013792949d0d3ba628fbe8685bce",
                     "owner": "aed2c611711548a4a9c16fb8fe166af4",
                     "min_ram": 0,
                     "schema": "/v2/schemas/image"
                 }
             ],
             "schema": "/v2/schemas/images",
             "first": "/v2/images"
         }

#. Create an EVS disk.

   -  API information

      URI format: POST /v2/{project_id}/volumes

      For details, see section "Creating an EVS Disk" in the *Elastic Volume Service API Reference*.

   -  Example request

      POST https://{EVS Endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/volumes

      .. code-block::

         {
             "volume": {
                 "name": "openapi_vol01",
                 "imageRef": "027cf713-45a6-45f0-ac1b-0ccc57ac12e2",
                 "availability_zone": "az-dc-1",
                 "description": "create for api test",
                 "volume_type": "SATA",
                 "metadata": {
                     "volume_owner": "openapi"
                 },
                 "consistencygroup_id": null,
                 "OS-SCH-HNT:scheduler_hints": {
                     "dedicated_storage_id": "eddc1a3e-4145-45be-98d7-bf6f65af9767"
                 },
                 "source_volid": null,
                 "snapshot_id": null,
                 "shareable": "false",
                 "multiattach": false,
                 "source_replica": null,
                 "size": 40
             }
         }

   -  Example response

      .. code-block::

         {
             "volume": {
                 "attachments": [ ],
                 "availability_zone": "az-dc-1",
                 "bootable": "false",
                 "consistencygroup_id": null,
                 "created_at": "2016-05-25T02:38:40.392463",
                 "description": "create for api test",
                 "encrypted": false,
                 "id": "8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
                 "links": [
                     {
                         "href": "https://volume.localdomain.com:8776/v2/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
                         "rel": "self"
                     },
                     {
                         "href": "https://volume.localdomain.com:8776/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
                         "rel": "bookmark"
                     }
                 ],
                 "metadata": {
                     "volume_owner": "openapi"
                 },
                 "name": "openapi_vol01",
                 "replication_status": "disabled",
                 "shareable": false,
                 "multiattach": false,
                 "size": 40,
                 "snapshot_id": null,
                 "source_volid": null,
                 "status": "creating",
                 "updated_at": null,
                 "user_id": "39f6696ae23740708d0f358a253c2637",
                 "volume_type": "SATA"
             }
         }

      or

      .. code-block::

         {
             "error": {
                 "message": "XXXX",
                 "code": "XXX"
             }
         }

      In the preceding example, **error** indicates a general error, for example, **badRequest** or **itemNotFound**. An example is provided as follows:

      .. code-block::

         {
             "badRequest": {
                 "message": "XXXX",
                 "code": "XXX"
             }
         }

#. Query VPCs.

   -  API information

      URI format: GET /v1/{project_id}/vpcs

      For details, see section "Querying VPCs" in the *Virtual Private Cloud API Reference*.

   -  Example request

      GET https://{VPC Endpoint}/v1/000efdc5f9064584b718b181df137bd7/vpcs

   -  Example response

      .. code-block::

         {
             "vpcs": [
                 {
                     "id": "13551d6b-755d-4757-b956-536f674975c0",
                     "name": "default",
                     "cidr": "172.16.0.0/16",
                     "status": "OK",
                     "routes": null
                 },
                 {
                     "id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                     "name": "222",
                     "cidr": "192.168.0.0/16",
                     "status": "OK",
                     "routes": null
                 },
                 {
                     "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
                     "name": "vpc",
                     "cidr": "192.168.0.0/16",
                     "status": "OK",
                     "routes": null
                 }
             ]
         }

#. Query a security group.

   -  API information

      URI format: GET /v2.0/security-groups

      For details, see section "Querying Security Groups" in the *Virtual Private Cloud API Reference*.

   -  Example request

      GET https://{VPC Endpoint}/v2.0/security-groups

   -  Example response

      .. code-block::

         {
             "security_groups": [
                 {
                     "tenant_id": "84b25ac10ed642cca484aa55c098e3aa",
                     "name": "default",
                     "description": "Default security group",
                     "security_group_rules": [
                         {
                             "remote_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967",
                             "direction": "ingress",
                             "remote_ip_prefix": null,
                             "protocol": null,
                             "ethertype": "IPv6",
                             "tenant_id": "84b25ac10ed642cca484aa55c098e3aa",
                             "port_range_max": null,
                             "port_range_min": null,
                             "id": "07adc044-3f21-4eeb-bd57-5e5eb6024b7f",
                             "description": null,
                             "security_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967"
                         },
                         {
                             "remote_group_id": null,
                             "direction": "egress",
                             "remote_ip_prefix": null,
                             "protocol": null,
                             "ethertype": "IPv6",
                             "tenant_id": "84b25ac10ed642cca484aa55c098e3aa",
                             "port_range_max": null,
                             "port_range_min": null,
                             "id": "47e05c14-1aa2-4355-aaf8-b57e18f98c9a",
                             "description": null,
                             "security_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967"
                         },
                         {
                             "remote_group_id": null,
                             "direction": "egress",
                             "remote_ip_prefix": null,
                             "protocol": null,
                             "ethertype": "IPv4",
                             "tenant_id": "84b25ac10ed642cca484aa55c098e3aa",
                             "port_range_max": null,
                             "port_range_min": null,
                             "id": "8a8a238b-fdb1-4321-b667-26205c7f37d1",
                             "description": null,
                             "security_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967"
                         },
                         {
                             "remote_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967",
                             "direction": "ingress",
                             "remote_ip_prefix": null,
                             "protocol": null,
                             "ethertype": "IPv4",
                             "tenant_id": "84b25ac10ed642cca484aa55c098e3aa",
                             "port_range_max": null,
                             "port_range_min": null,
                             "id": "b5874440-84a0-4382-8e37-3f012b90b71e",
                             "description": null,
                             "security_group_id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967"
                         }
                     ],
                     "id": "1d8b19c7-7c56-48f7-a99b-4b40eb390967"
                 }
             ]
         }

#. Query subnets.

   -  API information

      URI format: GET /v1/{project_id}/subnets

      For details, see section "Querying Subnets" in the *Virtual Private Cloud API Reference*.

   -  Example request

      GET https://{VPC Endpoint}/v1/000efdc5f9064584b718b181df137bd7/subnets

   -  Example response

      .. code-block::

         {
             "subnets": [
                 {
                     "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                     "name": "subnet",
                     "cidr": "192.168.20.0/24",
                     "dnsList": [
                         "114.114.114.114",
                         "114.114.115.115"
                     ],
                     "status": "ACTIVE",
                     "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                     "gateway_ip": "192.168.20.1",
                     "dhcp_enable": true,
                     "primary_dns": "114.114.114.114",
                     "secondary_dns": "114.114.115.115",
                     "availability_zone": "az-dc-1"  //Assume that the AZ name is az-dc-1.
                     "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                     "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
                 },
                 {
                     "id": "531dec0f-3116-411b-a21b-e612e42349fd",
                     "name": "Subnet1",
                     "cidr": "192.168.1.0/24",
                     "dnsList": [
                         "114.114.114.114",
                         "114.114.115.115"
                     ],
                     "status": "ACTIVE",
                     "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                     "gateway_ip": "192.168.1.1",
                     "dhcp_enable": true,
                     "primary_dns": "114.114.114.114",
                     "secondary_dns": "114.114.115.115",
                     "availability_zone": "az-dc-1"  //Assume that the AZ name is az-dc-1.
                     "neutron_network_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                     "neutron_subnet_id": "1aac193-a2ad-f153-d122-12d64c2c1d78"
                 }
             ]
         }

#. Create a BMS.

   -  Prerequisites

      Mandatory parameters: **name**, **imageRef**, **flavorRef**, **networks**, and **availability_zone**

      Optional parameters: **root_volume**, **data_volumes**, and **security_groups**

   -  API information

      URI format: POST /v2.1/{project_id}/servers

      For details, see section "Creating a BMS (Native OpenStack API)" in the *Bare Metal Server API Reference*.

   -  Example request

      POST /v2.1/000efdc5f9064584b718b181df137bd7/servers

      .. code-block::

         {
             "server": {
                 "imageRef": "1a6635d8-afea-4f2b-abb6-27a202bad319",
                 "flavorRef": "physical.o2.medium",
                 "data_volumes": [
                     {
                         "volumetype": "SATA",
                         "size": 40,
                         "shareable": false,
                         "extendparam": {
                            "resourceSpecCode": "",
                            "resourceType": ""
                         }
                     }
                 ],
                 "name": "bms_name01",
                 "availability_zone": "az-dc-1",
                 "networks": [
                     {
                         "uuid": "8470310b-bfa2-4edf-8f64-d15196b2b2c9"
                     }
                 ]
             }
         }

   -  Example response

      .. code-block::

         {
             "server": {
                 "security_groups": [
                     {
                         "name": "default"
                     }
                 ],
                 "OS-DCF:diskConfig": "MANUAL",
                 "os-extended-volumes:volumes_attached": [
                     {
                         "id": "dc5b02ea-bece-4ec8-b194-f39db96406c8",
                         "delete_on_termination": false
                     }
                 ],
                 "links": [
                     {
                         "rel": "self",
                         "href": "https://ecs-api.eu-de.otc-tsi.de/v2/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                     },
                     {
                         "rel": "bookmark",
                         "href": "https://ecs-api.eu-de.otc-tsi.de/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                     }
                 ],
                 "id": "9ab74d89-61e7-4259-8546-465fdebe4944",
                 "adminPass": "RjdD3h8U2DBe"
             }
         }
