:original_name: en-us_topic_0140735213.html

.. _en-us_topic_0140735213:

Lifecycle
=========

The lifecycle of a BMS contains all states from its creation to deletion.


.. figure:: /_static/images/en-us_image_0181878592.png
   :alt: **Figure 1** BMS states

   **Figure 1** BMS states

.. table:: **Table 1** BMS states

   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | State               | Attribute          | Description                                                                                                                                      | API Status                              |
   +=====================+====================+==================================================================================================================================================+=========================================+
   | Creating            | Intermediate state | A BMS is in this state after you request for the BMS and before it enters the running state.                                                     | BUILD/BUILDING                          |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | If a BMS remains in this state for a long time, exceptions will occur. Contact the operation administrator to handle the exceptions.             |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Starting            | Intermediate state | It is an intermediate state between **Stopped** and **Running**.                                                                                 | SHUTOFF                                 |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | If a BMS remains in this state for a long time, exceptions will occur. Contact the operation administrator to handle the exceptions.             |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Running             | Stable state       | A BMS is in this state when it is running properly.                                                                                              | ACTIVE                                  |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | A BMS in this state can be used normally.                                                                                                        |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Stopping            | Intermediate state | It is an intermediate state between **Running** and **Stopped**.                                                                                 | ACTIVE                                  |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | If a BMS remains in this state for a long time, exceptions will occur. Contact the operation administrator to handle the exceptions.             |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Stopped             | Stable state       | A BMS is in this state after it is stopped successfully.                                                                                         | SHUTOFF                                 |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | A BMS in this state cannot be used.                                                                                                              |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Restarting          | Intermediate state | A BMS is in this state when it is being restarted.                                                                                               | REBOOT                                  |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | If a BMS remains in this state for a long time, exceptions will occur. Contact the operation administrator to handle the exceptions.             |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Forcibly restarting | Intermediate state | A BMS is in this state when it is being forcibly restarted.                                                                                      | HARD_REBOOT                             |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Deleting            | Intermediate state | A BMS is in this state when it is being deleted.                                                                                                 | ACTIVE/SHUTOFF/REBOOT/HARD_REBOOT/ERROR |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | If a BMS remains in this state for a long time, exceptions will occur. Contact the operation administrator to handle the exceptions.             |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Deleted             | Intermediate state | A BMS is in this state after it is deleted successfully. A BMS in this state cannot be used and will be removed from the system in a short time. | DELETED                                 |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Faulty              | Stable state       | A BMS is in this state when an exception occurs on it.                                                                                           | ERROR                                   |
   |                     |                    |                                                                                                                                                  |                                         |
   |                     |                    | A BMS in this state cannot be used. Contact the operation administrator to rectify the fault.                                                    |                                         |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
   | Rebuilding          | Intermediate state | A BMS is in this state when it is being rebuilt.                                                                                                 | SHUTOFF                                 |
   +---------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
