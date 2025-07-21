:original_name: en-us_topic_0000001194363052.html

.. _en-us_topic_0000001194363052:

Modifying SSH Configuration Items
=================================

Scenario
--------

You can select the BMS login mode or account type. If special configuration is required, you can perform the operations in this section.

Procedure
---------

#. To improve BMS security, disable password-based remote login and retain only the certificate login mode.

   -  Check whether the **/etc/ssh/sshd_config** file contains parameter **ChallengeResponseAuthentication** and its value is **no**. If not, add the parameter and/or set its value to **no**. This ensures that passwords cannot be entered using the keyboard inactive method for logging in to the BMSs using Xshell.

#. Enable remote login as user **root** and SSH permissions of user **root**.

   .. caution::

      This operation may cause risks. Exercise caution before performing this operation.

   a. Open the **/etc/ssh/sshd_config** file.

      **vi /etc/ssh/sshd_config**

      Change the value of **PasswordAuthentication** to **yes** and the value of **UseDNS** to **no**.

      .. note::

         -  For SUSE and openSUSE, set the value of **PasswordAuthentication** and of **ChallengeResponseAuthentication** in the **sshd_config** file to **yes**.
         -  For Ubuntu OSs, set the value of **PermitRootLogin** to **yes**.

   b. To prevent risks, lock the initial password of user **root** in the image template by modifying the **shadow** file.

      #. Open the **/etc/shadow** file using the vi editor.

         **vi /etc/shadow**

         Add **!!** to the password hash value of user **root**. The modified configuration file is as follows:

         .. code-block::

            # cat /etc/shadow | grep root
             root:!!$6$SphQRPXu$Nvg6izXbhDPrcY3j1vRiHaQFVRpNiV3HD/bjDgnZrACOWPXwJahx78iaut1IigIUrwavVGSYQ1JOIw.rDlVh7.:17376:0:99999:7:::

      #. Press **Esc** and enter **:wq** to save and exit the file.

         .. note::

            For Ubuntu, delete the user created during OS installation. For example, if the created user is **ubuntu**, run **userdel -rf ubuntu** to delete the user.
