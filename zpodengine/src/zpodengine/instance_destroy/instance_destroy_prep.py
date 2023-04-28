from prefect import task

from zpodcommon import models as M
from zpodcommon.enums import InstanceStatus
from zpodengine.lib import database


@task(task_run_name="{instance_name}: prep")
def instance_destroy_prep(
    instance_id: int,
    instance_name: str,
):
    with database.get_session_ctx() as session:
        instance = session.get(M.Instance, instance_id)
        instance.status = InstanceStatus.DELETING
        session.add(instance)
        session.commit()