import subprocess
from . import config
from . import exceptions


def send_lego_train_command(cmd):
    try:
        subprocess.call(['irsend', 'SEND_ONCE', config.MODE, cmd])
    except FileNotFoundError:
        # raise exceptions.InvalidLircError()
        pass
    except Exception as e:
        raise exceptions.LegoTrainControllerException(str(e))


def get_lego_train_command(channel, output, speed, brake):
    try:
        channel = int(channel)
        output = str(output)
        speed = int(speed)
        brake = int(brake)
    except (TypeError, ValueError):
        raise exceptions.InvalidInputError()
    if channel in range(1, config.CHANNELS + 1) and output in config.OUTPUTS:
        if brake:
            cmd = 'BRAKE'
        elif speed in range(0, 8):
            cmd = '{}'.format(speed)
        elif speed in range(-7, 0):
            cmd = 'M{}'.format(abs(speed))
        if cmd:
            return '{}{}_{}'.format(channel, output, cmd)
        raise exceptions.InvalidCommandError()
