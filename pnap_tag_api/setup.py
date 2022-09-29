"""
    Tags API

    Tags are case-sensitive key-value pairs that simplify resource management. The Tag Manager API allows you to create and manage such tags to later assign them to related resources in your Bare Metal Cloud (through the respective resource apis) in order to group and categorize them.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#server-tag-manager-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/tag-manager/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


from pnap_tag_api.version import VERSION
from setuptools import setup, find_packages  # noqa: H301

NAME = "pnap-tag-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

def readme():
	with open('README.md', encoding='utf-8') as f:
		return f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Tags API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="https://phoenixnap.com/bare-metal-cloud",
    keywords=["OpenAPI", "OpenAPI-Generator", "Tags API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type="text/markdown",
    long_description=readme(),
    project_urls={
      'Repository': 'https://github.com/phoenixnap/python-sdk-bmc'
    }
)
