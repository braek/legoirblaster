class LegoTrainControllerException(Exception):
    """
    The common exception for this package
    """
    pass


class InvalidLircError(LegoTrainControllerException):
    message = 'There is something wrong with your LIRC installation.'


class InvalidCommandError(LegoTrainControllerException):
    message = 'You are trying to execute an invalid Lego command.'


class InvalidInputError(LegoTrainControllerException):
    message = 'Invalid or incomplete input provided.'
