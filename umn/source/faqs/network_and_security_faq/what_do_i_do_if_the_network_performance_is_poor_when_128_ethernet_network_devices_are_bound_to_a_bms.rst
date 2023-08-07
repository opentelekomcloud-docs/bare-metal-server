:original_name: en-us_topic_0170005210.html

.. _en-us_topic_0170005210:

What Do I Do If the Network Performance Is Poor When 128 Ethernet Network Devices Are Bound to a BMS?
=====================================================================================================

Symptom
-------

The network performance is poor when multiple Ethernet network devices (for example, 128 single-queue NICs) are bound to an EulerOS 2.3/Euler OS 2.5 BMS. This is because the interrupts of all the 128 NIC queues are processed by the same CPU, causing a critical bottleneck of the CPU and affecting the network performance. The root cause is that **--hintpolicy=subset** is set for irqbalance of the Euler OS 2.3/Euler OS 2.5 BMS. To solve the problem, change it to **--hintpolicy=ignore** as instructed in :ref:`Procedure <en-us_topic_0170005210__section590314415578>`.

.. note::

   hintpolicy is a policy used by irqbalance to balance interrupts across CPUs based on **affinity_hint** of each interrupt. **affinity_hint** indicates the CPU affinity of an interrupt. The value of **hintpolicy** can be:

   -  **exact**: irqbalance never violates **affinity_hint**.
   -  **subset**: irqbalance distributes interrupts to a subset of **affinity_hint**.
   -  **ignore**: irqbalance completely ignores **affinity_hint**.

.. _en-us_topic_0170005210__section590314415578:

Procedure
---------

The following operations use EulerOS 2.3 as an example:

#. Log in to the BMS as user **root**.

#. Run the following command to open the **/etc/sysconfig/irqbalance** file:

   **vi /etc/sysconfig/irqbalance**

#. The original setting is **--hintpolicy=subset**.

   |image1|

   Change the setting to **--hintpolicy-ignore**.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0236880110.png
.. |image2| image:: /_static/images/en-us_image_0236885177.png
