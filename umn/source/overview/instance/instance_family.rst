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

-  High-performance computing

   This BMS type provides a large number of CPU cores, large memory size, and high throughput. These BMSs use Intel Skylake V5 CPUs and InfiniBand NICs and can be quickly provisioned.

   .. table:: **Table 1** High-performance computing BMS specifications

      +-------------------+---------------------------------------------+-------------------+--------------------+---------------------------+
      | Flavor Name/ID    | CPU                                         | Memory            | Local Disk         | Extended Configuration    |
      +===================+=============================================+===================+====================+===========================+
      | physical.h2.large | 2 x 18 Core Intel Skylake 6151 V5 (3.0 GHz) | DDR4 RAM (192 GB) | 1 x 1.6TB NVMe SSD | 1 x 100G IB + 2-port 10GE |
      +-------------------+---------------------------------------------+-------------------+--------------------+---------------------------+

-  I/O-optimized

   This BMS type uses SSD disks as both the system and data disks and does not support cloud storage. It is ideal for services that require local high I/O storage or Intel SGX-based trusted execution environments (TEE).

   .. table:: **Table 2** I/O-optimized BMS specifications

      +-------------------------+---------------------------------+-------------------+-------------------------------------+--------------------------+
      | Flavor Name/ID          | CPU                             | Memory            | Local Disk                          | Extended Configuration   |
      +=========================+=================================+===================+=====================================+==========================+
      | physical.i7n.28xlarge.4 | 2*28core Intel Icelake 6348 V6( | DDR4 RAM (512 GB) | 2*960GB SATA SSD + 6*960GB SATA SSD | NIC: 2 x 25GE + 2 x 25GE |
      |                         |                                 |                   |                                     |                          |
      |                         | 2.6GHz,42MB Cache)              |                   |                                     |                          |
      +-------------------------+---------------------------------+-------------------+-------------------------------------+--------------------------+

   .. note::

      -  BMS does not support auto scaling.
      -  BMS supports public images, private images, and BYOL.
      -  BMS does not support RDS, ELB, MRS, CBR, or DNS.
      -  BMS only supports a single security group.
