:original_name: en-us_topic_0166937671.html

.. _en-us_topic_0166937671:

Is the BMS Host Name with Suffix novalocal Normal?
==================================================

Symptom
-------

Host names of some BMSs have suffix **.novalocal**.

For example, you set the host name to **abc** during BMS creation. :ref:`Table 1 <en-us_topic_0166937671__table168595206502>` lists the host names (obtained by running the **hostname** command) of BMSs created using different images and those displayed after the BMSs are restarted.

.. _en-us_topic_0166937671__table168595206502:

.. table:: **Table 1** Hostnames of BMSs created from different images

   ========== ============================ ===========================
   Image      Host Name Before BMS Restart Host Name After BMS Restart
   ========== ============================ ===========================
   CentOS 6.8 abc                          abc.novalocal
   CentOS 7.3 abc.novalocal                abc.novalocal
   Ubuntu 16  abc                          abc
   ========== ============================ ===========================

Host names of BMSs created from some types of images have suffix **.novalocal**, whereas others do not.

Troubleshooting
---------------

This is a normal phenomenon. You can ignore it.

The static host name of a Linux BMS is user-defined and injected using Cloud-Init during the BMS creation. According to the test results, Cloud-Init adapts to OSs differently. As a result, hostnames of some ECSs have suffix **.novalocal**, whereas others do not.

If you really do not want any host names with the suffix **.novalocal**, you can change the hostname. For details, see :ref:`Changing the Name of a BMS <en-us_topic_0083737000>`
