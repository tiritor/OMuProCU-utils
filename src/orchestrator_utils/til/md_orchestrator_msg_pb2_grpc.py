# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..til import md_orchestrator_msg_pb2 as til_dot_md__orchestrator__msg__pb2


class MDDeploymentCommunicatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/til.MDDeploymentCommunicator/Create',
                request_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/til.MDDeploymentCommunicator/Update',
                request_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/til.MDDeploymentCommunicator/Delete',
                request_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
                )
        self.Cleanup = channel.unary_unary(
                '/til.MDDeploymentCommunicator/Cleanup',
                request_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
                )
        self.CheckHealth = channel.unary_unary(
                '/til.MDDeploymentCommunicator/CheckHealth',
                request_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
                )


class MDDeploymentCommunicatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cleanup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckHealth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MDDeploymentCommunicatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.SerializeToString,
            ),
            'Cleanup': grpc.unary_unary_rpc_method_handler(
                    servicer.Cleanup,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.SerializeToString,
            ),
            'CheckHealth': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckHealth,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'til.MDDeploymentCommunicator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MDDeploymentCommunicator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.MDDeploymentCommunicator/Create',
            til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.MDDeploymentCommunicator/Update',
            til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.MDDeploymentCommunicator/Delete',
            til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cleanup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.MDDeploymentCommunicator/Cleanup',
            til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckHealth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.MDDeploymentCommunicator/CheckHealth',
            til_dot_md__orchestrator__msg__pb2.MDDeploymentRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.MDDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TopologyUpdateCommunicatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateHealthStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/UpdateHealthStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetHealthStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetHealthStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.UpdateNode = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/UpdateNode',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetNodes = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetNodes',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetEdgeNodes = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetEdgeNodes',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetDatacenterNodes = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetDatacenterNodes',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetEndpointNodes = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetEndpointNodes',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetAllDeviceNodes = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetAllDeviceNodes',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetDeviceNode = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetDeviceNode',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.SetDeviceNodeStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/SetDeviceNodeStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetDeviceNodeStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetDeviceNodeStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetDeviceNodeDeploymentStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetDeviceNodeDeploymentStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.SetDeviceNodeDeploymentStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/SetDeviceNodeDeploymentStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.SetDeviceNodeMDDeploymentStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/SetDeviceNodeMDDeploymentStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )
        self.GetDeviceNodeMDDeploymentStatus = channel.unary_unary(
                '/til.TopologyUpdateCommunicator/GetDeviceNodeMDDeploymentStatus',
                request_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
                response_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
                )


class TopologyUpdateCommunicatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateHealthStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHealthStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEdgeNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatacenterNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEndpointNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllDeviceNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceNodeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceNodeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceNodeDeploymentStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceNodeDeploymentStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceNodeMDDeploymentStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceNodeMDDeploymentStatus(self, request, context):
        """rpc ChangeEdgeConnectionState (TopologyUpdateRequest) returns (TopologyUpdateResponse);
        rpc AddLAGConfiguration (TopologyUpdateRequest) returns (TopologyUpdateResponse);
        rpc ChangeLAGMemberState (TopologyUpdateRequest) returns (TopologyUpdateResponse);
        remove lag configuration
        NextHop Map
        ipv4 host entries
        arp table host entries
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopologyUpdateCommunicatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateHealthStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHealthStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetHealthStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealthStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'UpdateNode': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNode,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodes,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetEdgeNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEdgeNodes,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetDatacenterNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatacenterNodes,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetEndpointNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEndpointNodes,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetAllDeviceNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllDeviceNodes,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetDeviceNode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceNode,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'SetDeviceNodeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceNodeStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetDeviceNodeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceNodeStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetDeviceNodeDeploymentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceNodeDeploymentStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'SetDeviceNodeDeploymentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceNodeDeploymentStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'SetDeviceNodeMDDeploymentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceNodeMDDeploymentStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
            'GetDeviceNodeMDDeploymentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceNodeMDDeploymentStatus,
                    request_deserializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.FromString,
                    response_serializer=til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'til.TopologyUpdateCommunicator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TopologyUpdateCommunicator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateHealthStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/UpdateHealthStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHealthStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetHealthStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/UpdateNode',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetNodes',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEdgeNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetEdgeNodes',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatacenterNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetDatacenterNodes',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEndpointNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetEndpointNodes',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllDeviceNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetAllDeviceNodes',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetDeviceNode',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceNodeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/SetDeviceNodeStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceNodeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetDeviceNodeStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceNodeDeploymentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetDeviceNodeDeploymentStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceNodeDeploymentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/SetDeviceNodeDeploymentStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceNodeMDDeploymentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/SetDeviceNodeMDDeploymentStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceNodeMDDeploymentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/til.TopologyUpdateCommunicator/GetDeviceNodeMDDeploymentStatus',
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateRequest.SerializeToString,
            til_dot_md__orchestrator__msg__pb2.TopologyUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
