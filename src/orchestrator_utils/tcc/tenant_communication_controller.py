

from concurrent import futures
from multiprocessing import Process

import grpc

from orchestrator_utils.til import til_msg_pb2
from orchestrator_utils.logger.logger import init_logger

from ..til import til_msg_pb2_grpc


class TenantCommunicationController(Process, til_msg_pb2_grpc.TCCommunicatorServicer):
    """
    Reference Implementation for a Tenant Communication Controller. This allows to follow the deployment pipeline presented in the paper.
    """

    def __init__(self, group = None, target = None, name = None, args = (), kwargs ={}, daemon = None, address="localhost:49050") -> None:
        Process.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self.logger = init_logger(self.__class__.__name__)
        try:
            self.grpc_server = grpc.server(futures.ThreadPoolExecutor(10))
            til_msg_pb2_grpc.add_TCCommunicatorServicer_to_server(self, self.grpc_server)
            self.grpc_server.add_insecure_port(address)
        except Exception as ex:
            self.logger.exception(ex, exc_info=True)

    def run(self) -> None:
        super().run()
        self.running = True
        self.grpc_server.start()
        self.logger.info("TCC started")

    def terminate(self) -> None:
        self.running = False
        self.logger.info("Got Terminate. Stopping GRPC server.")
        self.grpc_server.stop(10)
        self.logger.info("TCC stopped.")

        
    def CreateTenantConfig(self, request, context):
        return til_msg_pb2.TenantConfigResponse(
            status=200,
            message = "dummy response"
        )
    
    def DeleteTenantConfig(self, request, context):
        return til_msg_pb2.TenantConfigResponse(
            status=200,
            message = "dummy response"
        )
    
    def UpdateTenantConfig(self, request, context):
        return til_msg_pb2.TenantConfigResponse(
            status=200,
            message = "dummy response"
        )
