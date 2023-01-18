:original_name: en-us_topic_0108486960.html

.. _en-us_topic_0108486960:

Installing the LOM Driver
=========================

Scenario
--------

If the BMS uses an X722 LOM, install the LOM driver on the VM.

.. note::

   This section uses CentOS 7.6 as an example to describe how to install the LOM driver. The procedure is also applicable to other OSs.

Procedure
---------

#. Upload the **NIC-X710_X722_XL710_XXV710-CentOS7.6-i40e-2.15.9-1-x86_64.rpm** package obtained in :ref:`Making Preparations <en-us_topic_0131700230>` to the VM.

#. Go to the directory where the .rpm installation package is stored and run the following command to install it:

   **rpm -ivh** **NIC-X710_X722_XL710_XXV710-CentOS7.6-i40e-2.15.9-1-x86_64.rpm**

   .. code-block:: console

      [root@localhost i40e]# rpm -ivh NIC-X710_X722_XL710_XXV710-CentOS7.6-i40e-2.15.9-1-x86_64.rpm
      Preparing...                            ################################## [100%]
      Updating / installing...
         1:i40e-2.15.9-1                       ################################## [100%]
      original pci.ids saved in /usr/local/share/i40e
      Updating initrd...
      Using dracut to update initrd...
      Successfully updated initrd.
      [root@localhost i40e]#

#. After the installation is complete, run the **rpm -qa \| grep i40e** command. The installation is successful if information similar to the following is displayed:

   .. code-block::

      i40e-2.15.9-1.x86_64
