import subprocess
from . import constants
from . import exceptions


def send_command(command):
    """
    Function to send the IR command through LIRC. Make sure that LIRC is properly configured or this could raise
    exceptions.

    :param command: string representing the raw IR command to send
    :return: nothing, but sends and IR command through LIRC
    """
    try:
        subprocess.call(['irsend', 'SEND_ONCE', constants.RC_MODE, command])
    except FileNotFoundError:
        raise exceptions.LircError


def create_command(channel=1, output='R', speed=0, brake=False):
    """
    This function generates an IR command based upon user input.
    When no IR command can be generated based upon the user input, an exception is raised.

    :param channel: integer representing the channel to control (1 to 4)
    :param output: string representing the output to control (R or B)
    :param speed: integer representing speed and direction (-7 up to 7)
    :param brake: boolean indicating that the brake was hit
    :return: string representing the raw IR command
    """
    if channel in range(1, constants.CHANNELS + 1) and output in constants.OUTPUTS:
        command = None
        if brake:
            command = 'BRAKE'
        elif speed in range(0, constants.MAX_SPEED + 1):
            command = '{}'.format(speed)
        elif speed in range(-constants.MAX_SPEED, 0):
            command = 'M{}'.format(abs(speed))
        if command:
            return '{}{}_{}'.format(channel, output, command)
    raise exceptions.CommandError
