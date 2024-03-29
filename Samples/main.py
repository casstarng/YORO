from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route('/test', methods=['POST'])
def test():
    print('test request sent')
    socketio.emit('my response', {'user_name': 't', 'message': 't'}, namespace='/myevent')
    return 'hi'

@socketio.on('my event', namespace='/myevent')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    print(messageReceived)
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
