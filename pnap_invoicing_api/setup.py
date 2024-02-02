# coding: utf-8

"""
    Invoicing API

    List, fetch and pay invoices with the Invoicing API. 

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
NAME = "pnap-invoicing-api"
VERSION = "1.0.1-SNAPSHOT"
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
    description="Invoicing API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Invoicing API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    List, fetch and pay invoices with the Invoicing API. 
    """,  # noqa: E501
    package_data={"pnap_invoicing_api": ["py.typed"]},
)
