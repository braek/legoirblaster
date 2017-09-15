import subprocess
from . import config
from .exceptions import LegoTrainException


def send_lego_train_command(cmd):
    try:
        subprocess.call(['irsend', 'SEND_ONCE', config.MODE, cmd])
    except FileNotFoundError:
        # raise LegoTrainException("irsend is not installed!")
        pass
    except Exception as e:
        raise LegoTrainException(str(e))


def get_lego_train_command(channel, output, speed, brake):
    channel = int(channel)
    output = str(output)
    speed = int(speed)
    brake = int(brake)
    if channel in range(1, config.CHANNELS + 1) and output in config.OUTPUTS:
        if brake:
            cmd = 'BRAKE'
        elif speed in range(0, 8):
            cmd = '{}'.format(speed)
        elif speed in range(-7, 0):
            cmd = 'M{}'.format(abs(speed))
        if cmd:
            return '{}{}_{}'.format(channel, output, cmd)
        raise LegoTrainException('This command is invalid!')
