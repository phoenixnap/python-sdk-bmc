# OsConfigurationCloudInit

Cloud-init configuration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_data** | **bytearray** | (Write-only) User data for the &lt;a href&#x3D;&#39;https://cloudinit.readthedocs.io/en/latest/&#39; target&#x3D;&#39;_blank&#39;&gt;cloud-init&lt;/a&gt; configuration in base64 encoding. NoCloud format is supported. Follow the &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/bmc-cloud-init&#39; target&#x3D;&#39;_blank&#39;&gt;instructions&lt;/a&gt; on how to provision a server using cloud-init. Only ubuntu/bionic, ubuntu/focal, ubuntu/jammy, debian/bullseye, debian/bookworm, centos/centos7, centos/centos8, almalinux/almalinux8, almalinux/almalinux9, rockylinux/rockylinux8, rockylinux/rockylinux9 and virtuozzo/virtuozzo7 are supported. User data will not be stored and cannot be retrieved once you deploy the server. Copy and save it for future reference. | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration_cloud_init import OsConfigurationCloudInit

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationCloudInit from a JSON string
os_configuration_cloud_init_instance = OsConfigurationCloudInit.from_json(json)
# print the JSON string representation of the object
print OsConfigurationCloudInit.to_json()

# convert the object into a dict
os_configuration_cloud_init_dict = os_configuration_cloud_init_instance.to_dict()
# create an instance of OsConfigurationCloudInit from a dict
os_configuration_cloud_init_form_dict = os_configuration_cloud_init.from_dict(os_configuration_cloud_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


