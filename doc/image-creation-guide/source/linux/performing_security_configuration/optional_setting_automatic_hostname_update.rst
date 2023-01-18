:original_name: en-us_topic_0000001194363056.html

.. _en-us_topic_0000001194363056:

(Optional) Setting Automatic Hostname Update
============================================

.. note::

   After the restart, the hostname is restored to the console or the previous one. **localhost** in the **/etc/hosts** file is restored to the console name or the previous name. To prevent this problem, change the console name to be the same as the hostname.

**Check methods**

-  In the **/etc/cloud/cloud.cfg** file, check whether the **update_hostname** and **manage_etc_hosts** parameters are commented out or whether the value of **preserve_hostname** is **true**.
-  In Network Manager, check whether the value of **hostname-mode** in **/etc/NetworkManager/NetworkManager.conf** is set to **none**.
-  Check whether the value of **enable_preserve_hostname** in the **/opt/huawei/network_config/bms-network-config.conf** file is **True**.

**Commands**

-  Centralized BMS gateway

# Avoid the network from changing the hostname.

**sed -i 's/enable_preserve_hostname = False/enable_preserve_hostname = True/g' /opt/huawei/network_config/bms-network-config.conf**

# Avoid **/etc/hosts** from being modified after restart.

**sed -i '/manage_etc_hosts/s/^/#/g' /etc/cloud/cloud.cfg**

#Avoid hostname updates.

**sed -i '/- update_hostname/s/^/#/g' /etc/cloud/cloud.cfg**

-  Distributed BMS gateway

# Avoid **/etc/hosts** from being modified after restart.

**sed -i '/manage_etc_hosts/s/^/#/g' /etc/cloud/cloud.cfg**

#Avoid hostname updates.

**sed -i '/- update_hostname/s/^/#/g' /etc/cloud/cloud.cfg**

# Avoid NetworkManager from changing the name.

**sed -i '/\\[main\\]/a\\hostname-mode=none' /etc/NetworkManager/NetworkManager.conf**
