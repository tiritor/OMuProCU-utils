

from enum import Enum
import logging
import grpc
import yaml

from .logger.logger import init_logger
from .til.tif_control_pb2 import RoutingTableConfiguration
from .til.til_msg_pb2 import RuntimeRule
from .til.orchestrator_msg_pb2 import TIFControlRequest
from .til import md_orchestrator_msg_pb2_grpc
from .til.md_orchestrator_msg_pb2 import MDDeploymentRequest, MDDeploymentResponse, MDRulesUpdateRequest, MDRulesUpdateResponse

class TableCategory(Enum):
    PROVIDER_TABLES = "provider_tables"
    TENANT_TABLES = "tenant_tables"


class MDOMuProCUClient(object):
    """
    docstring
    """
    
    def __init__(self, MDOMuProCUAddress : str, log_level = logging.DEBUG) -> None:
        self.address = MDOMuProCUAddress
        self.channel = grpc.insecure_channel(MDOMuProCUAddress)
        self.md_orchestrator_stub = md_orchestrator_msg_pb2_grpc.MDDeploymentCommunicatorStub(self.channel)
        self.md_rulesupdater_stub = md_orchestrator_msg_pb2_grpc.MDRulesUpdaterCommunicatorStub(self.channel)
        self.logger = init_logger(self.__class__.__name__, level=log_level)

    def close(self):
        """
        docstring
        """
        self.channel.close()

    def create(self, mdtdc_path):
        """
        docstring
        """
        mdtdc = None
        with open(mdtdc_path) as f:
            mdtdc = f.read()
        resp : MDDeploymentResponse = self.md_orchestrator_stub.Create(
            MDDeploymentRequest(
                mdtdc_raw = mdtdc
            )
        )
        self.logger.debug(resp)
        return resp

    def update(self, mdtdc_path):
        """
        docstring
        """
        mdtdc = None
        with open(mdtdc_path) as f:
            mdtdc = f.read()
        resp : MDDeploymentResponse = self.md_orchestrator_stub.Update(
            MDDeploymentRequest(
                mdtdc_raw = mdtdc
            )
        )
        self.logger.debug(resp)
        return resp

    def delete(self, mdtdc_path):
        """
        docstring
        """
        mdtdc = None
        with open(mdtdc_path) as f:
            mdtdc = f.read()
        resp : MDDeploymentResponse = self.md_orchestrator_stub.Delete(
            MDDeploymentRequest(
                mdtdc_raw = mdtdc
            )
        )
        self.logger.debug(resp)
        return resp
    
    def check_health(self):
        """
        docstring
        """
        resp : MDDeploymentResponse = self.md_orchestrator_stub.CheckHealth(
            MDDeploymentRequest()
        )
        self.logger.debug(resp)
        return resp

    def cleanup(self):
        """
        docstring
        """
        resp : MDDeploymentResponse = self.md_orchestrator_stub.Cleanup(
            MDDeploymentRequest(
            )
        )
        self.logger.debug(resp)
        return resp

    def create_md_rules(self, arg = None, md_rules_path = None, tableCategory : TableCategory = None):
        """
        docstring
        """
        md_rules = None
        md_rules_per_device = None
        if md_rules_path is not None:
            with open(md_rules_path) as f:
                md_rules_per_device = yaml.safe_load(f)
        elif arg is not None:
            if tableCategory is None:
                raise ValueError("tableCategory cannot be None")
            md_rules = arg
            if len(md_rules) == 0:
                raise ValueError("arg cannot be empty")
            elif len(md_rules) == 4:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: {
                            md_rules[1]: {
                                md_rules[2]: md_rules[3]
                            }
                        }
                    }
                }
            elif len(md_rules) == 5:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: [
                            {
                                "table_name": md_rules[1],
                                "match_fields": md_rules[2],
                                "action_name": md_rules[3],
                                "action_params": md_rules[4]
                            }
                        ]
                    }
                }
            elif len(md_rules) <= 4 and tableCategory == TableCategory.TENANT_TABLES:
                raise ValueError("arg must have at 5 elements (device_name table_name match_fields action_name action_params)")
            elif len(md_rules) <= 3 and tableCategory == TableCategory.PROVIDER_TABLES:
                raise ValueError("arg must have at 4 elements (device_name table_name key nextHopId)")
            else:
                raise ValueError("arg has too many arguments and must have 4 or 5 arguments! (device_name table_name key nextHopId) or (device_name table_name match_fields action_name action_params")
        else:
            raise ValueError("md_rules_path or arg cannot be None")
        nextHopEntries = []
        ipv4HostEntries = []
        arpHostEntries = []
        runtimeRules = []
        tifControlRequests = []
        print(md_rules_per_device)
        for dev, table_category in md_rules_per_device.items():
            for category, tables in table_category.items():
                print(tables)
                if category == TableCategory.PROVIDER_TABLES.value:
                    for name, table in tables.items():
                        print(name)
                        if name == "nexthop_map" and name == "nexthop":
                            for key, entry in table.items():
                                nextHopEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                        elif name == "ipv4_host":
                            print(tables)
                            for key, entry in table.items():
                                print(entry)
                                ipv4HostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                        elif name == "arp_host":
                            for key, entry in table.values():
                                arpHostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                elif category == TableCategory.TENANT_TABLES.value:
                    for entry in tables:
                        print(entry)
                        runtimeRules.append(RuntimeRule(
                            table=entry["table_name"],
                            matches=[entry["match_fields"]],
                            actionName=entry["action_name"],
                            actionParams=[entry["action_params"]]
                        ))
                        print(runtimeRules)
            tifControlRequests.append({
                    "nextHopEntries" : nextHopEntries,
                    "ipv4HostEntries" : ipv4HostEntries,
                    "arpHostEntries" : arpHostEntries,
                    "runtimeRules" : runtimeRules
                })
        resp : MDRulesUpdateResponse = self.md_rulesupdater_stub.CreateRule(
            MDRulesUpdateRequest(
                infrastructureDeviceNames=[dev for dev in md_rules_per_device.keys()],
                tifControlRequests=[TIFControlRequest(
                    nexthopMapEntries=request["nextHopEntries"],
                    ipv4HostEntries=request["ipv4HostEntries"],
                    arpHostEntries=request["arpHostEntries"],
                    runtimeRules=request["runtimeRules"]
                ) for request in tifControlRequests]
            )
        )
        self.logger.debug(resp)
        return resp

    def update_md_rules(self, arg = None, md_rules_path = None, tableCategory : TableCategory = None):
        """
        docstring
        """
        md_rules = None
        md_rules_per_device = None
        if md_rules_path is not None:
            with open(md_rules_path) as f:
                md_rules_per_device = yaml.safe_load(f)
        elif arg is not None:
            if tableCategory is None:
                raise ValueError("tableCategory cannot be None")
            md_rules = arg
            if len(md_rules) == 0:
                raise ValueError("arg cannot be empty")
            elif len(md_rules) == 4:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: {
                            md_rules[1]: {
                                md_rules[2]: md_rules[3]
                            }
                        }
                    }
                }
            elif len(md_rules) == 5:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: [
                            {
                                "table_name": md_rules[1],
                                "match_fields": md_rules[2],
                                "action_name": md_rules[3],
                                "action_params": md_rules[4]
                            }
                        ]
                    }
                }
            elif len(md_rules) <= 4 and tableCategory == TableCategory.TENANT_TABLES:
                raise ValueError("arg must have at 5 elements (device_name table_name match_fields action_name action_params)")
            elif len(md_rules) <= 3 and tableCategory == TableCategory.PROVIDER_TABLES:
                raise ValueError("arg must have at 4 elements (device_name table_name key nextHopId)")
            else:
                raise ValueError("arg has too many arguments and must have 4 or 5 arguments! (device_name table_name key nextHopId) or (device_name table_name match_fields action_name action_params")
        else:
            raise ValueError("md_rules_path or arg cannot be None")
        nextHopEntries = []
        ipv4HostEntries = []
        arpHostEntries = []
        runtimeRules = []
        tifControlRequests = []
        print(md_rules_per_device)
        for dev, table_category in md_rules_per_device.items():
            for category, tables in table_category.items():
                print(tables)
                if category == TableCategory.PROVIDER_TABLES.value:
                    for name, table in tables.items():
                        print(name)
                        if name == "nexthop_map" and name == "nexthop":
                            for key, entry in table.items():
                                nextHopEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                        elif name == "ipv4_host":
                            print(tables)
                            for key, entry in table.items():
                                print(entry)
                                ipv4HostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                        elif name == "arp_host":
                            for key, entry in table.values():
                                arpHostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(entry)
                                ))
                elif category == TableCategory.TENANT_TABLES.value:
                    for entry in tables:
                        print(entry)
                        runtimeRules.append(RuntimeRule(
                            table=entry["table_name"],
                            matches=[entry["match_fields"]],
                            actionName=entry["action_name"],
                            actionParams=[entry["action_params"]]
                        ))
            tifControlRequests.append({
                    "nextHopEntries" : nextHopEntries,
                    "ipv4HostEntries" : ipv4HostEntries,
                    "arpHostEntries" : arpHostEntries,
                    "runtimeRules" : runtimeRules
                })
        resp : MDRulesUpdateResponse = self.md_rulesupdater_stub.UpdateRule(
            MDRulesUpdateRequest(
                infrastructureDeviceNames=[dev for dev in md_rules_per_device.keys()],
                tifControlRequests=[TIFControlRequest(
                    nexthopMapEntries=request["nextHopEntries"],
                    ipv4HostEntries=request["ipv4HostEntries"],
                    arpHostEntries=request["arpHostEntries"],
                    runtimeRules=request["runtimeRules"]
                ) for request in tifControlRequests]
            )
        )
        self.logger.debug(resp)
        return resp
    
    def delete_md_rules(self, arg = None, md_rules_path = None, tableCategory : TableCategory = None):
        """
        docstring
        """
        md_rules = None
        md_rules_per_device = None
        if md_rules_path is not None:
            with open(md_rules_path) as f:
                md_rules_per_device = yaml.safe_load(f)
        elif arg is not None:
            if tableCategory is None:
                raise ValueError("tableCategory cannot be None")
            md_rules = arg
            if len(md_rules) == 0:
                raise ValueError("arg cannot be empty")
            elif len(md_rules) == 4:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: {
                            md_rules[1]: {
                                md_rules[2]: md_rules[3]
                            }
                        }
                    }
                }
            elif len(md_rules) == 5:
                md_rules_per_device = {
                    md_rules[0]: {
                        tableCategory.value: [
                            {
                                "table_name": md_rules[1],
                                "match_fields": md_rules[2],
                                "action_name": md_rules[3],
                                "action_params": md_rules[4]
                            }
                        ]
                    }
                }
            elif len(md_rules) <= 4 and tableCategory == TableCategory.TENANT_TABLES:
                raise ValueError("arg must have at 5 elements (device_name table_name match_fields action_name action_params)")
            elif len(md_rules) <= 3 and tableCategory == TableCategory.PROVIDER_TABLES:
                raise ValueError("arg must have at 4 elements (device_name table_name key nextHopId)")
            else:
                raise ValueError("arg has too many arguments and must have 4 or 5 arguments! (device_name table_name key nextHopId) or (device_name table_name match_fields action_name action_params")
        else:
            raise ValueError("md_rules_path or arg cannot be None")
        nextHopEntries = []
        ipv4HostEntries = []
        arpHostEntries = []
        runtimeRules = []
        tifControlRequests = []
        for dev, table_category in md_rules_per_device.items():
            for category, tables in table_category.items():
                if category == TableCategory.PROVIDER_TABLES.value:
                    for name, table in tables.items():
                        if name == "nexthop_map" and name == "nexthop":
                            for key, value in table.items():
                                nextHopEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(value)
                                ))
                        elif name == "ipv4_host":
                            for key, value in table.items():
                                ipv4HostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(value)
                                ))
                        elif name == "arp_table":
                            for key, value in table.items():
                                arpHostEntries.append(RoutingTableConfiguration(
                                    key=str(key),
                                    nextHopId=int(value)
                                ))
                elif category == TableCategory.TENANT_TABLES.value:
                    for entry in tables:
                        runtimeRules.append(RuntimeRule(
                            table=entry["table_name"],
                            matches=[entry["match_fields"]],
                            actionName=entry["action_name"],
                            actionParams=[entry["action_params"]]
                        ))
                tifControlRequests.append(TIFControlRequest(
                        nexthopMapEntries=nextHopEntries,
                        ipv4HostEntries=ipv4HostEntries,
                        arpHostEntries=arpHostEntries,
                        runtimeRules=runtimeRules
                    ))
        resp : MDRulesUpdateResponse = self.md_rulesupdater_stub.DeleteRule(
            MDRulesUpdateRequest(
                infrastructureDeviceNames=[dev for dev in md_rules_per_device.keys()],
                tifControlRequests=tifControlRequests
            )
        )
        self.logger.debug(resp)
        return resp
    
    def get_md_rules(self, dev : str = None, table : str = None, tableCategory : TableCategory = None):
        """
        docstring
        """
        # FIXME: This must be improved
        if dev is None:
            raise ValueError("dev cannot be None")
        if table is None:
            raise ValueError("table cannot be None")
        if tableCategory is None:
            raise ValueError("tableCategory cannot be None")
        # with open(md_rules_path) as f:
        #     md_rules_per_device = yaml.safe_load(f)
        nextHopEntries = []
        ipv4HostEntries = []
        arpHostEntries = []
        runtimeRules = []
        tifControlRequests = []
        # for dev, table_category in md_rules_per_device.items():
        if tableCategory == TableCategory.PROVIDER_TABLES:
            if table.key() == "nexthop_map":
                for entry in table.values():
                    nextHopEntries.append(RoutingTableConfiguration(
                        key=entry.key(),
                        nextHopId=entry.value()
                    ))
            elif table["table_name"] == "ipv4_host":
                for entry in table.values():
                    ipv4HostEntries.append(RoutingTableConfiguration(
                        key=entry.key(),
                        nextHopId=entry.value()
                    ))
            elif table["table_name"] == "arp_host":
                for entry in table.values():
                    arpHostEntries.append(RoutingTableConfiguration(
                        key=entry.key(),
                        nextHopId=entry.value()
                    ))
        elif tableCategory == TableCategory.TENANT_TABLES:
            runtimeRules.append(RuntimeRule(
                table_name=table["table_name"],
            ))
            tifControlRequests.append(TIFControlRequest(
                    nexthopMapEntries=nextHopEntries,
                    ipv4HostEntries=ipv4HostEntries,
                    arpHostEntries=arpHostEntries,
                    runtimeRules=runtimeRules
            ))
        # resp : MDRulesUpdateResponse = self.md_rulesupdater_stub.GetRule(
        #     MDRulesUpdateRequest(
        #         infrastructureDeviceNames=[dev for dev in md_rules_per_device.keys()],
        #         tifControlRequests=tifControlRequests
        #     )
        # )
        # self.logger.debug(resp)
        # return resp