:original_name: en-us_topic_0000001696535081.html

.. _en-us_topic_0000001696535081:

How Do I Verify Software Package Integrity?
===========================================

.. _en-us_topic_0000001696535081__en-us_topic_0000001644407540_section12495643121911:

Prerequisites
-------------

-  A BMS has been created.
-  You have obtained the software package and its SHA256 checksum.

Verifying Software Package Integrity (Linux)
--------------------------------------------

#. Log in to the BMS as the **root** user.

#. .. _en-us_topic_0000001696535081__en-us_topic_0000001644407540_li29545568112:

   Obtain the hash value of the software.

   **sha256sum** *{Local directory of the software package}*\ **/**\ *{Software package name}*

   Replace *{Local directory of the software package}* with the actual download directory.

   Replace *{Software package name}* with the actual name of the downloaded software package. For example, the name can be **qemu-img-hw.zip**.

#. .. _en-us_topic_0000001696535081__en-us_topic_0000001644407540_li41930441931:

   Check whether the SHA256 hash value obtained in :ref:`Prerequisites <en-us_topic_0000001696535081__en-us_topic_0000001644407540_section12495643121911>` is consistent with that obtained in step :ref:`2 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li29545568112>`.

   -  If they are consistent, the verification is successful.
   -  If they are inconsistent, download the software package again and repeat steps :ref:`2 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li29545568112>` and :ref:`3 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li41930441931>` to verify it.

Verifying Software Package Integrity (Windows)
----------------------------------------------

#. Log in to the BMS.

#. .. _en-us_topic_0000001696535081__en-us_topic_0000001644407540_li15534751675:

   Open the cmd window as an administrator and run the following command to obtain the hash value of the software:

   **certutil -hashfile** *{Local directory of the software package}*\ **\\**\ *{Software package name}* **SHA256**

   Replace *{Local directory of the software package}* with the actual download directory.

   Replace *{Software package name}* with the actual name of the downloaded software package. For example, the name can be **qemu-img-hw.zip**.

#. .. _en-us_topic_0000001696535081__en-us_topic_0000001644407540_li175351751377:

   Check whether the SHA256 hash value obtained in :ref:`Prerequisites <en-us_topic_0000001696535081__en-us_topic_0000001644407540_section12495643121911>` is consistent with that obtained in step :ref:`2 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li15534751675>`.

   -  If they are consistent, the verification is successful.
   -  If they are inconsistent, download the software package again and repeat steps :ref:`2 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li15534751675>` and :ref:`3 <en-us_topic_0000001696535081__en-us_topic_0000001644407540_li175351751377>` to verify it.
