from pymongo import MongoClient
import time
import os

MONGO_HOST = os.getenv('MONGO_IP')
MONGO_DB = "freeway"

connection = MongoClient(MONGO_HOST, 27017)
db = connection[MONGO_DB]

#return all detectors
detectors = db['detectors']
all_detectors = detectors.find({},projection={'stationid': 1})

start_time = time.time()

for detector in all_detectors:
    d_id = detector['_id']
    s_id = detector['stationid']
    #update all loop_data documents that have the detectorid assigned
    db['loop_data'].update_many({'detectorid': d_id}, {'$set': {'stationid': s_id}})

end_time = time.time()
time_diff = end_time - start_time

print(f"Time to run query: {time_diff}")
