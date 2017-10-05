from flask import Flask, render_template, Response, request
from flask import jsonify
from . import core, constants
from . import exceptions
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    channels = list(range(1, constants.CHANNELS + 1))
    devices = list(range(1, constants.CHANNELS * len(constants.OUTPUTS) + 1))
    response = Response(render_template('index.html', channels=channels, outputs=constants.OUTPUTS, devices=devices))
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    return response


@app.route('/cmd', methods=['POST'])
def cmd():
    channel = int(request.form.get('channel', 0))
    output = request.form.get('output', 'R').upper()
    speed = int(request.form.get('speed', -8))
    brake = bool(int(request.form.get('brake', 0)))
    try:
        cmd = core.create_command(channel, output, speed, brake)
        core.send_command(cmd)
        data = {
            'cmd': cmd
        }
        status_code = 200
    except exceptions.LegoIRBlasterException as e:
        data = {
            'error': str(e)
        }
        if isinstance(e, exceptions.LircError):
            status_code = 500
        else:
            status_code = 400

    # Create HTTP response
    response = jsonify(data)
    response.status_code = status_code
    return response
