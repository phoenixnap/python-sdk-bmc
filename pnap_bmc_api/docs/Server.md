# Server

Bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the server. | 
**status** | **str** | The status of the server. | 
**hostname** | **str** | Hostname of server. | 
**os** | **str** | The server’s OS ID used when the server was created. Currently this field should be set to either &#x60;ubuntu/bionic&#x60;, &#x60;ubuntu/focal&#x60;, &#x60;centos/centos7&#x60;, &#x60;centos/centos8&#x60;, &#x60;windows/srv2019std&#x60;, &#x60;windows/srv2019dc&#x60;, &#x60;esxi/esxi70u2&#x60;, &#x60;debian/bullseye&#x60; or &#x60;proxmox/bullseye&#x60;. | 
**type** | **str** | Server type ID. Cannot be changed once a server is created. Currently this field should be set to either &#x60;s0.d1.small&#x60;, &#x60;s0.d1.medium&#x60;, &#x60;s1.c1.small&#x60;, &#x60;s1.c1.medium&#x60;, &#x60;s1.c2.medium&#x60;, &#x60;s1.c2.large&#x60;, &#x60;s1.e1.small&#x60;, &#x60;s1.e1.medium&#x60;, &#x60;s1.e1.large&#x60;, &#x60;s2.c1.small&#x60;, &#x60;s2.c1.medium&#x60;, &#x60;s2.c1.large&#x60;, &#x60;s2.c2.small&#x60;, &#x60;s2.c2.medium&#x60;, &#x60;s2.c2.large&#x60;, &#x60;d1.c1.small&#x60;, &#x60;d1.c2.small&#x60;, &#x60;d1.c3.small&#x60;, &#x60;d1.c4.small&#x60;, &#x60;d1.c1.medium&#x60;, &#x60;d1.c2.medium&#x60;, &#x60;d1.c3.medium&#x60;, &#x60;d1.c4.medium&#x60;, &#x60;d1.c1.large&#x60;, &#x60;d1.c2.large&#x60;, &#x60;d1.c3.large&#x60;, &#x60;d1.c4.large&#x60;, &#x60;d1.m1.medium&#x60;, &#x60;d1.m2.medium&#x60;, &#x60;d1.m3.medium&#x60;, &#x60;d1.m4.medium&#x60;, &#x60;d2.c1.medium&#x60;, &#x60;d2.c2.medium&#x60;, &#x60;d2.c3.medium&#x60;, &#x60;d2.c4.medium&#x60;, &#x60;d2.c5.medium&#x60;, &#x60;d2.c1.large&#x60;, &#x60;d2.c2.large&#x60;, &#x60;d2.c3.large&#x60;, &#x60;d2.c4.large&#x60;, &#x60;d2.c5.large&#x60;, &#x60;d2.m1.medium&#x60;, &#x60;d2.m1.large&#x60;, &#x60;d2.m2.medium&#x60;, &#x60;d2.m2.large&#x60;, &#x60;d2.m2.xlarge&#x60; or &#x60;d2.c4.storage.pliops1&#x60;. | 
**location** | **str** | Server location ID. Cannot be changed once a server is created. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | 
**cpu** | **str** | A description of the machine CPU. | 
**cpu_count** | **int** | The number of CPUs available in the system. | 
**cores_per_cpu** | **int** | The number of physical cores present on each CPU. | 
**cpu_frequency** | **float** | The CPU frequency in GHz. | 
**ram** | **str** | A description of the machine RAM. | 
**storage** | **str** | A description of the machine storage. | 
**private_ip_addresses** | **[str]** | Private IP addresses assigned to server. | 
**public_ip_addresses** | **[str]** | Public IP addresses assigned to server. | 
**network_configuration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | 
**pricing_model** | **str** | The pricing model this server is being billed. Currently this field should be set to &#x60;HOURLY&#x60;, &#x60;ONE_MONTH_RESERVATION&#x60;, &#x60;TWELVE_MONTHS_RESERVATION&#x60;, &#x60;TWENTY_FOUR_MONTHS_RESERVATION&#x60; or &#x60;THIRTY_SIX_MONTHS_RESERVATION&#x60;. | defaults to "HOURLY"
**description** | **str** | Description of server. | [optional] 
**reservation_id** | **str** | The reservation reference id if any. | [optional] 
**password** | **str** | Password set for user Admin on Windows server or user root on ESXi server which will only be returned in response to provisioning a server. | [optional] 
**network_type** | **str** | The type of network configuration for this server. Currently this field should be set to &#x60;PUBLIC_AND_PRIVATE&#x60; or &#x60;PRIVATE_ONLY&#x60;. | [optional]  if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"
**cluster_id** | **str** | The cluster reference id if any. | [optional] 
**tags** | [**[TagAssignment]**](TagAssignment.md) | The tags assigned if any. | [optional] 
**provisioned_on** | **datetime** | Date and time when server was provisioned. | [optional] 
**os_configuration** | [**OsConfiguration**](OsConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


