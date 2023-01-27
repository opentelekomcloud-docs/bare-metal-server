:original_name: en-us_topic_0081116640.html

.. _en-us_topic_0081116640:

Ubuntu 18.04, Ubuntu 16.04, Ubuntu 14.04, and Debian 8.6
========================================================

.. caution::

   Use **ubuntu-**\ *xx.xx.x*\ **-server-amd64.iso** instead of **ubuntu-**\ *xx.xx.x*\ **-live-server-amd64.iso**.

#. When you install Ubuntu 18.04 or Ubuntu 16.04 ARM, select **Boot and Install with the HWE kernel** and then **Install Ubuntu Server**. (When you create an Ubuntu 18.04, Ubuntu 16.04, Ubuntu 14.04, or Debian 8.6 image, you only need to select **Install**.)

   |image1|

   |image2|

#. For Ubuntu 16.04 ARM image, select automatic partitioning. For16.04, Ubuntu 14.04, or Debian 8.6, perform the following steps for manual partitioning:

   |image3|

   |image4|

   |image5|

   |image6|

   |image7|

   |image8|

   Select **Primary** rather than **Logical**, as shown in the following figure.

   |image9|

   |image10|

   |image11|

   |image12|

   The preceding figures show how to create the boot partition and are also applicable to swap and / partitions. The following figures show the partitioning results (root partition is the last partition).

   |image13|

   Install predefined software.

   |image14|

   Install GRUB on your hard disk.

   |image15|

   |image16|

.. |image1| image:: /_static/images/en-us_image_0110218411.png
.. |image2| image:: /_static/images/en-us_image_0123516515.png
.. |image3| image:: /_static/images/en-us_image_0123516778.png
.. |image4| image:: /_static/images/en-us_image_0123517865.png
.. |image5| image:: /_static/images/en-us_image_0123517877.png
.. |image6| image:: /_static/images/en-us_image_0123517907.png
.. |image7| image:: /_static/images/en-us_image_0123518308.png
.. |image8| image:: /_static/images/en-us_image_0123518311.png
.. |image9| image:: /_static/images/en-us_image_0123519114.png
.. |image10| image:: /_static/images/en-us_image_0123519260.png
.. |image11| image:: /_static/images/en-us_image_0123519733.png
.. |image12| image:: /_static/images/en-us_image_0123519748.png
.. |image13| image:: /_static/images/en-us_image_0123527589.png
.. |image14| image:: /_static/images/en-us_image_0125269939.png
.. |image15| image:: /_static/images/en-us_image_0123527751.png
.. |image16| image:: /_static/images/en-us_image_0123527717.png
