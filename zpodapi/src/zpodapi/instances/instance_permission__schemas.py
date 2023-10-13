from zpodapi.lib.schema_base import Field, SchemaBase
from zpodcommon import enums

from ..permission_groups.permission_group__schemas import PermissionGroupView
from ..users.user__schemas import UserView


class D:
    id = {"example": 1}
    permission = {"example": enums.InstancePermission.OWNER}
    user_id = {"example": 1}
    username = {"example": "jdoe"}
    group_id = {"example": 1}
    groupname = {"example": "admins"}


class InstancePermissionView(SchemaBase):
    id: int = Field(..., D.id)
    permission: enums.InstancePermission = Field(..., D.permission)
    users: list[UserView] = []
    permission_groups: list[PermissionGroupView] = []


class InstancePermissionUserAddRemove(SchemaBase):
    user_id: int = Field(None, D.user_id)
    username: str = Field(None, D.username)


class InstancePermissionGroupAddRemove(SchemaBase):
    group_id: int = Field(None, D.group_id)
    groupname: str = Field(None, D.groupname)
