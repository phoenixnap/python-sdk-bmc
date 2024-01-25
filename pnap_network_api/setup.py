# coding: utf-8

"""
    Networks API

    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.<br> <br> <span class='pnap-api-knowledge-base-link'> Helpful knowledge base articles are available for  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>multi-private backend networks</a> and <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-15' target='_blank'>public networks</a>. </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pnap-network-api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Networks API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Networks API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.&lt;br&gt; &lt;br&gt; &lt;span class&#x3D;&#39;pnap-api-knowledge-base-link&#39;&gt; Helpful knowledge base articles are available for  &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api&#39; target&#x3D;&#39;_blank&#39;&gt;multi-private backend networks&lt;/a&gt; and &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-15&#39; target&#x3D;&#39;_blank&#39;&gt;public networks&lt;/a&gt;. &lt;/span&gt;&lt;br&gt; &lt;br&gt; &lt;b&gt;All URLs are relative to (https://api.phoenixnap.com/networks/v1/)&lt;/b&gt; 
    """,  # noqa: E501
    package_data={"pnap_network_api": ["py.typed"]},
)
