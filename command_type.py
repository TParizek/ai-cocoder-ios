from enum import Enum

class CommandType(Enum):
    DOCUMENT = "document"
    UNIT_TEST = "unit_test"
    REFACTORING = "refactoring"