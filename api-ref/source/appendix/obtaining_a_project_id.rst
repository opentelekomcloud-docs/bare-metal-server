:original_name: en-us_topic_0171277624.html

.. _en-us_topic_0171277624:

Obtaining a Project ID
======================

Scenarios
---------

A project ID is required for some URLs when an API is called. Therefore, you need to obtain a project ID in advance. Two methods are available:

-  :ref:`Obtain the Project ID by Calling an API <en-us_topic_0171277624__en-us_topic_0121673684_section86806471133>`
-  :ref:`Obtain the Project ID from the Console <en-us_topic_0171277624__en-us_topic_0121673684_section32975495318>`

.. _en-us_topic_0171277624__en-us_topic_0121673684_section86806471133:

Obtain the Project ID by Calling an API
---------------------------------------

You can obtain the project ID by calling the IAM API used to query project information based on the specified criteria.

The API used to obtain a project ID is GET https://{Endpoint}/v3/projects. {Endpoint} is the IAM endpoint and can be obtained from `Regions and Endpoints <https://docs.otc.t-systems.com/additional/endpoints.html>`__.

The following is an example response. The value of **id** is the project ID.

.. code-block::

   {
       "projects": [
           {
               "domain_id": "65382450e8f64ac0870cd180d14e684b",
               "is_domain": false,
               "parent_id": "65382450e8f64ac0870cd180d14e684b",
               "name": "project_name",
               "description": "",
               "links": {
                   "next": null,
                   "previous": null,
                   "self": "https://www.example.com/v3/projects/a4a5d4098fb4474fa22cd05f897d6b99"
               },
               "id": "a4a5d4098fb4474fa22cd05f897d6b99",
               "enabled": true
           }
       ],
       "links": {
           "next": null,
           "previous": null,
           "self": "https://www.example.com/v3/projects"
       }
   }

.. _en-us_topic_0171277624__en-us_topic_0121673684_section32975495318:

Obtain a Project ID from the Console
------------------------------------

A project ID needs to be specified in the URIs of some APIs. Therefore, you need to obtain the project ID before calling APIs. The following procedure describes how to obtain a project ID:

#. Log in to the management console.

#. Click the username and select **My Credentials** from the drop-down list.

   On the **My Credentials** page, view project IDs in the project list.


   .. figure:: /_static/images/en-us_image_0000001508295281.png
      :alt: **Figure 1** Viewing project IDs

      **Figure 1** Viewing project IDs

   In multi-project scenarios, expand the region, and obtain your sub-project ID from the **Project ID** column.
