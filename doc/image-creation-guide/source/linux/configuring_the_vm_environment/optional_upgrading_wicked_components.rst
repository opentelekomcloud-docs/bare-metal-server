:original_name: en-us_topic_0000001238838165.html

.. _en-us_topic_0000001238838165:

(Optional) Upgrading Wicked Components
======================================

Scenario
--------

For SUSE 12 SP1, you need to upgrade wicked components. For other OSs, skip this section.

Procedure
---------

#. Run the **rpm -ivh --nodeps --force \*rpm** command to forcibly install wicked.

#. Run the following command to query all the installed wicked components:

   .. code-block::

      linux-locc:/home/fsp/Desktop # rpm -qa | grep wick
      wicked-service-0.6.28-1.1.x86_64
      libwicked-0-6-0.6.28-1.1.x86_64
      libwicked-0-6-0.6.40-28.6.1.x86_64
      wicked-0.6.28-1.1.x86_64
      wicked-service-0.6.40-28.6.1.x86_64
      wicked-0.6.40-28.6.1.x86_64

#. Uninstall the old wicked.

   .. code-block::

      linux-locc:/home/fsp/Desktop # rpm -e wicked-service-0.6.28-1.1.x86_64
      linux-locc:/home/fsp/Desktop # rpm -e libwicked-0-6-0.6.28-1.1.x86_64
      linux-locc:/home/fsp/Desktop # rpm -e wicked-0.6.28-1.1.x86_64
