:original_name: en-us_topic_0110303862.html

.. _en-us_topic_0110303862:

BMS Operations Recorded by CTS
==============================

Cloud Trace Service (CTS) is a log audit service provided by the public cloud and intended for cloud security. It allows you to collect, store, and query cloud resource operation records and use these records for security analysis, compliance auditing, resource tracking, and fault locating.

You can use CTS to record BMS operations for later querying, auditing, and backtracking.

Prerequisites
-------------

You need to enable CTS before using it. If it is not enabled, BMS operations cannot be recorded. After being enabled, CTS automatically creates a tracker to record all your operations. The tracker stores only the operations of the last seven days. To store the operations for a longer time, store trace files in OBS buckets.


BMS Operations Recorded by CTS
------------------------------

.. table:: **Table 1** BMS operations recorded by CTS

   ================ ======== ======================
   Operation        Resource Trace Name
   ================ ======== ======================
   Creating a BMS   bms      createBareMetalServers
   Deleting a BMS   bms      deleteBareMetalServers
   Starting a BMS   bms      startBareMetalServers
   Stopping a BMS   bms      stopBareMetalServers
   Restarting a BMS bms      rebootBareMetalServers
   ================ ======== ======================
