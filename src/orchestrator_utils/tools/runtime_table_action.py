

from enum import Enum


class RuntimeTableAction(Enum):
    ADD = "table_add"
    UPDATE = "table_update"
    REMOVE = "table_remove"