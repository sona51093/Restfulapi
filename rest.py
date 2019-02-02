from flask import Flask , request, jsonify
from flask_api import status

app = Flask(__name__)

time_message = {}
@app.route('/getmessage/<time>', methods=['GET'])
def getMessage(time):
    try:
       return jsonify(time_message[time])
    except:
        content = {'message not present': 'Message not present for the requested time'}
        return jsonify(content), status.HTTP_404_NOT_FOUND


@app.route('/setmessage/', methods=['POST'])
def setMessage():

    try:
        message = time_message[request.json['time']]
        content = {'already scedule': 'this time is already schedule for other message'}
        return jsonify(content), status.HTTP_400_BAD_REQUEST
    except:
        time_message[request.json['time']] = request.json['message']
        content = {status.HTTP_202_ACCEPTED: 'the requested message scedule for give time'}
        return jsonify(content), status.HTTP_202_ACCEPTED

if __name__ == '__main__':
    app.run(debug=True)