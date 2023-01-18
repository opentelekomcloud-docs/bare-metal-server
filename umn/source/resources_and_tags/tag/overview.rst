:original_name: en-us_topic_0157874334.html

.. _en-us_topic_0157874334:

Overview
========

To facilitate your management of BMSs, disks, images, and other cloud resources, you can add a tag to each resource to allocate your own metadata to the resource. Tag Management Service (TMS) is a visualized service for fast and unified cross-region tagging and categorization of cloud services.

Basics of Tags
--------------

Tags are used to identify cloud resources. When you have many cloud resources of the same type, you can use tags to classify cloud resources by dimension (for example, use, owner, or environment).

.. _en-us_topic_0157874334__fig81911042564:

.. figure:: /_static/images/en-us_image_0157904965.png
   :alt: **Figure 1** Example tags

   **Figure 1** Example tags

:ref:`Figure 1 <en-us_topic_0157874334__fig81911042564>` shows how tags work. In this example, you assign two tags to each cloud resource. Each tag contains a key and a value that you define. The key of one tag is **Owner**, and the key of another tag is **Use**. Each tag has a value.

You can quickly search for and filter specific cloud resources based on the tags added to them. For example, you can define a set of tags for cloud resources in an account to track the owner and usage of each cloud resource, making resource management easier.

Tag Usage
---------

-  BMS-related services that support tags include ECS, IMS, and EVS.

-  Each tag consists of a key and a value.

-  A BMS can have a maximum of nine tags.

-  For each resource, each tag key must be unique and can have only one tag value.

-  :ref:`Table 1 <en-us_topic_0157874334__table124931582713>` provides the tag key and value requirements.

   .. _en-us_topic_0157874334__table124931582713:

   .. table:: **Table 1** Tag key and value requirements

      +-----------------------+-------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Requirement                                                                         | Example Value         |
      +=======================+=====================================================================================+=======================+
      | Tag key               | -  Cannot be left blank.                                                            | Organization          |
      |                       | -  Can only contain letters, digits, underscores (_), and hyphens (-).              |                       |
      |                       | -  Contains a maximum of 36 characters.                                             |                       |
      +-----------------------+-------------------------------------------------------------------------------------+-----------------------+
      | Tag value             | -  Cannot be left blank.                                                            | Apache                |
      |                       | -  Can only contain letters, digits, underscores (_), periods (.), and hyphens (-). |                       |
      |                       | -  Contains a maximum of 43 characters.                                             |                       |
      +-----------------------+-------------------------------------------------------------------------------------+-----------------------+
