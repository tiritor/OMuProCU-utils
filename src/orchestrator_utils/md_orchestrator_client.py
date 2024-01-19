

import grpc

from .logger.logger import init_logger
from .til import md_orchestrator_msg_pb2_grpc
from .til.md_orchestrator_msg_pb2 import MDDeploymentRequest, MDDeploymentResponse


class MDOMuProCUClient(object):
    """
    docstring
    """
    
    def __init__(self, MDOMuProCUAddress : str) -> None:
        self.address = MDOMuProCUAddress
        self.channel = grpc.insecure_channel(MDOMuProCUAddress)
        self.md_orchestrator_stub = md_orchestrator_msg_pb2_grpc.MDDeploymentCommunicatorStub(self.channel)
        self.logger = init_logger(self.__class__.__name__)

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
    
    def check_health(self):
        """
        docstring
        """
        resp : MDDeploymentResponse = self.md_orchestrator_stub.CheckHealth(
            MDDeploymentRequest()
        )
        self.logger.debug(resp)

    def cleanup(self):
        """
        docstring
        """
        resp : MDDeploymentResponse = self.md_orchestrator_stub.Cleanup(
            MDDeploymentRequest(
            )
        )
        self.logger.debug(resp)