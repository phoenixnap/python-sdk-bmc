# coding: utf-8

"""
    Network Storage API

    Create, list, edit, and delete storage networks with the Network Storage API. Use storage networks to expand storage capacity on a private network. <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bare-metal-cloud-storage' target='_blank'>here</a> </span> <br> <b>All URLs are relative to (https://api.phoenixnap.com/network-storage/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from pnap_network_storage_api.version import VERSION
from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pnap-network-storage-api"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
  "urllib3 >= 1.25.3, < 2.1.0",
  "python-dateutil",
  "pydantic >= 2",
  "typing-extensions >= 4.7.1",
]

def readme():
	with open('README.md', encoding='utf-8') as f:
		return f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Network Storage API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="https://phoenixnap.com/bare-metal-cloud",
    keywords=["OpenAPI", "OpenAPI-Generator", "Network Storage API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type="text/markdown",
    long_description=readme(),
    package_data={"pnap_network_storage_api": ["py.typed"]},
    project_urls={
      'Repository': 'https://github.com/phoenixnap/python-sdk-bmc'
    }
)
