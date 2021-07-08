from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

import json

class AzureService(object):
    def __init__(self):
        self.driver = None

    def connect_driver(self, ten_id, sub_id, app_id, password):
        cls = get_driver(Provider.AZURE_ARM)
        self.driver = cls(tenant_id=ten_id, subscription_id=sub_id,
                          key=app_id, secret=password)

    def get_nodes(self):
        return self.driver.list_nodes()

    def get_subnets(self, network):
        return self.driver.ex_list_subnets(network)

    def get_vnet(self):
        return self.driver.ex_list_networks()

    def get_nics(self, resource_group):
        return self.driver.ex_list_nics(resource_group=resource_group)

    def get_resource_groups(self):
        return self.driver.ex_list_resource_groups()
        


az = AzureService()
az.connect_driver("b9db4e90-e1e0-46c8-ac77-25cc6454e1d9", "f6bba0a0-dbcc-466e-87b0-9e6aaa23a9f7", "edb3179f-45b6-4501-94c6-5ad2c453a5f2", "iU_4x6dAuQacnO?_6U.7_D2U/ukc53]p")
zn = None
for n in az.get_vnet():
    if "zymr" in n.name:
        zn = n
        break

print(json.dumps(zn.extra, indent=4))
