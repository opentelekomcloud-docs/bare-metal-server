:original_name: en-us_topic_0000001194043086.html

.. _en-us_topic_0000001194043086:

(Optional) Modifying the /etc/motd Configuration Item
=====================================================

Scenario
--------

You can modify the **motd** configuration item to remind users of changing passwords at their first login to BMSs to improve security.

Procedure
---------

#. Create or open **/etc/motd** using the vi editor.

   **vi /etc/motd**

   .. note::

      **/etc/motd** is used to store prompts displayed after you log in to Linux OSs.

#. Press **I** to enter editing mode and add the content to be displayed at the end of the file.

#. Press **Esc** and enter **:wq** to save and exit the file.
