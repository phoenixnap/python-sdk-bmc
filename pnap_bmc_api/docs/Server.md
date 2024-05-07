# Server

Bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the server. | 
**status** | **str** | The status of the server. Can have one of the following values: &#x60;creating&#x60; , &#x60;powered-on&#x60; , &#x60;powered-off&#x60; , &#x60;rebooting&#x60; , &#x60;resetting&#x60; , &#x60;deleting&#x60; , &#x60;reserved&#x60; , &#x60;error&#x60; or &#x60;reinstating&#x60;. | 
**hostname** | **str** | Hostname of server. | 
**description** | **str** | Description of server. | [optional] 
**os** | **str** | The server’s OS ID used when the server was created. Currently this field should be set to either &#x60;ubuntu/bionic&#x60;, &#x60;ubuntu/focal&#x60;, &#x60;ubuntu/jammy&#x60;, &#x60;centos/centos7&#x60;, &#x60;centos/centos8&#x60;, &#x60;windows/srv2019std&#x60;, &#x60;windows/srv2019dc&#x60;, &#x60;windows/srv2022std&#x60;, &#x60;windows/srv2022dc&#x60;, &#x60;esxi/esxi70&#x60;, &#x60;esxi/esxi80&#x60;, &#x60;almalinux/almalinux8&#x60;, &#x60;rockylinux/rockylinux8&#x60;, &#x60;almalinux/almalinux9&#x60;, &#x60;rockylinux/rockylinux9&#x60;, &#x60;debian/bullseye&#x60;, &#x60;debian/bookworm&#x60;, &#x60;proxmox/bullseye&#x60;, &#x60;proxmox/proxmox8&#x60;, &#x60;netris/controller&#x60;, &#x60;netris/softgate_1g&#x60;, &#x60;netris/softgate_10g&#x60; or &#x60;netris/softgate_25g&#x60;. | [optional] 
**type** | **str** | Server type ID. Cannot be changed once a server is created. Currently this field should be set to either &#x60;s0.d1.small&#x60;, &#x60;s0.d1.medium&#x60;, &#x60;s1.c1.small&#x60;, &#x60;s1.c1.medium&#x60;, &#x60;s1.c2.medium&#x60;, &#x60;s1.c2.large&#x60;, &#x60;s1.e1.small&#x60;, &#x60;s1.e1.medium&#x60;, &#x60;s1.e1.large&#x60;, &#x60;s2.c1.small&#x60;, &#x60;s2.c1.medium&#x60;, &#x60;s2.c1.large&#x60;, &#x60;s2.c2.small&#x60;, &#x60;s2.c2.medium&#x60;, &#x60;s2.c2.large&#x60;, &#x60;d1.c1.small&#x60;, &#x60;d1.c2.small&#x60;, &#x60;d1.c3.small&#x60;, &#x60;d1.c4.small&#x60;, &#x60;d1.c1.medium&#x60;, &#x60;d1.c2.medium&#x60;, &#x60;d1.c3.medium&#x60;, &#x60;d1.c4.medium&#x60;, &#x60;d1.c1.large&#x60;, &#x60;d1.c2.large&#x60;, &#x60;d1.c3.large&#x60;, &#x60;d1.c4.large&#x60;, &#x60;d1.m1.medium&#x60;, &#x60;d1.m2.medium&#x60;, &#x60;d1.m3.medium&#x60;, &#x60;d1.m4.medium&#x60;, &#x60;d2.c1.medium&#x60;, &#x60;d2.c2.medium&#x60;, &#x60;d2.c3.medium&#x60;, &#x60;d2.c4.medium&#x60;, &#x60;d2.c5.medium&#x60;, &#x60;d2.c1.large&#x60;, &#x60;d2.c2.large&#x60;, &#x60;d2.c3.large&#x60;, &#x60;d2.c4.large&#x60;, &#x60;d2.c5.large&#x60;, &#x60;d2.m1.xlarge&#x60;, &#x60;d2.m2.xxlarge&#x60;, &#x60;d2.m3.xlarge&#x60;, &#x60;d2.m4.xlarge&#x60;, &#x60;d2.m5.xlarge&#x60;, &#x60;d2.c4.db1.pliops1&#x60;, &#x60;d3.m4.xlarge&#x60;, &#x60;d3.m5.xlarge&#x60;, &#x60;d3.m6.xlarge&#x60;, &#x60;a1.c5.large&#x60;, &#x60;d3.s5.xlarge&#x60;, &#x60;d3.m4.xxlarge&#x60;, &#x60;d3.m5.xxlarge&#x60;,  &#x60;d3.m6.xxlarge&#x60;, &#x60;s3.c3.medium&#x60;, &#x60;s3.c3.large&#x60;, &#x60;d3.c4.medium&#x60;, &#x60;d3.c5.medium&#x60;, &#x60;d3.c6.medium&#x60;, &#x60;d3.c1.large&#x60;, &#x60;d3.c2.large&#x60;, &#x60;d3.c3.large&#x60;, &#x60;d3.m1.xlarge&#x60;, &#x60;d3.m2.xlarge&#x60; or &#x60;d3.m3.xlarge&#x60;. | 
**location** | **str** | Server location ID. Cannot be changed once a server is created. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | 
**cpu** | **str** | A description of the machine CPU. | 
**cpu_count** | **int** | The number of CPUs available in the system. | 
**cores_per_cpu** | **int** | The number of physical cores present on each CPU. | 
**cpu_frequency** | **float** | The CPU frequency in GHz. | 
**ram** | **str** | A description of the machine RAM. | 
**storage** | **str** | A description of the machine storage. | 
**private_ip_addresses** | **List[str]** | Private IP addresses assigned to server. | 
**public_ip_addresses** | **List[str]** | Public IP addresses assigned to server. | [optional] 
**reservation_id** | **str** | The reservation reference id if any. | [optional] 
**pricing_model** | **str** | The pricing model this server is being billed. Currently this field should be set to &#x60;HOURLY&#x60;, &#x60;ONE_MONTH_RESERVATION&#x60;, &#x60;TWELVE_MONTHS_RESERVATION&#x60;, &#x60;TWENTY_FOUR_MONTHS_RESERVATION&#x60; or &#x60;THIRTY_SIX_MONTHS_RESERVATION&#x60;. | [default to 'HOURLY']
**password** | **str** | Auto-generated password set for user &#x60;Admin&#x60; on Windows server, user &#x60;root&#x60; on ESXi servers, user &#x60;root&#x60; on Proxmox server and user &#x60;netris&#x60; on Netris servers.&lt;br&gt; The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference. | [optional] 
**network_type** | **str** | The type of network configuration for this server. Currently this field should be set to &#x60;PUBLIC_AND_PRIVATE&#x60;, &#x60;PRIVATE_ONLY&#x60;, &#x60;PUBLIC_ONLY&#x60; or &#x60;NONE&#x60;. | [optional] [default to 'PUBLIC_AND_PRIVATE']
**cluster_id** | **str** | The cluster reference id if any. | [optional] 
**tags** | [**List[TagAssignment]**](TagAssignment.md) | The tags assigned if any. | [optional] 
**provisioned_on** | **datetime** | Date and time when server was provisioned. | [optional] 
**os_configuration** | [**OsConfiguration**](OsConfiguration.md) |  | [optional] 
**network_configuration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | 
**storage_configuration** | [**StorageConfiguration**](StorageConfiguration.md) |  | 
**superseded_by** | **str** | Unique identifier of the server to which the reservation has been transferred. | [optional] 
**supersedes** | **str** | Unique identifier of the server from which the reservation has been transferred. | [optional] 

## Example

```python
from pnap_bmc_api.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print Server.to_json()

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_form_dict = server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


