from sqlmodel import SQLModel

from zpodapi.lib.service_base import ServiceBase
from zpodcommon import models as M
from zpodcommon.lib import zpodengine

from . import instance__utils
from .instance__enums import InstanceStatusEnum
from .instance__schemas import InstanceCreate, InstanceDelete


class InstanceService(ServiceBase):
    base_model: SQLModel = M.Instance

    def get_all(
        self,
        *,
        name: str | None = None,
    ):
        return self.get_all_filtered(
            base_criteria=[M.Instance.status == InstanceStatusEnum.ACTIVE.value],
            name=name,
        )

    def create(
        self,
        *,
        item_in: InstanceCreate,
        current_user: M.User,
    ):
        instance = self.crud.create(
            item_in=item_in,
            extra=dict(
                status=InstanceStatusEnum.PENDING,
                password=instance__utils.gen_password(),
                permissions=[
                    M.InstancePermission(
                        permission="zpodowner",
                        users=[current_user],
                    )
                ],
            ),
        )
        zpod_engine = zpodengine.ZpodEngine()
        zpod_engine.create_flow_run_by_name(
            flow_name="flow-deploy-instance",
            deployment_name="default",
            instance_id=instance.id,
            profile=instance.profile,
            instance_name=instance.name,
        )
        return instance

    def delete(self, *, instance: SQLModel):
        self.crud.update(
            item=instance,
            item_in=InstanceDelete(status=InstanceStatusEnum.DELETED),
        )
        return None