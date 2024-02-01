# coding: utf-8

import os
import codecs

"""
    Payments API

    Payments API are currently designed to fetch Transactions only.

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
  with codecs.open(os.path.join(here, './pnap_payments_api/VERSION')) as fp:
	  return fp.read()

NAME = "pnap-payments-api"
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
    description="Payments API",
    author="PhoenixNAP Team",
    author_email="support@phoenixnap.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Payments API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Payments API are currently designed to fetch Transactions only.
    """,  # noqa: E501
    package_data={"pnap_payments_api": ["py.typed"]},
)
