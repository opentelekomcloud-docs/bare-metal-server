:original_name: en-us_topic_0062679077.html

.. _en-us_topic_0062679077:

Are the EVS Disk Device Names on the Console and the Device Names in BMS OSs Consistent?
========================================================================================

Local System Disk
-----------------

The EVS disk device names displayed on the BMS details page on the VPC console are inconsistent with the device names displayed in the BMS OS. To prevent impact of device name changes on services, you are advised to use EVS disks by UUID.

If EVS disks are specified during BMS allocation, the EVS disk device names displayed on the BMS details page start from **/dev/sdb** and the device names displayed in the BMS OS start after the BMS local disk names, as shown in :ref:`Figure 1 <en-us_topic_0062679077__fig1769278111120>`.

.. _en-us_topic_0062679077__fig1769278111120:

.. figure:: /_static/images/en-us_image_0085721597.png
   :alt: **Figure 1** Device names in the BMS OS

   **Figure 1** Device names in the BMS OS

If EVS disks are attached to an allocated BMS, the device names displayed on the BMS details page are those specified by the tenant during disk attaching. After the EVS disks are detached from the BMS, the disks will not be displayed on the BMS details page, and the device names will be released.

If EVS disks are detached from an allocated BMS, the device names displayed in the BMS OS vary depending on whether the BMS OS restarts.

After EVS disks are attached to a BMS, if the BMS OS does not restart, the device names displayed in the BMS OS start from the smallest device name that is not used by other devices. For example, if device names **/dev/sda** and **/dev/sdc** are in use, the device names will start from **dev/sdb**. After EVS disks are detached from the BMSs, if the BMS OS does not restart, the BMS OS will release the device names.

If the BMS OS restarts, the device names displayed in the BMS OS will change based on the number of disks the BMS has and the disk attaching sequence. :ref:`Figure 2 <en-us_topic_0062679077__fig125556971412>` shows the device names displayed in the BMS OS after EVS disks are attached to the BMS (before and after BMS restart). :ref:`Figure 3 <en-us_topic_0062679077__fig571093113146>` shows the device names displayed in the BMS OS after EVS disks are detached from the BMS (before and after BMS restart).

.. _en-us_topic_0062679077__fig125556971412:

.. figure:: /_static/images/en-us_image_0085722230.png
   :alt: **Figure 2** Attaching EVS disks to a BMS

   **Figure 2** Attaching EVS disks to a BMS

.. _en-us_topic_0062679077__fig571093113146:

.. figure:: /_static/images/en-us_image_0085722243.png
   :alt: **Figure 3** Detaching EVS disks from a BMS

   **Figure 3** Detaching EVS disks from a BMS

EVS System Disk
---------------

The EVS disk device names displayed on the BMS details page on the VPC console may be inconsistent with the device names displayed in the BMS OS.

If EVS disks are specified during BMS allocation, the EVS disk device names displayed on the BMS details page start from **/dev/sda** and the device names in the BMS OS are displayed in a sequence determined by system scanning. There are two situations as shown in :ref:`Figure 4 <en-us_topic_0062679077__fig73716231158>` and :ref:`Figure 5 <en-us_topic_0062679077__fig17464143631512>`, and the EVS system disk always has the smallest drive letter of all the EVS disks.

.. _en-us_topic_0062679077__fig73716231158:

.. figure:: /_static/images/en-us_image_0085722419.png
   :alt: **Figure 4** Device names in the BMS OS (situation 1)

   **Figure 4** Device names in the BMS OS (situation 1)

.. _en-us_topic_0062679077__fig17464143631512:

.. figure:: /_static/images/en-us_image_0085722440.png
   :alt: **Figure 5** Device names in the BMS OS (situation 2)

   **Figure 5** Device names in the BMS OS (situation 2)

If EVS disks are attached to an allocated BMS, the device names displayed on the BMS details page are those specified by the tenant during disk attaching. After the EVS disks are detached from the BMS, the disks will not be displayed on the BMS details page, and the device names will be released.

If EVS disks are detached from an allocated BMS, the device names displayed in the BMS OS vary depending on whether the BMS OS restarts.

After EVS disks are attached to a BMS, if the BMS OS does not restart, the device names displayed in the BMS OS start from the smallest device name that is not used by other devices. For example, if device names **/dev/sda** and **/dev/sdc** are in use, the device names will start from **dev/sdb**. After EVS disks are detached from the BMSs, if the BMS OS does not restart, the BMS OS will release the device names.

If the BMS OS restarts, the device names displayed in the BMS OS will change based on the number of disks the BMS has and the disk attaching sequence. :ref:`Figure 6 <en-us_topic_0062679077__fig2951141791613>` and :ref:`Figure 7 <en-us_topic_0062679077__fig167631251101615>` show the device names displayed in the BMS OS after EVS disks are attached to the BMS (before and after BMS restart). :ref:`Figure 8 <en-us_topic_0062679077__fig1773821141716>` and :ref:`Figure 9 <en-us_topic_0062679077__fig107095363171>` show the device names displayed in the BMS OS after EVS disks are detached from the BMS (before and after BMS restart).

.. _en-us_topic_0062679077__fig2951141791613:

.. figure:: /_static/images/en-us_image_0085722518.png
   :alt: **Figure 6** Attaching an EVS disk (before the BMS restart)

   **Figure 6** Attaching an EVS disk (before the BMS restart)

.. _en-us_topic_0062679077__fig167631251101615:

.. figure:: /_static/images/en-us_image_0085722530.png
   :alt: **Figure 7** Attaching an EVS disk (after the BMS restart)

   **Figure 7** Attaching an EVS disk (after the BMS restart)

.. _en-us_topic_0062679077__fig1773821141716:

.. figure:: /_static/images/en-us_image_0085722556.png
   :alt: **Figure 8** Detaching an EVS disk (before the BMS restart)

   **Figure 8** Detaching an EVS disk (before the BMS restart)

.. _en-us_topic_0062679077__fig107095363171:

.. figure:: /_static/images/en-us_image_0085722625.png
   :alt: **Figure 9** Detaching an EVS disk (after the BMS restart)

   **Figure 9** Detaching an EVS disk (after the BMS restart)
