

from enum import Enum


class DeploymentStatus(Enum):
    """
    Pipeline Status
    """
    UNSPECIFIED = 0
    VALIDATING = 1
    SCHEDULING = 2
    SCHEDULED = 3
    UPDATING = 4
    NOS_UPDATED = 5
    IN_UPDATED = 6
    RUNNING = 7
    DELETED = 8
    REQUEST_DELETE = 9
    FAILED = 10