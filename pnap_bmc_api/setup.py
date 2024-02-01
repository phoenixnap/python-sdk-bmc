# coding: utf-8

import os
import codecs

"""
    Bare Metal Cloud API

    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API.  Deprovision servers, get or edit SSH key details, assign public IPs, assign servers to networks and a lot more.  Manage your infrastructure more efficiently using just a few simple API calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)</b> 

    The version of the OpenAPI document: 0.1
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

def get_version():
  here = os.path.abspath(os.path.dirname(__file__))
  with codecs.open(os.path.join(here, './pnap_bmc_api/VERSION')) as fp:
	  return fp.read()

NAME = "pnap-bmc-api"
VERSION = get_version()

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
    description="Bare Metal Cloud API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Bare Metal Cloud API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API.  Deprovision servers, get or edit SSH key details, assign public IPs, assign servers to networks and a lot more.  Manage your infrastructure more efficiently using just a few simple API calls.&lt;br&gt; &lt;br&gt; &lt;span class&#x3D;&#39;pnap-api-knowledge-base-link&#39;&gt; Knowledge base articles to help you can be found &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt; &lt;/span&gt;&lt;br&gt; &lt;br&gt; &lt;b&gt;All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)&lt;/b&gt; 
    """,  # noqa: E501
    package_data={"pnap_bmc_api": ["py.typed"]},
)
