


import logging

from .logger.logger import init_logger
from .validator import Validator


class OrchestratorUtils(object):
    """
    Some general util collections to simplify OMuProCU's code.
    """

    def __init__(self) -> None:
        self.validator = Validator()
        self.logger = init_logger(self.__class__.__name__)

    @staticmethod
    def _build_tenant_cnf_id(tenantId, tenantFuncName):
        return "t" + str(tenantId) + "-" + tenantFuncName
