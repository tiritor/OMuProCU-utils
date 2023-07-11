
import grpc
import yaml

from .til import til_msg_pb2_grpc, til_msg_pb2

class OrchestratorClient(object):
    """
    OMuProCU reference client

    This communicates and submit TDCs to the OMuProCU default port.
    """
    def __init__(self, orchestrator_address) -> None:
        self.channel = grpc.insecure_channel(orchestrator_address)
        self.orchestrator_stub = til_msg_pb2_grpc.DeploymentCommunicatorStub(self.channel)

    def restart_reconfig_scheduler_loop(self):
        """
        Restart OMuProCU's Reconfiguration Scheduler Loop
        """
        resp: til_msg_pb2.DeploymentResponse = self.orchestrator_stub.RestartSchedulerLoop(
            til_msg_pb2.DeploymentRequest(
                tenantMetadata = til_msg_pb2.TenantMetadata(),
            )
        )
        return resp.status, resp.message
    
    def create(self, tdc_path):
        """
        Submit a deployment to create a specified TDC. 

        Parameters
        -----------
        tdc_path : str
            Path to a TDC yaml file
        """
        tdc_content = ""
        with open(tdc_path, "r") as f:
            tdc_content = f.read()
            resp: til_msg_pb2.DeploymentResponse = self.orchestrator_stub.Create(
                til_msg_pb2.DeploymentRequest(
                    tenantMetadata = til_msg_pb2.TenantMetadata(),
                    deploymentMessage = til_msg_pb2.DeploymentMessage(
                        deploymentRaw = tdc_content 
                    )

                )
            )
        return resp.status, resp.message
        
    def update(self, tdc_path):
        """
        Submit a deployment to update a specified TDC. 

        Parameters
        -----------
        tdc_path : str
            Path to a TDC yaml file
        """
        tdc_content = ""
        with open(tdc_path, "r") as f:
            tdc_content = f.read()
            resp: til_msg_pb2.DeploymentResponse = self.orchestrator_stub.Update(
                til_msg_pb2.DeploymentRequest(
                    tenantMetadata = til_msg_pb2.TenantMetadata(),
                    deploymentMessage = til_msg_pb2.DeploymentMessage(
                        deploymentRaw = tdc_content 
                    )

                )
            )
        return resp.status, resp.message

    def delete(self, tdc_path=None):
        """
        Submit a deployment to delete a specified TDC. 

        Parameters
        -----------
        tdc_path : str
            Path to a TDC yaml file
        """
        tdc_content = ""
        if tdc_path is not None:
            with open(tdc_path, "r") as f:
                tdc = yaml.safe_load(f) 
                resp : til_msg_pb2.DeploymentResponse = self.orchestrator_stub.Delete(
                    til_msg_pb2.DeploymentRequest(
                        tenantMetadata = til_msg_pb2.TenantMetadata(tenantId=tdc["id"], tenantFuncName=tdc["name"]),

                    )
                )
        return resp.status, resp.message

    def cleanup(self):
        """
        Trigger OMuProCU to cleanup all TDCs and get the initial state.
        """
        resp: til_msg_pb2.DeploymentResponse = self.orchestrator_stub.Cleanup(
            til_msg_pb2.TenantMetadata()
        )
        return resp.status, resp.message

    def close(self):
        """
        Close the GRPC channel to OMuProCU.
        """
        self.channel.close()
    