:original_name: en-us_topic_0081116680.html

.. _en-us_topic_0081116680:

How Do I Set the BMS CPU Frequency Governor?
============================================

Generally, CPU frequency governors include **performance**, **powersave**, and **ondemand**. You can select one based on your service requirements.

Assume that you want to set the CPU frequency governor to **performance**.

-  Red Hat 6

   Make the following modification in the **/etc/sysconfig/cpuspeed** file:

   .. code-block::

      GOVERNOR=performance

-  Red Hat 7

   Make the following modification in the **/etc/sysconfig/cpupower** file:

   .. code-block::

      CPUPOWER_START_OPTS="frequency-set -g performance"

-  Debian Gnu/Linux 8

   Make the following modification in the **/etc/init.d/cpufrequtils** file:

   .. code-block::

      GOVERNOR="performance"

.. note::

   -  You can run the **yum install** *Software name* command to install the software you need, or download the software (.rpm package) from the official website and install it.
   -  You can configure a script for Red Hat 6 to automatically load the intel_pstate driver and make the preceding configurations take effect upon OS startup.

      #. Run the following command to create the **intel_pstate.modules** file:

         **vi /etc/sysconfig/modules/intel_pstate.modules**

      #. Add the following information into the file:

         .. code-block::

            /sbin/modprobe intel_pstate > /dev/null 2>&1

      #. Press **Esc** and enter **:wq!** to save the configuration.

      #. Run the following commands to modify the file permission:

         **chmod 755 /etc/sysconfig/modules/intel_pstate.modules**
