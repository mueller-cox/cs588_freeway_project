from pymongo import MongoClient
import pprint
import os

MONGO_HOST = os.getenv('MONGO_IP')
MONGO_DB = "freeway"

connection = MongoClient(MONGO_HOST, 27017)
db = connection[MONGO_DB]

#return all stations
stations = db['stations']
all_stations = stations.find()

for station in all_stations:
    #find all detectors for the station
    collect_detectors = db['detectors']
    s_id = station['_id']
    detectors = list(collect_detectors.find({'stationid': s_id},projection={'lanenumber': 1, 'detectorclass': 1}))
    #add the detectors to a detectors field for the station
    stations.update_one({'_id':station['_id']},{'$set': {'detectors': detectors}})
