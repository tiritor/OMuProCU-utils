

from enum import Enum


class CountermeasureAction(Enum):

    ACCEPT = "accept"
    DROP = "drop"
    SOFT = "soft"
    HARD = "hard"