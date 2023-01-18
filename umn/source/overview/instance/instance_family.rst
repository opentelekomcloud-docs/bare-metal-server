:original_name: en-us_topic_0083745258.html

.. _en-us_topic_0083745258:

Instance Family
===============

Overview
--------

An instance is a purchased BMS. Different instance types provide varied computing capabilities, storage space, and network performance. You can select a type that meets your service requirements.

BMS Types
---------

The cloud platform provides a variety of BMS flavors that you can choose from.

-  Compute-optimized

   This BMS type uses SDI iNICs and supports OLTP databases with higher performance, higher memory ratio, and transactional workloads cache.

   .. table:: **Table 1** Compute-optimized BMS specifications

      +--------------------+--------------------------------------------+-------------------+------------------------------------------------+------------------------+
      | Flavor Name/ID     | CPU                                        | Memory            | Local Disk                                     | Extended Configuration |
      +====================+============================================+===================+================================================+========================+
      | physical.o2.medium | 2 x 8 Core Intel Xeon E5-2667 V4 (3.2 GHz) | DDR4 RAM (256 GB) | 2 x 800GB SAS SSD RAID1 + NVMe SSD Card 1.6 TB | 2 x 2-port 10GE        |
      +--------------------+--------------------------------------------+-------------------+------------------------------------------------+------------------------+

-  High-performance computing

   This BMS type provides a large number of CPU cores, large memory size, and high throughput. These BMSs use Intel Skylake V5 CPUs and InfiniBand NICs and can be quickly provisioned.

   .. table:: **Table 2** High-performance computing BMS specifications

      +-------------------+---------------------------------------------+-------------------+--------------------+---------------------------+
      | Flavor Name/ID    | CPU                                         | Memory            | Local Disk         | Extended Configuration    |
      +===================+=============================================+===================+====================+===========================+
      | physical.h2.large | 2 x 18 Core Intel Skylake 6151 V5 (3.0 GHz) | DDR4 RAM (192 GB) | 1 x 1.6TB NVMe SSD | 1 x 100G IB + 2-port 10GE |
      +-------------------+---------------------------------------------+-------------------+--------------------+---------------------------+

-  GPU-accelerated

   This BMS type provides outstanding floating-point computing performance and is ideal for real-time, highly concurrent massive computing scenarios, such as deep learning, scientific computing, CAE, 3D animation rendering, and CAD. G560 servers with InfiniBand NICs and industry-leading NVIDIA Tesla P100 GPU and Tesla V100 GPU are used to provide you with excellent performance and cost-effective services.

   .. table:: **Table 3** GPU-accelerated BMS specifications

      +-------------------+---------------------------------------------+-------------------+----------------------------------------+--------------------------------+
      | Flavor Name/ID    | CPU                                         | Memory            | Local Disk                             | Extended Configuration         |
      +===================+=============================================+===================+========================================+================================+
      | physical.p1.large | 2 x 14 Core Intel Xeon E5-2690 V4 (2.6 GHz) | DDR4 RAM (512 GB) | 2 x 600GB SAS HDD + 6 x 800GB NVMe SSD | NIC: 1 x 100G IB + 2-port 10GE |
      |                   |                                             |                   |                                        |                                |
      |                   |                                             |                   |                                        | GPU: 8 x Tesla P100            |
      |                   |                                             |                   |                                        |                                |
      |                   |                                             |                   |                                        | GPU memory: 16 GB              |
      +-------------------+---------------------------------------------+-------------------+----------------------------------------+--------------------------------+
      | physical.p2.large | 2 x 14 Core Intel Xeon E5-2690 V4 (2.6 GHz) | DDR4 RAM (512 GB) | 2 x 600GB SAS HDD + 6 x 800GB NVMe SSD | NIC: 1 x 100G IB + 2-port 10GE |
      |                   |                                             |                   |                                        |                                |
      |                   |                                             |                   |                                        | GPU: 8 x Tesla V100            |
      |                   |                                             |                   |                                        |                                |
      |                   |                                             |                   |                                        | GPU memory: 16 GB              |
      +-------------------+---------------------------------------------+-------------------+----------------------------------------+--------------------------------+

   .. note::

      physical.p1.large and physical.p2.large BMSs support only Ubuntu 16.04 and CentOS 7.4 private images.

-  Memory-optimized

   This BMS type has DIMM memory with quick read/write speed and high density and is ideal for SAP HANA and memory databases.

   .. table:: **Table 4** Memory-optimized BMS specifications

      +--------------------+----------------------------------------------------+--------------------+----------------------------------------------------------------------------+------------------------+
      | Flavor Name/ID     | CPU                                                | Memory             | Local Disk                                                                 | Extended Configuration |
      +====================+====================================================+====================+============================================================================+========================+
      | physical.m2.medium | 4 x 24 Core Broadwell EX Xeon E7-8890 V4 (2.2 GHz) | DDR4 RAM (2048 GB) | 2 x 600GB SAS HDD RAID1 + 7 x 1.8TB SAS HDD RAID5 + 2 x 1.6TB NVMe SSD     | 2 x 2-port 10GE        |
      +--------------------+----------------------------------------------------+--------------------+----------------------------------------------------------------------------+------------------------+
      | physical.m2.xlarge | 4 x 24 Core Broadwell EX Xeon E7-8890 V4 (2.2 GHz) | DDR4 RAM (4096 GB) | 2 x 600GB SAS HDD RAID 1 + 14 x 1.8TB SAS HDD RAID 50 + 2 x 1.6TB NVMe SSD | 2 x 2-port 10GE        |
      +--------------------+----------------------------------------------------+--------------------+----------------------------------------------------------------------------+------------------------+
