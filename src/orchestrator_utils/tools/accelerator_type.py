

from enum import Enum

from ..til.orchestrator_msg_pb2 import ACCELERATOR_TYPE_BMV2, ACCELERATOR_TYPE_TNA, ACCELERATOR_TYPE_UNSPECIFIED


class AcceleratorType(Enum):
    NONE = None
    BMv2 = "bmv2"
    TNA = "tofino"


def find_protobuf_acceleratorTypeEnum(value):
    if value == AcceleratorType.BMv2.value:
        return ACCELERATOR_TYPE_BMV2
    elif value == AcceleratorType.TNA.value:
        return ACCELERATOR_TYPE_TNA
    else:
        return ACCELERATOR_TYPE_UNSPECIFIED

def find_python_acceleratorTypeEnum(protobuf_value):
    if protobuf_value == ACCELERATOR_TYPE_TNA:
        return AcceleratorType.TNA
    elif protobuf_value == ACCELERATOR_TYPE_BMV2:
        return AcceleratorType.BMv2
    else:
        return AcceleratorType.NONE
