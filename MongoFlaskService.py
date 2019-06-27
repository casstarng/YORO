from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb+srv://catarng:yoro@yoro-5bxmt.mongodb.net/yoro?retryWrites=true&w=majority")
db = client.yoro

@app.route('/yoro/checkInUser', methods=['POST'])
def checkInuser():
    # Check if ticket_id is present in request
    if not request.json or not 'id' in request.json:
        return jsonify({'code': 'F1',
                        'response': 'Fail',
                        'message': 'id is not present in request'}), 201

    query = {
        '_id': request.json['id']
    }

    # Query
    user = db.user.find_one(query)

    # Check if user exists
    if user is None:
        return jsonify({'code': 'F2',
                        'response': 'Fail',
                        'message': 'There is no user with that ID'}), 201

    # Check if user is already checked in
    if user['checked_in'] == 'true':
        return jsonify({'code': 'S1',
                        'response': 'Success',
                        'message': 'User has already been checked in'}), 201

    # Update user info
    db.user.update({'_id': request.json['id']}, {'$set': {'checked_in': 'true'}})

    # Return success response
    return jsonify({'code': 'S0',
                    'response': 'Success',
                    'message': 'User has now been checked in',
                    'user_info': user}), 201

if __name__ == '__main__':
    app.run(debug=True)