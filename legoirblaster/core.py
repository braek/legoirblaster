import subprocess
from . import constants
from . import exceptions


def send_command(cmd):
    """
    Function to send the IR command through LIRC. Make sure that LIRC is properly configured or this could raise
    exceptions.

    :param cmd: string representing the raw IR command to send
    :return: nothing, but sends and IR command through LIRC
    """
    try:
        subprocess.call(['irsend', 'SEND_ONCE', constants.RC_MODE, cmd])
    except FileNotFoundError:
        raise exceptions.LircError


def create_command(channel, output, speed, brake):
    """
    This function generates an IR command based upon user input.
    When no IR command can be generated based upon the user input, an exception is raised.

    :param channel: integer representing the channel to control (1 to 4)
    :param output: string representing the output to control (R or B)
    :param speed: integer representing speed and direction (-7 up to 7)
    :param brake: boolean indicating that the brake was hit
    :return: string representing the raw IR command
    """
    print('brake={}'.format(brake))
    if channel in range(1, constants.CHANNELS + 1) and output in constants.OUTPUTS:
        if brake:
            cmd = 'BRAKE'
        elif speed in range(0, constants.MAX_SPEED + 1):
            cmd = '{}'.format(speed)
        elif speed in range(-constants.MAX_SPEED, 0):
            cmd = 'M{}'.format(abs(speed))
        if cmd:
            return '{}{}_{}'.format(channel, output, cmd)
    raise exceptions.CommandError
