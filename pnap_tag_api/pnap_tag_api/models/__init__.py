# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from pnap_tag_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from pnap_tag_api.model.delete_result import DeleteResult
from pnap_tag_api.model.error import Error
from pnap_tag_api.model.resource_assignment import ResourceAssignment
from pnap_tag_api.model.tag import Tag
from pnap_tag_api.model.tag_create import TagCreate
from pnap_tag_api.model.tag_update import TagUpdate
