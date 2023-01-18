:original_name: en-us_topic_0078504478.html

.. _en-us_topic_0078504478:

What Do I Do If the BMS Console Is Displayed Improperly After I Remotely Log In to a BMS?
=========================================================================================

Symptom
-------

The following symptoms occur:

-  After you exit the vim editor, only half space of the screen is editable.
-  When you enter more than 80 characters, the current row is covered.
-  If you adjust the size of the browser window when using a text editor such as vim, rows are broken on the screen.

Possible Causes
---------------

Remote login to a BMS is subject to the communication on the serial port. The BMS console cannot automatically adapt to the screen. The default number of rows is 24, and that of columns is 80.

Solution
--------

After you log in to the BMS remotely, right-click the blank area and select **Resize: xxx**. A command will be pasted on the command line, such as **stty cols 166 rows 48**. Then press **Enter** and adjust the console size.


.. figure:: /_static/images/en-us_image_0086489072.png
   :alt: **Figure 1** Selecting Resize: xxx

   **Figure 1** Selecting Resize: xxx

.. caution::

   When you are using a text editor such as vim, do not adjust the window size. If you do need to adjust the window size, exit the editor first, adjust the window size, and adjust the console size based on the solution provided in this section.
