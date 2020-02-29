from enum import IntEnum


class OpenList(IntEnum):
    F_N = 0
    NODE = 1

    # Source: https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
    def __str__(self):
        return '%s' % self.value


class MovesList(IntEnum):
    F_N = 0
    G_N = 1
    H_N = 2
    POSITION = 3
    PARENT_NODE = 4

    # Source: https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
    def __str__(self):
        return '%s' % self.value


class VisitedNode(IntEnum):
    NODE = 0
    NODE_INFO = 1
    SOLVED = 2

    # Source: https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
    def __str__(self):
        return '%s' % self.value


class OutputValues(IntEnum):
    F_N = 0
    G_N = 1
    H_N = 2

    # Source: https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
    def __str__(self):
        return '%s' % self.value


