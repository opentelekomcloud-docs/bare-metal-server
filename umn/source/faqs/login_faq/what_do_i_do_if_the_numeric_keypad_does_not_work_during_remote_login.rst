:original_name: en-us_topic_0243372663.html

.. _en-us_topic_0243372663:

What Do I Do If the Numeric Keypad Does Not Work During Remote Login?
=====================================================================

Symptom
-------

When I enter numbers using the numeric keypad for remote login, the numbers are not displayed properly.

|image1|

Solution
--------

Run the Linux **setleds** command to turn on the numeric keypad.

#. On the remote login page, run the following command to query the status of the numeric keypad:

   **setleds -F**

   |image2|

   **NumLock** is **off**, indicating that the numeric keypad is turned off.

#. Run the following command to turn on the numeric keypad:

   **setleds +num**

#. Run the **setleds -F** command again. If **NumLock** changes to **on**, the issue is fixed.

.. |image1| image:: /_static/images/en-us_image_0243377357.png
.. |image2| image:: /_static/images/en-us_image_0243377633.png
