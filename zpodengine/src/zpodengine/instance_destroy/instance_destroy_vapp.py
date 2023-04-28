from prefect import task

from zpodcommon import models as M
from zpodcommon.lib.vmware import vCenter
from zpodengine.lib import database


@task(task_run_name="{instance_name}: delete vapp")
def instance_destroy_vapp(instance_id: int, instance_name: str):
    print("Delete Instance VAPP")
    with database.get_session_ctx() as session:
        instance = session.get(M.Instance, instance_id)
        with vCenter.auth_by_instance(instance=instance) as vc:
            vc.delete_vapp(f"zPod-{instance.name}")