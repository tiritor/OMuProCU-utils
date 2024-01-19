#!/bin/bash

source .venv/bin/activate
python3 -m grpc_tools.protoc -Isrc/orchestrator_utils/third_party/googleapis -Iprotos --python_out=./src/orchestrator_utils/ --grpc_python_out=./src/orchestrator_utils/ --mypy_out=./src/orchestrator_utils/ bfrt_proto/bfruntime.proto til/md_orchestrator_msg.proto til/til_msg.proto til/orchestrator_msg.proto til/tif_control.proto til/time_measurement.proto # p4/v1/p4runtime.proto p4/v1/p4data.proto p4/config/v1/p4info.proto p4/config/v1/p4types.proto

echo -e "!!!IMPORTANT!!! The import paths of the generated Protobuf bindings must be set to **relative**, because the paths of the package are relative! "