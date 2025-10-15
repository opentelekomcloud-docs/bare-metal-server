:original_name: en-us_topic_0113607323.html

.. _en-us_topic_0113607323:

Querying IP Addresses of BMSs
=============================

Scenario
--------

Call the required API to query the IP address of the BMS you have created.

Restrictions and Limitations
----------------------------

Pagination query is not supported.

Involved APIs
-------------

The following APIs are required:

Querying IP addresses of BMSs

Procedure
---------

#. Query IP addresses of BMSs.

   -  API information

      URI format: GET /v2/{project_id}/servers/{server_id}/ips

      For details, see section "Querying IP Addresses of BMSs (Native OpenStack API)" in the *Bare Metal Server API Reference*.

   -  Example request

      GET https://{ECS Endpoint}/v2/000efdc5f9064584b718b181df137bd7/servers/5850a7e7-88dd-4d99-8439-347de8cc0dd7/ips

   -  Example response

      .. code-block::

         {
             "addresses": {
                 "ddd56db4-e084-42d1-b0ff-fba1ed82abd0": [
                     {
                         "version": 4,
                         "addr": "192.168.215.62"
                     }
                 ]
             }
         }
