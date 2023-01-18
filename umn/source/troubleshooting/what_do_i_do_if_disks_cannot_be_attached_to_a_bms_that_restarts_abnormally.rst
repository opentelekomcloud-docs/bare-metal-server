:original_name: en-us_topic_0104157854.html

.. _en-us_topic_0104157854:

What Do I Do If Disks Cannot Be Attached to a BMS That Restarts Abnormally?
===========================================================================

Symptom
-------

After a BMS provisioned using a local disk with data volumes restarts abnormally, no volume information exists in the BMS OS, and disks cannot be attached to the BMS on the management console.

Abnormal restart indicates that a BMS is powered off and then powered on abnormally, which is not caused by the tenant's operation on the management console.

Solution
--------

Locate the row that contains the BMS, click **More** in the **Operation** column, and select **Restart**. Disks are attached to the BMS automatically after the BMS restarts.

If disks still cannot be attached to the BMS after it is restarted, contact the operation administrator.
