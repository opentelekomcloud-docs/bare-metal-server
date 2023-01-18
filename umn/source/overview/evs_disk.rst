:original_name: en-us_topic_0083745260.html

.. _en-us_topic_0083745260:

EVS Disk
========

What Is Elastic Volume Service (EVS)?
-------------------------------------

EVS offers scalable block storage for BMSs. EVS disks feature high reliability, high performance, and rich specifications, and are ideal for distributed file systems, development and test environments, data warehouse applications, and high-performance computing (HPC) scenarios.

Unlike traditional servers that can only use local disks, BMSs can use EVS disks that are not constrained by capacity. Shared EVS disks allow concurrent reads and writes by multiple BMSs, enabling you to deploy core applications in clusters.

EVS Disk Types
--------------

BMSs support the following types of EVS disks:

-  Common I/O: This EVS disk type delivers a maximum of 1000 IOPS. It is ideal for application scenarios that require large capacity, medium read/write speed, and fewer transactions, such as enterprise applications and small-scale testing.
-  High I/O: This EVS disk type delivers a maximum of 3000 IOPS and a minimum of 6 ms read/write latency. It is designed to meet the needs of mainstream high-performance, high-reliability application scenarios, such as enterprise applications, large-scale development and testing, and web server logs.
-  Ultra-high I/O: This EVS disk type delivers a maximum of 20,000 IOPS and a minimum of 1 ms read/write latency. It is excellent for ultra-high I/O, ultra-high bandwidth, and read/write-intensive application scenarios, such as distributed file systems in HPC or NoSQL/RDS in I/O-intensive scenarios.
-  Extreme SSD: This EVS disk type delivers up to 128,000 IOPS and sub-millisecond read latencies. With RDMA integrated with low-latency congestion control algorithms, this disk type is suitable for application scenarios that require ultra-high bandwidth and ultra-low latency.

EVS Disk Performance
--------------------

The key indicators of EVS disk performance include read/write latency, IOPS, and throughput.

-  IOPS: number of read/write operations performed by an EVS disk per second
-  Throughput: amount of data successfully transmitted by an EVS disk per second, that is, the amount of data read from and written into an EVS disk
-  Read/write latency: minimum interval between two consecutive read/write operations of an EVS disk

For more details, see *Elastic Volume Service User Guide*.

EVS Disk Device Types
---------------------

BMS supports only Small Computer System Interface (SCSI) EVS disks.

On the management console, you can create EVS disks with **Device Type** set to **SCSI**. The EVS disks support transparent SCSI command transmission, allowing BMS OSs to directly access underlying storage media. The EVS disks support basic read/write SCSI commands and advanced SCSI commands.

.. note::

   BMS public image OSs are preinstalled with the driver required to use SCSI disks, so you do not need to install the driver. To know how to install the driver, see "Installing the SDI Card Driver" in *Bare Metal Server Private Image Creation Guide*.
