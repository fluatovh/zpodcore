from prefect import task

from zpodcommon import models as M
from zpodcommon.lib.network import create_dnsmasq_config, get_primary_subnet_ip
from zpodengine.lib import database


@task(task_run_name="{instance_name}: configure dnsmasq")
def instance_deploy_dnsmasq(
    instance_id: int,
    instance_name: str,
):
    with database.get_session_ctx() as session:
        instance = session.get(M.Instance, instance_id)

        # Fetch associate zbox IP from subnet
        dns_ip = get_primary_subnet_ip(instance, "zbox")

        # Create dnsmasq configuration
        create_dnsmasq_config(instance.name, instance.domain, dns_ip)