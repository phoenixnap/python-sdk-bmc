# ServerCreate

Provision bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname of server. | 
**os** | **str** | The server’s OS ID used when the server was created. Currently this field should be set to either &#x60;ubuntu/bionic&#x60;, &#x60;ubuntu/focal&#x60;, &#x60;ubuntu/jammy&#x60;, &#x60;centos/centos7&#x60;, &#x60;centos/centos8&#x60;, &#x60;windows/srv2019std&#x60;, &#x60;windows/srv2019dc&#x60;, &#x60;esxi/esxi70&#x60;, &#x60;esxi/esxi80&#x60;, &#x60;almalinux/almalinux8&#x60;, &#x60;rockylinux/rockylinux8&#x60;, &#x60;virtuozzo/virtuozzo7&#x60;, &#x60;debian/bullseye&#x60;, &#x60;proxmox/bullseye&#x60;, &#x60;netris/controller&#x60;, &#x60;netris/softgate_1g&#x60; or &#x60;netris/softgate_10g&#x60;. | 
**type** | **str** | Server type ID. Cannot be changed once a server is created. Currently this field should be set to either &#x60;s0.d1.small&#x60;, &#x60;s0.d1.medium&#x60;, &#x60;s1.c1.small&#x60;, &#x60;s1.c1.medium&#x60;, &#x60;s1.c2.medium&#x60;, &#x60;s1.c2.large&#x60;, &#x60;s1.e1.small&#x60;, &#x60;s1.e1.medium&#x60;, &#x60;s1.e1.large&#x60;, &#x60;s2.c1.small&#x60;, &#x60;s2.c1.medium&#x60;, &#x60;s2.c1.large&#x60;, &#x60;s2.c2.small&#x60;, &#x60;s2.c2.medium&#x60;, &#x60;s2.c2.large&#x60;, &#x60;d1.c1.small&#x60;, &#x60;d1.c2.small&#x60;, &#x60;d1.c3.small&#x60;, &#x60;d1.c4.small&#x60;, &#x60;d1.c1.medium&#x60;, &#x60;d1.c2.medium&#x60;, &#x60;d1.c3.medium&#x60;, &#x60;d1.c4.medium&#x60;, &#x60;d1.c1.large&#x60;, &#x60;d1.c2.large&#x60;, &#x60;d1.c3.large&#x60;, &#x60;d1.c4.large&#x60;, &#x60;d1.m1.medium&#x60;, &#x60;d1.m2.medium&#x60;, &#x60;d1.m3.medium&#x60;, &#x60;d1.m4.medium&#x60;, &#x60;d2.c1.medium&#x60;, &#x60;d2.c2.medium&#x60;, &#x60;d2.c3.medium&#x60;, &#x60;d2.c4.medium&#x60;, &#x60;d2.c5.medium&#x60;, &#x60;d2.c1.large&#x60;, &#x60;d2.c2.large&#x60;, &#x60;d2.c3.large&#x60;, &#x60;d2.c4.large&#x60;, &#x60;d2.c5.large&#x60;, &#x60;d2.m1.medium&#x60;, &#x60;d2.m1.large&#x60;, &#x60;d2.m2.medium&#x60;, &#x60;d2.m2.large&#x60;, &#x60;d2.m2.xlarge&#x60;, &#x60;d2.c4.db1.pliops1&#x60;, &#x60;d3.m4.xlarge&#x60;, &#x60;d3.m5.xlarge&#x60;, &#x60;d3.m6.xlarge&#x60; or &#x60;a1.c5.large&#x60;. | 
**location** | **str** | Server location ID. Cannot be changed once a server is created. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | 
**description** | **str** | Description of server. | [optional] 
**install_default_ssh_keys** | **bool** | Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request. | [optional]  if omitted the server will use the default value of True
**ssh_keys** | **[str]** | A list of SSH keys that will be installed on the server. | [optional] 
**ssh_key_ids** | **[str]** | A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request. | [optional] 
**reservation_id** | **str** | Server reservation ID. | [optional] 
**pricing_model** | **str** | Server pricing model. Currently this field should be set to &#x60;HOURLY&#x60;, &#x60;ONE_MONTH_RESERVATION&#x60;, &#x60;TWELVE_MONTHS_RESERVATION&#x60;, &#x60;TWENTY_FOUR_MONTHS_RESERVATION&#x60; or &#x60;THIRTY_SIX_MONTHS_RESERVATION&#x60;. | [optional]  if omitted the server will use the default value of "HOURLY"
**network_type** | **str** | The type of network configuration for this server.&lt;br&gt; Currently this field should be set to &#x60;PUBLIC_AND_PRIVATE&#x60;, &#x60;PRIVATE_ONLY&#x60;, &#x60;PUBLIC_ONLY&#x60; or &#x60;USER_DEFINED&#x60;.&lt;br&gt; Setting the &#x60;force&#x60; query parameter to &#x60;true&#x60; allows you to configure network configuration type as &#x60;NONE&#x60;. | [optional]  if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"
**os_configuration** | [**OsConfiguration**](OsConfiguration.md) |  | [optional] 
**tags** | [**[TagAssignmentRequest]**](TagAssignmentRequest.md) | Tags to set to the server. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview). | [optional] 
**network_configuration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**storage_configuration** | [**StorageConfiguration**](StorageConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


