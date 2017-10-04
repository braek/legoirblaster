class LegoIRBlasterException(Exception):
    """
    The common exception for this package
    """
    pass


class InvalidLircError(LegoIRBlasterException):
    message = 'There is something wrong with your LIRC installation.'


class InvalidCommandError(LegoIRBlasterException):
    message = 'You are trying to execute an invalid Lego command.'


class InvalidInputError(LegoIRBlasterException):
    message = 'Invalid or incomplete input provided.'
