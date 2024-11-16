from enum import Enum, auto


class DeciderType(Enum):
    """ enum to connect which decider will be used. """
    CLI = auto()
    QUEUE = auto()
    # TODO -> TEST should only be called from within a test -> can I enforce this somehow?
    TEST = auto()
