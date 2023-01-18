:original_name: en-us_topic_0081116590.html

.. _en-us_topic_0081116590:

Stopping the VM and Obtaining the Image
=======================================

Stopping the VM
---------------

You can run the **sudo poweroff** command in the VM to stop it. If it cannot be stopped, on virt-manager, click **Virtual Machine Manager**, select the VM and right-click **Shut Down**.

If the VM still cannot be stopped, you are advised to click **Force Off** to forcibly stop it.

Generating an Image File
------------------------

If you choose to automatically create the image, the .qcow2 or .img image file is stored in the **/var/lib/libvirt/images** directory on the host.


.. figure:: /_static/images/en-us_image_0110273640.png
   :alt: **Figure 1** Image file (Linux)

   **Figure 1** Image file (Linux)

If you choose to manually create the image, obtain the image file from your specified directory.

Compressing the Image File
--------------------------

If the generated image file is too large, run the following command to compress it:

**qemu-img convert -f raw -O qcow2** *SourceFile* *FinallyFile.qcow2*

*SourceFile* can be in .img or .qcow2 format.
