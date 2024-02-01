# coding: utf-8

import os
import codecs

"""
    IP Addresses API

    Public IP blocks are a set of contiguous IPs that allow you to access your servers or networks from the internet. Use the IP Addresses API to request and delete IP blocks.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/public-ip-management#bmc-public-ip-allocations-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/ips/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from pnap_ip_api.version import VERSION
from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

NAME = "pnap-ip-api"
VERSION = VERSION

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
    description="IP Addresses API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "IP Addresses API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Public IP blocks are a set of contiguous IPs that allow you to access your servers or networks from the internet. Use the IP Addresses API to request and delete IP blocks.&lt;br&gt; &lt;br&gt; &lt;span class&#x3D;&#39;pnap-api-knowledge-base-link&#39;&gt; Knowledge base articles to help you can be found &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/public-ip-management#bmc-public-ip-allocations-api&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt; &lt;/span&gt;&lt;br&gt; &lt;br&gt; &lt;b&gt;All URLs are relative to (https://api.phoenixnap.com/ips/v1/)&lt;/b&gt; 
    """,  # noqa: E501
    package_data={"pnap_ip_api": ["py.typed"]},
)
