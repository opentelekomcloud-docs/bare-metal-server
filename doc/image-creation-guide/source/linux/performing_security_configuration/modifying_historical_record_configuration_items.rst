:original_name: en-us_topic_0000001239043027.html

.. _en-us_topic_0000001239043027:

Modifying Historical Record Configuration Items
===============================================

Scenario
--------

Modify the **/etc/profile.d/history.sh** configuration file to sort historical records by date and time. A maximum of 1000 historical records can be stored.

.. note::

   This method applies to all OSs except EulerOS.

Procedure
---------

#. Open the **/etc/profile.d/history.sh** file.

   **vi /etc/profile.d/history.sh**

#. Press **i** to enter editing mode and add the following content at the end of the file:

   .. code-block::

      export HISTTIMEFORMAT="%F %T `whoami` "
      export HISTSIZE=1000

#. Press **Esc** and enter **:wq** to save and exit the file.
