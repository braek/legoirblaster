class LegoTrainException(Exception):
    pass


class LegoTrainControllerException(Exception):
    """
    The common exception for this package
    """
    pass


class LircNotInstalledError(LegoTrainControllerException):
    pass


class UnknownCommandError(LegoTrainControllerException):
    pass
