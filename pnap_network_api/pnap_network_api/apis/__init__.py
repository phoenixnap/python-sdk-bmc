
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from pnap_network_api.api.private_networks_api import PrivateNetworksApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from pnap_network_api.api.private_networks_api import PrivateNetworksApi
from pnap_network_api.api.public_networks_api import PublicNetworksApi
