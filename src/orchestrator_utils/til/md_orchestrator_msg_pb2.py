# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: til/md_orchestrator_msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..til import til_msg_pb2 as til_dot_til__msg__pb2
from ..til import tif_control_pb2 as til_dot_tif__control__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtil/md_orchestrator_msg.proto\x12\x03til\x1a\x11til/til_msg.proto\x1a\x15til/tif_control.proto\"\x94\x01\n\x13MDDeploymentMessage\x12\"\n\x1ainfrastructure_device_name\x18\x01 \x01(\t\x12&\n\x1einfrastructure_device_category\x18\x02 \x01(\t\x12\x31\n\x11\x64\x65ploymentMessage\x18\x03 \x01(\x0b\x32\x16.til.DeploymentMessage\"\x8c\x01\n\x13MDDeploymentRequest\x12+\n\x0etenantMetadata\x18\x01 \x01(\x0b\x32\x13.til.TenantMetadata\x12\x35\n\x13mdDeploymentMessage\x18\x02 \x03(\x0b\x32\x18.til.MDDeploymentMessage\x12\x11\n\tmdtdc_raw\x18\x03 \x01(\t\"7\n\x14MDDeploymentResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x85\x01\n\x04\x45\x64ge\x12\x0f\n\x07srcPort\x18\x01 \x01(\r\x12\x10\n\x08\x64\x65stPort\x18\x02 \x01(\r\x12\x11\n\tsrcDpPort\x18\x03 \x01(\r\x12\x12\n\ndestDpPort\x18\x04 \x01(\r\x12\x0e\n\x06weight\x18\x05 \x01(\x02\x12\x0f\n\x07\x65nabled\x18\x06 \x01(\x08\x12\x12\n\ndestDevice\x18\x07 \x01(\t\"\xa8\x03\n\x04Node\x12\x10\n\x08nodeName\x18\x01 \x01(\t\x12=\n\x17orchestratorHealthState\x18\x02 \x01(\x0e\x32\x1c.til.OrchestratorHealthState\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x17\n\x0fOMuProCUAddress\x18\x04 \x01(\t\x12\x17\n\x0fOMuProCUEnabled\x18\x05 \x01(\x08\x12\x18\n\x05\x65\x64ges\x18\x06 \x03(\x0b\x32\t.til.Edge\x12\x1b\n\tlagGroups\x18\x07 \x03(\x0b\x32\x08.til.Lag\x12\x39\n\x11nexthopMapEntries\x18\x08 \x03(\x0b\x32\x1e.til.RoutingTableConfiguration\x12\x37\n\x0fipv4HostEntries\x18\t \x03(\x0b\x32\x1e.til.RoutingTableConfiguration\x12\x36\n\x0e\x61rpHostEntries\x18\n \x03(\x0b\x32\x1e.til.RoutingTableConfiguration\x12(\n\x0b\x64\x65ployments\x18\x0b \x03(\x0b\x32\x13.til.TenantMetadata\"*\n\x0eTopologyUpdate\x12\x18\n\x05nodes\x18\x01 \x03(\x0b\x32\t.til.Node\"\xc1\x01\n\x14\x44\x65ploymentNodeUpdate\x12,\n\x0ftenantMetadatas\x18\x01 \x03(\x0b\x32\x13.til.TenantMetadata\x12\x17\n\x04node\x18\x02 \x01(\x0b\x32\t.til.Node\x12/\n\x10\x64\x65ploymentStatus\x18\x03 \x01(\x0e\x32\x15.til.DeploymentStatus\x12\x31\n\x12mdDeploymentStatus\x18\x04 \x01(\x0e\x32\x15.til.DeploymentStatus\"~\n\x15TopologyUpdateRequest\x12+\n\x0etopologyUpdate\x18\x01 \x01(\x0b\x32\x13.til.TopologyUpdate\x12\x38\n\x15\x64\x65ploymentNodeUpdates\x18\x02 \x03(\x0b\x32\x19.til.DeploymentNodeUpdate\"\xa0\x01\n\x16TopologyUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12+\n\x0etopologyUpdate\x18\x03 \x01(\x0b\x32\x13.til.TopologyUpdate\x12\x38\n\x15\x64\x65ploymentNodeUpdates\x18\x04 \x03(\x0b\x32\x19.til.DeploymentNodeUpdate*\xe1\x01\n\x17OrchestratorHealthState\x12)\n%ORCHESTRATOR_HEALTH_STATE_UNSPECIFIED\x10\x00\x12%\n!ORCHESTRATOR_HEALTH_STATE_OFFLINE\x10\x01\x12%\n!ORCHESTRATOR_HEALTH_STATE_RUNNING\x10\x02\x12&\n\"ORCHESTRATOR_HEALTH_STATE_DISABLED\x10\x03\x12%\n!ORCHESTRATOR_HEALTH_STATE_UNKNOWN\x10\x04\x32\xdb\x02\n\x18MDDeploymentCommunicator\x12=\n\x06\x43reate\x12\x18.til.MDDeploymentRequest\x1a\x19.til.MDDeploymentResponse\x12=\n\x06Update\x12\x18.til.MDDeploymentRequest\x1a\x19.til.MDDeploymentResponse\x12=\n\x06\x44\x65lete\x12\x18.til.MDDeploymentRequest\x1a\x19.til.MDDeploymentResponse\x12>\n\x07\x43leanup\x12\x18.til.MDDeploymentRequest\x1a\x19.til.MDDeploymentResponse\x12\x42\n\x0b\x43heckHealth\x12\x18.til.MDDeploymentRequest\x1a\x19.til.MDDeploymentResponse2\xcc\t\n\x1aTopologyUpdateCommunicator\x12M\n\x12UpdateHealthStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12J\n\x0fGetHealthStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12\x45\n\nUpdateNode\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12\x43\n\x08GetNodes\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12G\n\x0cGetEdgeNodes\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12M\n\x12GetDatacenterNodes\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12K\n\x10GetEndpointNodes\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12L\n\x11GetAllDeviceNodes\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12H\n\rGetDeviceNode\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12N\n\x13SetDeviceNodeStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12N\n\x13GetDeviceNodeStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12X\n\x1dGetDeviceNodeDeploymentStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12X\n\x1dSetDeviceNodeDeploymentStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12Z\n\x1fSetDeviceNodeMDDeploymentStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponse\x12Z\n\x1fGetDeviceNodeMDDeploymentStatus\x12\x1a.til.TopologyUpdateRequest\x1a\x1b.til.TopologyUpdateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'til.md_orchestrator_msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORCHESTRATORHEALTHSTATE']._serialized_start=1526
  _globals['_ORCHESTRATORHEALTHSTATE']._serialized_end=1751
  _globals['_MDDEPLOYMENTMESSAGE']._serialized_start=81
  _globals['_MDDEPLOYMENTMESSAGE']._serialized_end=229
  _globals['_MDDEPLOYMENTREQUEST']._serialized_start=232
  _globals['_MDDEPLOYMENTREQUEST']._serialized_end=372
  _globals['_MDDEPLOYMENTRESPONSE']._serialized_start=374
  _globals['_MDDEPLOYMENTRESPONSE']._serialized_end=429
  _globals['_EDGE']._serialized_start=432
  _globals['_EDGE']._serialized_end=565
  _globals['_NODE']._serialized_start=568
  _globals['_NODE']._serialized_end=992
  _globals['_TOPOLOGYUPDATE']._serialized_start=994
  _globals['_TOPOLOGYUPDATE']._serialized_end=1036
  _globals['_DEPLOYMENTNODEUPDATE']._serialized_start=1039
  _globals['_DEPLOYMENTNODEUPDATE']._serialized_end=1232
  _globals['_TOPOLOGYUPDATEREQUEST']._serialized_start=1234
  _globals['_TOPOLOGYUPDATEREQUEST']._serialized_end=1360
  _globals['_TOPOLOGYUPDATERESPONSE']._serialized_start=1363
  _globals['_TOPOLOGYUPDATERESPONSE']._serialized_end=1523
  _globals['_MDDEPLOYMENTCOMMUNICATOR']._serialized_start=1754
  _globals['_MDDEPLOYMENTCOMMUNICATOR']._serialized_end=2101
  _globals['_TOPOLOGYUPDATECOMMUNICATOR']._serialized_start=2104
  _globals['_TOPOLOGYUPDATECOMMUNICATOR']._serialized_end=3332
# @@protoc_insertion_point(module_scope)