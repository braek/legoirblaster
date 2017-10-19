from flask import Flask, render_template, Response, request
from flask import jsonify
from . import core, constants
from . import exceptions
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    channels = list(range(1, constants.CHANNELS + 1))
    devices = list(range(1, constants.CHANNELS * len(constants.OUTPUTS) + 1))
    return Response(
        render_template('index.html', channels=channels, outputs=constants.OUTPUTS, devices=devices),
        content_type=constants.HTML_CONTENT_TYPE
    )


@app.route('/cmd', methods=['POST'])
def cmd():
    try:
        # Parse input
        channel = int(request.form.get('channel', 0))
        output = request.form.get('output', 'R').upper()
        speed = int(request.form.get('speed', -8))
        brake = bool(int(request.form.get('brake', 0)))

        # Create command
        cmd = core.create_command(channel, output, speed, brake)

        # Execute command
        core.send_command(cmd)

        # Success response
        data = {
            'cmd': cmd
        }
        status_code = 200
    except ValueError as e:
        data = {
            'error': str(e)
        }
        status_code = 400
    except exceptions.CommandError as e:
        data = {
            'error': str(e)
        }
        status_code = 405
    except exceptions.LircError as e:
        data = {
            'error': str(e)
        }
        status_code = 500

    # Create HTTP response
    response = jsonify(data)
    response.status_code = status_code
    return response
