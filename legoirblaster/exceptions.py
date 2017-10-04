class LegoIRBlasterException(Exception):
    """
    The common exception for this package
    """
    pass


class LircError(LegoIRBlasterException):
    """
    This error is raised when there is something wrong with the LIRC installation
    """
    def __init__(self):
        LegoIRBlasterException.__init__(self, 'LIRC is not installed or FUBAR')


class CommandError(LegoIRBlasterException):
    """
    This error is raised when you try to execute a command that is not known by LEGO® Power Functions
    """
    def __init__(self):
        LegoIRBlasterException.__init__(self, 'LEGO® Power Functions does not compute')
