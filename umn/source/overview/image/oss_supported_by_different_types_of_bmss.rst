:original_name: en-us_topic_0263802108.html

.. _en-us_topic_0263802108:

OSs Supported by Different Types of BMSs
========================================

The following tables list the 64-bit OSs supported by different BMS types.

-  :ref:`Table 1 <en-us_topic_0263802108__table145638289168>` lists the OSs supported by compute-optimized physical.o2.medium BMSs.
-  :ref:`Table 2 <en-us_topic_0263802108__table221119842419>` lists the OSs supported by GPU-accelerated P1 and P2 BMSs.
-  :ref:`Table 3 <en-us_topic_0263802108__table1261773364111>` lists the OSs supported by high-performance computing physical.h2.large BMSs.
-  :ref:`Table 4 <en-us_topic_0263802108__table16114231102412>` lists the OSs supported by memory-optimized M2 BMSs.

.. note::

   -  It is recommended that you use the official OS release versions. Do not tailor or customize the release versions, or problems may occur.
   -  OS vendors do not always update OS release versions regularly. Some versions are no longer maintained, and these deprecated versions no longer receive security patches. Ensure that you read the update notifications from OS vendors and update your OS so that it runs properly.
   -  For CentOS 7.4 or earlier, BMS extension NICs cannot be pinged due to known kernel issues. So, you are advised to use CentOS 7.5 or later. For details, see :ref:`How Do I Handle the Failure to Ping a CentOS 7 Extension NIC? <en-us_topic_0151554411>`

.. _en-us_topic_0263802108__table145638289168:

.. table:: **Table 1** Compute-optimized physical.o2.medium

   +-----------------------------------+---------------------------------------------------+
   | OS                                | Version                                           |
   +===================================+===================================================+
   | Windows                           | Windows Server 2012 R2 Standard                   |
   |                                   |                                                   |
   |                                   | Windows Server 2016 Standard                      |
   +-----------------------------------+---------------------------------------------------+
   | CentOS                            | CentOS 6.7/6.8/6.9/7.2/7.3/7.4/7.5/7.6            |
   +-----------------------------------+---------------------------------------------------+
   | Red Hat                           | Red Hat 6.7/6.8/6.9/7.2/7.3/7.4/7.5               |
   +-----------------------------------+---------------------------------------------------+
   | SUSE                              | SUSE Linux Enterprise 11.SP4/12.SP1/12.SP2/12.SP3 |
   +-----------------------------------+---------------------------------------------------+
   | Ubuntu                            | Ubuntu 14.04 LTS                                  |
   |                                   |                                                   |
   |                                   | Ubuntu 14.04.5 LTS                                |
   |                                   |                                                   |
   |                                   | Ubuntu 16.04 LTS                                  |
   +-----------------------------------+---------------------------------------------------+
   | Oracle Linux                      | Oracle Linux 6.9/7.4                              |
   +-----------------------------------+---------------------------------------------------+
   | EulerOS                           | EulerOS 2.2/2.3                                   |
   +-----------------------------------+---------------------------------------------------+

.. _en-us_topic_0263802108__table221119842419:

.. table:: **Table 2** GPU-accelerated P1 and P2

   ======= ==================
   OS      Version
   ======= ==================
   CentOS  CentOS 7.4/7.5/7.6
   Ubuntu  Ubuntu 16.04 LTS
   EulerOS EulerOS 2.3
   ======= ==================

.. _en-us_topic_0263802108__table1261773364111:

.. table:: **Table 3** High-performance computing physical.h2.large

   ======= =================================================
   OS      Version
   ======= =================================================
   CentOS  CentOS 6.9/7.3/7.4/7.5/7.6
   SUSE    SUSE Linux Enterprise 11.SP4/12.SP1/12.SP2/12.SP3
   Ubuntu  Ubuntu 16.04 LTS
   EulerOS EulerOS 2.3
   ======= =================================================

.. _en-us_topic_0263802108__table16114231102412:

.. table:: **Table 4** Memory-optimized M2

   ====== ==========================
   OS     Version
   ====== ==========================
   CentOS CentOS 7.2/7.3/7.4/7.5/7.6
   ====== ==========================
