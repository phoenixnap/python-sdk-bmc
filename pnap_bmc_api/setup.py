"""
    Bare Metal Cloud API

    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API.  Deprovision servers, get or edit SSH key details, assign public IPs, assign servers to networks and a lot more.  Manage your infrastructure more efficiently using just a few simple API calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


from pnap_bmc_api.version import VERSION
from setuptools import setup, find_packages  # noqa: H301

NAME = "pnap-bmc-api"
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
    description="Bare Metal Cloud API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    keywords=["OpenAPI", "OpenAPI-Generator", "Bare Metal Cloud API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type="text/markdown",
    long_description=readme(),
    project_urls={
        'Repository': 'https://github.com/phoenixnap/python-sdk-bmc'
    },
    url='https://phoenixnap.com/bare-metal-cloud'
)
