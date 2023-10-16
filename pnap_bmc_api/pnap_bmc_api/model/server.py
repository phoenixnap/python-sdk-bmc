"""
    Bare Metal Cloud API

    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API.  Deprovision servers, get or edit SSH key details, assign public IPs, assign servers to networks and a lot more.  Manage your infrastructure more efficiently using just a few simple API calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pnap_bmc_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from pnap_bmc_api.exceptions import ApiAttributeError


def lazy_import():
    from pnap_bmc_api.model.network_configuration import NetworkConfiguration
    from pnap_bmc_api.model.os_configuration import OsConfiguration
    from pnap_bmc_api.model.storage_configuration import StorageConfiguration
    from pnap_bmc_api.model.tag_assignment import TagAssignment
    globals()['NetworkConfiguration'] = NetworkConfiguration
    globals()['OsConfiguration'] = OsConfiguration
    globals()['StorageConfiguration'] = StorageConfiguration
    globals()['TagAssignment'] = TagAssignment


class Server(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('hostname',): {
            'max_length': 100,
            'min_length': 1,
            'regex': {
                'pattern': r'^(?=.*[a-zA-Z])([a-zA-Z0-9().-])+$',  # noqa: E501
            },
        },
        ('cpu_count',): {
            'inclusive_minimum': 1,
        },
        ('cores_per_cpu',): {
            'inclusive_minimum': 1,
        },
        ('cpu_frequency',): {
            'inclusive_minimum': 0,
        },
        ('private_ip_addresses',): {
            'min_items': 1,
        },
        ('description',): {
            'max_length': 250,
        },
        ('public_ip_addresses',): {
            'min_items': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'hostname': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'cpu': (str,),  # noqa: E501
            'cpu_count': (int,),  # noqa: E501
            'cores_per_cpu': (int,),  # noqa: E501
            'cpu_frequency': (float,),  # noqa: E501
            'ram': (str,),  # noqa: E501
            'storage': (str,),  # noqa: E501
            'private_ip_addresses': ([str],),  # noqa: E501
            'pricing_model': (str,),  # noqa: E501
            'network_configuration': (NetworkConfiguration,),  # noqa: E501
            'storage_configuration': (StorageConfiguration,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'os': (str,),  # noqa: E501
            'public_ip_addresses': ([str],),  # noqa: E501
            'reservation_id': (str,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'network_type': (str,),  # noqa: E501
            'cluster_id': (str,),  # noqa: E501
            'tags': ([TagAssignment],),  # noqa: E501
            'provisioned_on': (datetime,),  # noqa: E501
            'os_configuration': (OsConfiguration,),  # noqa: E501
            'superseded_by': (str,),  # noqa: E501
            'supersedes': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'hostname': 'hostname',  # noqa: E501
        'type': 'type',  # noqa: E501
        'location': 'location',  # noqa: E501
        'cpu': 'cpu',  # noqa: E501
        'cpu_count': 'cpuCount',  # noqa: E501
        'cores_per_cpu': 'coresPerCpu',  # noqa: E501
        'cpu_frequency': 'cpuFrequency',  # noqa: E501
        'ram': 'ram',  # noqa: E501
        'storage': 'storage',  # noqa: E501
        'private_ip_addresses': 'privateIpAddresses',  # noqa: E501
        'pricing_model': 'pricingModel',  # noqa: E501
        'network_configuration': 'networkConfiguration',  # noqa: E501
        'storage_configuration': 'storageConfiguration',  # noqa: E501
        'description': 'description',  # noqa: E501
        'os': 'os',  # noqa: E501
        'public_ip_addresses': 'publicIpAddresses',  # noqa: E501
        'reservation_id': 'reservationId',  # noqa: E501
        'password': 'password',  # noqa: E501
        'network_type': 'networkType',  # noqa: E501
        'cluster_id': 'clusterId',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'provisioned_on': 'provisionedOn',  # noqa: E501
        'os_configuration': 'osConfiguration',  # noqa: E501
        'superseded_by': 'supersededBy',  # noqa: E501
        'supersedes': 'supersedes',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, status, hostname, type, location, cpu, cpu_count, cores_per_cpu, cpu_frequency, ram, storage, private_ip_addresses, network_configuration, storage_configuration, *args, **kwargs):  # noqa: E501
        """Server - a model defined in OpenAPI

        Args:
            id (str): The unique identifier of the server.
            status (str): The status of the server.
            hostname (str): Hostname of server.
            type (str): Server type ID. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `d1.c1.small`, `d1.c2.small`, `d1.c3.small`, `d1.c4.small`, `d1.c1.medium`, `d1.c2.medium`, `d1.c3.medium`, `d1.c4.medium`, `d1.c1.large`, `d1.c2.large`, `d1.c3.large`, `d1.c4.large`, `d1.m1.medium`, `d1.m2.medium`, `d1.m3.medium`, `d1.m4.medium`, `d2.c1.medium`, `d2.c2.medium`, `d2.c3.medium`, `d2.c4.medium`, `d2.c5.medium`, `d2.c1.large`, `d2.c2.large`, `d2.c3.large`, `d2.c4.large`, `d2.c5.large`, `d2.m1.medium`, `d2.m1.large`, `d2.m2.medium`, `d2.m2.large`, `d2.m2.xlarge`, `d2.c4.db1.pliops1`, `d3.m4.xlarge`, `d3.m5.xlarge`, `d3.m6.xlarge`, `a1.c5.large` or `d3.s5.xlarge`.
            location (str): Server location ID. Cannot be changed once a server is created. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.
            cpu (str): A description of the machine CPU.
            cpu_count (int): The number of CPUs available in the system.
            cores_per_cpu (int): The number of physical cores present on each CPU.
            cpu_frequency (float): The CPU frequency in GHz.
            ram (str): A description of the machine RAM.
            storage (str): A description of the machine storage.
            private_ip_addresses ([str]): Private IP addresses assigned to server.
            network_configuration (NetworkConfiguration):
            storage_configuration (StorageConfiguration):

        Keyword Args:
            pricing_model (str): The pricing model this server is being billed. Currently this field should be set to `HOURLY`, `ONE_MONTH_RESERVATION`, `TWELVE_MONTHS_RESERVATION`, `TWENTY_FOUR_MONTHS_RESERVATION` or `THIRTY_SIX_MONTHS_RESERVATION`.. defaults to "HOURLY"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): Description of server.. [optional]  # noqa: E501
            os (str): The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `esxi/esxi70`, `esxi/esxi80`, `almalinux/almalinux8`, `rockylinux/rockylinux8`, `debian/bullseye`, `proxmox/bullseye`, `netris/controller`, `netris/softgate_1g` or `netris/softgate_10g`.. [optional]  # noqa: E501
            public_ip_addresses ([str]): Public IP addresses assigned to server.. [optional]  # noqa: E501
            reservation_id (str): The reservation reference id if any.. [optional]  # noqa: E501
            password (str): Auto-generated password set for user `Admin` on Windows server, user `root` on ESXi servers, user `root` on Proxmox server and user `netris` on Netris servers.<br> The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference.. [optional]  # noqa: E501
            network_type (str): The type of network configuration for this server. Currently this field should be set to `PUBLIC_AND_PRIVATE`, `PRIVATE_ONLY`, `PUBLIC_ONLY` or `NONE`.. [optional] if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"  # noqa: E501
            cluster_id (str): The cluster reference id if any.. [optional]  # noqa: E501
            tags ([TagAssignment]): The tags assigned if any.. [optional]  # noqa: E501
            provisioned_on (datetime): Date and time when server was provisioned.. [optional]  # noqa: E501
            os_configuration (OsConfiguration): [optional]  # noqa: E501
            superseded_by (str): Unique identifier of the server to which the reservation has been transferred.. [optional]  # noqa: E501
            supersedes (str): Unique identifier of the server from which the reservation has been transferred.. [optional]  # noqa: E501
        """

        pricing_model = kwargs.get('pricing_model', "HOURLY")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.status = status
        self.hostname = hostname
        self.type = type
        self.location = location
        self.cpu = cpu
        self.cpu_count = cpu_count
        self.cores_per_cpu = cores_per_cpu
        self.cpu_frequency = cpu_frequency
        self.ram = ram
        self.storage = storage
        self.private_ip_addresses = private_ip_addresses
        self.pricing_model = pricing_model
        self.network_configuration = network_configuration
        self.storage_configuration = storage_configuration
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, status, hostname, type, location, cpu, cpu_count, cores_per_cpu, cpu_frequency, ram, storage, private_ip_addresses, network_configuration, storage_configuration, *args, **kwargs):  # noqa: E501
        """Server - a model defined in OpenAPI

        Args:
            id (str): The unique identifier of the server.
            status (str): The status of the server.
            hostname (str): Hostname of server.
            type (str): Server type ID. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `d1.c1.small`, `d1.c2.small`, `d1.c3.small`, `d1.c4.small`, `d1.c1.medium`, `d1.c2.medium`, `d1.c3.medium`, `d1.c4.medium`, `d1.c1.large`, `d1.c2.large`, `d1.c3.large`, `d1.c4.large`, `d1.m1.medium`, `d1.m2.medium`, `d1.m3.medium`, `d1.m4.medium`, `d2.c1.medium`, `d2.c2.medium`, `d2.c3.medium`, `d2.c4.medium`, `d2.c5.medium`, `d2.c1.large`, `d2.c2.large`, `d2.c3.large`, `d2.c4.large`, `d2.c5.large`, `d2.m1.medium`, `d2.m1.large`, `d2.m2.medium`, `d2.m2.large`, `d2.m2.xlarge`, `d2.c4.db1.pliops1`, `d3.m4.xlarge`, `d3.m5.xlarge`, `d3.m6.xlarge`, `a1.c5.large` or `d3.s5.xlarge`.
            location (str): Server location ID. Cannot be changed once a server is created. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.
            cpu (str): A description of the machine CPU.
            cpu_count (int): The number of CPUs available in the system.
            cores_per_cpu (int): The number of physical cores present on each CPU.
            cpu_frequency (float): The CPU frequency in GHz.
            ram (str): A description of the machine RAM.
            storage (str): A description of the machine storage.
            private_ip_addresses ([str]): Private IP addresses assigned to server.
            network_configuration (NetworkConfiguration):
            storage_configuration (StorageConfiguration):

        Keyword Args:
            pricing_model (str): The pricing model this server is being billed. Currently this field should be set to `HOURLY`, `ONE_MONTH_RESERVATION`, `TWELVE_MONTHS_RESERVATION`, `TWENTY_FOUR_MONTHS_RESERVATION` or `THIRTY_SIX_MONTHS_RESERVATION`.. defaults to "HOURLY"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): Description of server.. [optional]  # noqa: E501
            os (str): The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `esxi/esxi70`, `esxi/esxi80`, `almalinux/almalinux8`, `rockylinux/rockylinux8`, `debian/bullseye`, `proxmox/bullseye`, `netris/controller`, `netris/softgate_1g` or `netris/softgate_10g`.. [optional]  # noqa: E501
            public_ip_addresses ([str]): Public IP addresses assigned to server.. [optional]  # noqa: E501
            reservation_id (str): The reservation reference id if any.. [optional]  # noqa: E501
            password (str): Auto-generated password set for user `Admin` on Windows server, user `root` on ESXi servers, user `root` on Proxmox server and user `netris` on Netris servers.<br> The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference.. [optional]  # noqa: E501
            network_type (str): The type of network configuration for this server. Currently this field should be set to `PUBLIC_AND_PRIVATE`, `PRIVATE_ONLY`, `PUBLIC_ONLY` or `NONE`.. [optional] if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"  # noqa: E501
            cluster_id (str): The cluster reference id if any.. [optional]  # noqa: E501
            tags ([TagAssignment]): The tags assigned if any.. [optional]  # noqa: E501
            provisioned_on (datetime): Date and time when server was provisioned.. [optional]  # noqa: E501
            os_configuration (OsConfiguration): [optional]  # noqa: E501
            superseded_by (str): Unique identifier of the server to which the reservation has been transferred.. [optional]  # noqa: E501
            supersedes (str): Unique identifier of the server from which the reservation has been transferred.. [optional]  # noqa: E501
        """

        pricing_model = kwargs.get('pricing_model', "HOURLY")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.status = status
        self.hostname = hostname
        self.type = type
        self.location = location
        self.cpu = cpu
        self.cpu_count = cpu_count
        self.cores_per_cpu = cores_per_cpu
        self.cpu_frequency = cpu_frequency
        self.ram = ram
        self.storage = storage
        self.private_ip_addresses = private_ip_addresses
        self.pricing_model = pricing_model
        self.network_configuration = network_configuration
        self.storage_configuration = storage_configuration
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
