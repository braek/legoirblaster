from flask import Flask, render_template, Response, request
from flask import jsonify
from . import core, constants
from .exceptions import LegoIRBlasterException
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
    channel = request.form.get('channel')
    output = request.form.get('output')
    speed = request.form.get('speed')
    brake = request.form.get('brake')
    try:
        cmd = core.create_command(channel, output, speed, brake)
        core.send_command(cmd)
        data = {
            'cmd': cmd
        }
        status_code = 200
    except LegoIRBlasterException as e:
        data = {
            'error': str(e)
        }
        status_code = 400

    # Create HTTP response
    response = jsonify(data)
    response.status_code = status_code
    return response
