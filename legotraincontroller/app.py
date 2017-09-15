from flask import Flask, render_template, Response, request
from flask import jsonify
from . import core, config
from .exceptions import LegoTrainException
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    channels = list(range(1, config.CHANNELS + 1))
    trains = list(range(1, config.CHANNELS * len(config.OUTPUTS) + 1))
    response = Response(render_template('index.html', channels=channels, outputs=config.OUTPUTS, trains=trains,
                                        title=config.TITLE))
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    return response


@app.route('/cmd', methods=['POST'])
def cmd():
    channel = request.form.get('channel')
    output = request.form.get('output')
    speed = request.form.get('speed')
    brake = request.form.get('brake')
    try:
        cmd = core.get_lego_train_command(channel, output, speed, brake)
        core.send_lego_train_command(cmd)
        data = {
            'cmd': cmd
        }
        status_code = 200
    except LegoTrainException as e:
        data = {
            'error': str(e)
        }
        status_code = 400

    # Create HTTP response
    response = jsonify(data)
    response.status_code = status_code
    return response
