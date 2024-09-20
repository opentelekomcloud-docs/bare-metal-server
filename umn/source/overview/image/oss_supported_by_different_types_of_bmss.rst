:original_name: en-us_topic_0263802108.html

.. _en-us_topic_0263802108:

OSs Supported by Different Types of BMSs
========================================

The following tables list the 64-bit OSs supported by different BMS types.

:ref:`Table 1 <en-us_topic_0263802108__table1261773364111>` lists the OSs supported by high-performance computing physical.h2.large BMSs.

:ref:`Table 2 <en-us_topic_0263802108__table188617221012>` lists the OSs supported by I/O optimized physical.i7n.28xlarge.4 BMSs.

.. note::

   -  It is recommended that you use the official OS release versions. Do not tailor or customize the release versions, or problems may occur.
   -  OS vendors do not always update OS release versions regularly. Some versions are no longer maintained, and these deprecated versions no longer receive security patches. Ensure that you read the update notifications from OS vendors and update your OS so that it runs properly.
   -  For CentOS 7.4 or earlier, BMS extension NICs cannot be pinged due to known kernel issues. So, you are advised to use CentOS 7.5 or later. For details, see :ref:`How Do I Handle the Failure to Ping a CentOS 7 Extension NIC? <en-us_topic_0151554411>`

.. _en-us_topic_0263802108__table1261773364111:

.. table:: **Table 1** High-performance computing physical.h2.large

   ======= =================================================
   OS      Version
   ======= =================================================
   CentOS  CentOS 6.9/7.3/7.4/7.5/7.6
   SUSE    SUSE Linux Enterprise 11.SP4/12.SP1/12.SP2/12.SP3
   Ubuntu  Ubuntu 16.04 LTS
   EulerOS EulerOS 2.3
   ======= =================================================

.. _en-us_topic_0263802108__table188617221012:

.. table:: **Table 2** I/O-optimized physical.i7n.28xlarge.4

   ====== ================
   OS     Version
   ====== ================
   Ubuntu Ubuntu 22.04 LTS
   ====== ================
