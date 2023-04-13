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
    from pnap_bmc_api.model.tag_assignment_request import TagAssignmentRequest
    globals()['NetworkConfiguration'] = NetworkConfiguration
    globals()['OsConfiguration'] = OsConfiguration
    globals()['TagAssignmentRequest'] = TagAssignmentRequest


class ServerCreate(ModelNormal):
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
        ('description',): {
            'max_length': 250,
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
            'hostname': (str,),  # noqa: E501
            'os': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'install_default_ssh_keys': (bool,),  # noqa: E501
            'ssh_keys': ([str],),  # noqa: E501
            'ssh_key_ids': ([str],),  # noqa: E501
            'reservation_id': (str,),  # noqa: E501
            'pricing_model': (str,),  # noqa: E501
            'network_type': (str,),  # noqa: E501
            'os_configuration': (OsConfiguration,),  # noqa: E501
            'tags': ([TagAssignmentRequest],),  # noqa: E501
            'network_configuration': (NetworkConfiguration,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'hostname': 'hostname',  # noqa: E501
        'os': 'os',  # noqa: E501
        'type': 'type',  # noqa: E501
        'location': 'location',  # noqa: E501
        'description': 'description',  # noqa: E501
        'install_default_ssh_keys': 'installDefaultSshKeys',  # noqa: E501
        'ssh_keys': 'sshKeys',  # noqa: E501
        'ssh_key_ids': 'sshKeyIds',  # noqa: E501
        'reservation_id': 'reservationId',  # noqa: E501
        'pricing_model': 'pricingModel',  # noqa: E501
        'network_type': 'networkType',  # noqa: E501
        'os_configuration': 'osConfiguration',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'network_configuration': 'networkConfiguration',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, hostname, os, type, location, *args, **kwargs):  # noqa: E501
        """ServerCreate - a model defined in OpenAPI

        Args:
            hostname (str): Hostname of server.
            os (str): The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `esxi/esxi70`, `debian/bullseye`, `proxmox/bullseye`, `netris/controller`, `netris/softgate_1g` or `netris/softgate_10g`.
            type (str): Server type ID. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `d1.c1.small`, `d1.c2.small`, `d1.c3.small`, `d1.c4.small`, `d1.c1.medium`, `d1.c2.medium`, `d1.c3.medium`, `d1.c4.medium`, `d1.c1.large`, `d1.c2.large`, `d1.c3.large`, `d1.c4.large`, `d1.m1.medium`, `d1.m2.medium`, `d1.m3.medium`, `d1.m4.medium`, `d2.c1.medium`, `d2.c2.medium`, `d2.c3.medium`, `d2.c4.medium`, `d2.c5.medium`, `d2.c1.large`, `d2.c2.large`, `d2.c3.large`, `d2.c4.large`, `d2.c5.large`, `d2.m1.medium`, `d2.m1.large`, `d2.m2.medium`, `d2.m2.large`, `d2.m2.xlarge`, `d2.c4.storage.pliops1`, `d3.m4.xlarge`, `d3.m5.xlarge` or `d3.m6.xlarge`.
            location (str): Server location ID. Cannot be changed once a server is created. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.

        Keyword Args:
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
            install_default_ssh_keys (bool): Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request.. [optional] if omitted the server will use the default value of True  # noqa: E501
            ssh_keys ([str]): A list of SSH keys that will be installed on the server.. [optional]  # noqa: E501
            ssh_key_ids ([str]): A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request.. [optional]  # noqa: E501
            reservation_id (str): Server reservation ID.. [optional]  # noqa: E501
            pricing_model (str): Server pricing model. Currently this field should be set to `HOURLY`, `ONE_MONTH_RESERVATION`, `TWELVE_MONTHS_RESERVATION`, `TWENTY_FOUR_MONTHS_RESERVATION` or `THIRTY_SIX_MONTHS_RESERVATION`.. [optional] if omitted the server will use the default value of "HOURLY"  # noqa: E501
            network_type (str): The type of network configuration for this server. Currently this field should be set to `PUBLIC_AND_PRIVATE` or `PRIVATE_ONLY`.. [optional] if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"  # noqa: E501
            os_configuration (OsConfiguration): [optional]  # noqa: E501
            tags ([TagAssignmentRequest]): Tags to set to the server. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview).. [optional]  # noqa: E501
            network_configuration (NetworkConfiguration): [optional]  # noqa: E501
        """

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

        self.hostname = hostname
        self.os = os
        self.type = type
        self.location = location
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
    def __init__(self, hostname, os, type, location, *args, **kwargs):  # noqa: E501
        """ServerCreate - a model defined in OpenAPI

        Args:
            hostname (str): Hostname of server.
            os (str): The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `esxi/esxi70`, `debian/bullseye`, `proxmox/bullseye`, `netris/controller`, `netris/softgate_1g` or `netris/softgate_10g`.
            type (str): Server type ID. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `d1.c1.small`, `d1.c2.small`, `d1.c3.small`, `d1.c4.small`, `d1.c1.medium`, `d1.c2.medium`, `d1.c3.medium`, `d1.c4.medium`, `d1.c1.large`, `d1.c2.large`, `d1.c3.large`, `d1.c4.large`, `d1.m1.medium`, `d1.m2.medium`, `d1.m3.medium`, `d1.m4.medium`, `d2.c1.medium`, `d2.c2.medium`, `d2.c3.medium`, `d2.c4.medium`, `d2.c5.medium`, `d2.c1.large`, `d2.c2.large`, `d2.c3.large`, `d2.c4.large`, `d2.c5.large`, `d2.m1.medium`, `d2.m1.large`, `d2.m2.medium`, `d2.m2.large`, `d2.m2.xlarge`, `d2.c4.storage.pliops1`, `d3.m4.xlarge`, `d3.m5.xlarge` or `d3.m6.xlarge`.
            location (str): Server location ID. Cannot be changed once a server is created. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.

        Keyword Args:
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
            install_default_ssh_keys (bool): Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request.. [optional] if omitted the server will use the default value of True  # noqa: E501
            ssh_keys ([str]): A list of SSH keys that will be installed on the server.. [optional]  # noqa: E501
            ssh_key_ids ([str]): A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request.. [optional]  # noqa: E501
            reservation_id (str): Server reservation ID.. [optional]  # noqa: E501
            pricing_model (str): Server pricing model. Currently this field should be set to `HOURLY`, `ONE_MONTH_RESERVATION`, `TWELVE_MONTHS_RESERVATION`, `TWENTY_FOUR_MONTHS_RESERVATION` or `THIRTY_SIX_MONTHS_RESERVATION`.. [optional] if omitted the server will use the default value of "HOURLY"  # noqa: E501
            network_type (str): The type of network configuration for this server. Currently this field should be set to `PUBLIC_AND_PRIVATE` or `PRIVATE_ONLY`.. [optional] if omitted the server will use the default value of "PUBLIC_AND_PRIVATE"  # noqa: E501
            os_configuration (OsConfiguration): [optional]  # noqa: E501
            tags ([TagAssignmentRequest]): Tags to set to the server. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview).. [optional]  # noqa: E501
            network_configuration (NetworkConfiguration): [optional]  # noqa: E501
        """

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

        self.hostname = hostname
        self.os = os
        self.type = type
        self.location = location
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
