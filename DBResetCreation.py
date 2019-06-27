import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://catarng:yoro@yoro-5bxmt.mongodb.net/yoro?retryWrites=true&w=majority")
print('Dropping Database')
client.drop_database('yoro')
db = client.yoro

query = {
  '_id': '5d1387b338fd21e',
  'event_name': 'Data Symposium 2019',
  'total_registered': '2560',
  'in': '120'
}

db.event.insert_one(query)
event = db.event.find_one({'event_name': 'Data Symposium 2019'})

ids = str(event['_id'])

print('1 Event has been created with _id: ', ids)

query = {
  '_id': ids + '#catarng',
  'first_name': 'Cassidy',
  'last_name': 'Tarng',
  'cec_id': 'catarng',
  'registered': 'true',
  'checked_in': 'false'
}
db.user.insert_one(query)
print('1 User has been created')

