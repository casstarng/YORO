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
  'checked_in': 'false',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#jonathat',
  'first_name': 'Jonathan',
  'last_name': 'Tan',
  'cec_id': 'jonathat',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#jimpan',
  'first_name': 'Jimmy',
  'last_name': 'Pan',
  'cec_id': 'jimpan',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#algarbar',
  'first_name': 'Alex',
  'last_name': 'Garbarini',
  'cec_id': 'algarbar',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#zitun',
  'first_name': 'Zin',
  'last_name': 'Tun',
  'cec_id': 'zitun',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#amandela',
  'first_name': 'Aruna',
  'last_name': 'Mandela',
  'cec_id': 'amandela',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#harkgrew',
  'first_name': 'Harkamal',
  'last_name': 'Grewal',
  'cec_id': 'harkgrew',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')

query = {
  '_id': ids + '#vagaur',
  'first_name': 'Vasu',
  'last_name': 'Gaur',
  'cec_id': 'vagaur',
  'registered': 'true',
  'checked_in': 'true',
  'event_id': ids
}
db.user.insert_one(query)
print('1 User has been created')