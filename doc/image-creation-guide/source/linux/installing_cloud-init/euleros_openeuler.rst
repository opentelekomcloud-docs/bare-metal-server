:original_name: en-us_topic_0100489888.html

.. _en-us_topic_0100489888:

EulerOS/OpenEuler
=================

#. Use EulerOS2.2 as an example. Configure the yum source of EulerOS2.2 by editing the **/etc/yum.repos.d/EulerOS-base.repo** file. For example, the configuration is:

   .. code-block::

      [EulerOS-base]
      name=EulerOS-base
      baseurl=https://repo.huaweicloud.com/euler/2.2/os/x86_64/
      enabled=1
      gpgcheck=1
      gpgkey=https://repo.huaweicloud.com/euler/2.2/os/RPM-GPG-KEY-EulerOS

   Save the configuration.

#. Run the following command to update the yum source:

   **yum repolist**

   Run the following command to install Cloud-Init 0.7.6:

   **yum install cloud-init**

   Dependent packages of Cloud-Init 0.7.6 will be installed automatically.

   .. code-block::

      Installed:
        cloud-init.x86_64 0:0.7.6-2

      Dependency Installed:
        PyYAML.x86_64 0:3.10-11                                       audit-libs-python.x86_64 0:2.4.1-5
        checkpolicy.x86_64 0:2.1.12-6                                 libsemanage-python.x86_64 0:2.1.10-18
        libyaml.x86_64 0:0.1.4-11                                     policycoreutils-python.x86_64 0:2.2.5-15.h1
        python-IPy.noarch 0:0.75-6                                    python-backports.x86_64 0:1.0-8
        python-backports-ssl_match_hostname.noarch 0:3.4.0.2-4        python-jsonpatch.noarch 0:1.2-2
        python-jsonpointer.noarch 0:1.9-2                             python-prettytable.noarch 0:0.7.2-1
        python-requests.noarch 0:2.6.0-1                              python-six.noarch 0:1.9.0-2
        python-urllib3.noarch 0:1.10.2-2                              setools-libs.x86_64 0:3.3.7-46

      Complete!

#. To inject the password of user **root**, run the following command to upgrade **selinux-policy** from h1 to h2.

   **yum install selinux-policy**

#. Run the **cloud-init -v** command. If the command output contains the Cloud-Init version number, the installation is complete.
