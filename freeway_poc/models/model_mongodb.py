"""
   Models to be used for mongodb database integration
   Initializes db if not created and outlines functions supported for accessing database records in the model
"""
from pymongo import MongoClient
import time
import os
from bson.json_util import loads, dumps
import json
import datetime

MONGO_HOST = os.getenv('MONGO_IP')
MONGO_DB = "Freeway"
connection = MongoClient(MONGO_HOST, 27017)
db = connection[MONGO_DB]


class model():
    def __init__(self):
        """
          connect to database, if database and/or table doesn't doesn't exist create it
        """
        pass

    def count_low_high_speeds(self, low, high):
        """
        Returns number of loop_data entries less than the low speed
        and number of loop_data entries greater than the high speed

        :param low: int
        :param high: int
        :return: dictionary
        """
        connection = MongoClient(MONGO_HOST, 27017)
        db = connection[MONGO_DB]
        loop_data = db['loop_data']

        results = loop_data.find({'speed': { '$gte': int(high), '$lte': int(low) } }).count()

        return results

    def volume_by_station(self, station_name, year, day, month):
        """
        Returns total volume of cars that pass through station on particular day
        :param station_name: string
        :param year: int
        :param day: int
        :param month: int
        :return: int
        """
        connection = MongoClient(MONGO_HOST, 27017)
        db = connection[MONGO_DB]
        stationParams = {'station_name': station_name}

        if (len(str(year)) != 4 or len(str(day)) != 2 or len(str(month)) != 2):
            raise Exception("Year, month, or day not in correct format.")

        year = int(year)
        month = int(month)
        day = int(day)
        startOfDay = datetime.datetime(year, month, day)
        endOfDay = datetime.datetime(year, month, day, 11, 59, 59)

        stations = db['stations']
        loop_data = db['loop_data']
        volume = 0

        station = json.loads(dumps(
            stations.find({'locationtext': stationParams['station_name']}, 
                projection={'_id':1, 'locationtext':1, 'milepost':1})))
        stationID = station[0]['_id']

        newStationData = loop_data.aggregate([
            {
                '$match':
                {
                    'stationid': stationID, 
                    'starttime':
                    {
                        '$gte': startOfDay,
                        '$lte': endOfDay
                    }
                }
            },
            {
                '$group': { '_id': '$stationid', 'totalAmount': {'$sum': '$volume'}}
            }
        ])

        for item in newStationData:
            if (item['_id'] == stationID):
                return item['totalAmount']
            else:
                return -1

    def find_route(self, direction, station_start, station_end):
        """
        Returns list of all stations, and their mileposts from start to end
        :param start_station: string
        :param end_station: string
        :return: list of dictionaries each entry is locationtext: milepost
        """
        stations = self.get_stations()
        params = {'station_start': station_start, 'station_end': station_end}
        starting_list = list(filter(lambda station: station['locationtext'] == params['station_start'], stations))
        ending_list = list(filter(lambda station: station['locationtext'] == params['station_end'], stations))
        starting = starting_list[0]
        ending = ending_list[0]
        i = 0
        path = []

        stream_dir = 0

        if(direction == 'south'):
            stream_dir = float(ending['milepost']) - float(starting['milepost'])

        else:
            stream_dir = float(starting['milepost']) - float(ending['milepost'])

        #set starting point as first point on path
        path.append(starting)

        if(starting['milepost'] == ending['milepost']):
            return path
        elif (stream_dir > 0.0):
            while((path[i]['_id'] != ending['_id']) and path[i]['upstream'] != 0):
                next_stop = list(filter(lambda station: station['_id'] == path[i]['upstream'], stations))
                path.append(next_stop[0])
                i += 1
        else:
            while((path[i]['_id'] != ending['_id']) and path[i]['downstream'] != 0):
                next_stop = list(filter(lambda station: station['_id'] == path[i]['downstream'], stations))
                path.append(next_stop[0])
                i += 1

        return path

    def update_station(self, station_name, milemarker):
        """
        Returns previous milepost and updated milepost
        :param start_station: string
        :param end_station: string
        :return: dictionary with each milepost as a list, before then after
        """
        connection = MongoClient(MONGO_HOST, 27017)
        db = connection[MONGO_DB]
        params = {'station_name': station_name, 'milemarker': milemarker}
        results = {}

        stations = db['stations']
        #get previous version
        results1 = json.loads(dumps(stations.find({'locationtext': params['station_name']}, projection={'_id':0, 'locationtext':1,'milepost':1})))
        station_before = results1[0]['milepost']
        #update station
        stations.update_one({'locationtext': params['station_name']},{'$set': {'milepost': params['milemarker']}})
        #get new version
        results2 = json.loads(dumps(stations.find({'locationtext': params['station_name']}, projection={'_id':0, 'locationtext':1,'milepost':1})))
        station_after = results2[0]['milepost']

        results[params['station_name']] = [station_before, station_after]

        return results

    def get_stations(self):
        """
        Returns a list of dictionaries, each entry is a station with id, locationtext, milepost, upstream, downstream
        """
        connection = MongoClient(MONGO_HOST, 27017)
        db = connection[MONGO_DB]
        path = []

        collection = db['stations']
        #get stations
        results = json.loads(dumps(collection.find({}, projection={'locationtext':1,'milepost':1, 'upstream':1, 'downstream':1})))

        return results
