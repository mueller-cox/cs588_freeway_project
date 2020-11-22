"""
   Models to be used for mongodb database integration
   Initializes db if not created and outlines functions supported for accessing database records in the model
"""
from .Model import Model
from pymongo import MongoClient
import time
import os
from bson.json_util import loads, dumps
import json

MONGO_HOST = os.getenv('MONGO_IP')
MONGO_DB = "freeway"
connection = MongoClient(MONGO_HOST, 27017)
db = connection[MONGO_DB]


class model(Model):
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
        pass

    def volume_by_station(self, station_name, year, day, month):
        """
        Returns total volume of cars that pass through station on particular day
        :param station_name: string
        :param year: int
        :param day: int
        :param month: int
        :return: int
        """
        pass

    def find_route(self, station_start, station_end):
        """
        Returns list of all stations, and their mileposts from start to end
        :param start_station: string
        :param end_station: string
        :return: list of dictionaries each entry is locationtext: milepost
        """
        stations = self.get_stations()

        starting = dict(filter(lambda station: station['locationtext'] == params['station_start'], stations))
        ending = dict(filter(lambda station: station['locationtext'] == params['station_end'], stations))
        i = 0
        path = []

        if(starting['milepost'] == ending['milepost']):
            path.append(starting)
        else if (starting['milepost'] > ending['milepost']):
            path.append(starting)
            while(path[i]['_id'] != ending['_id'] && path[i]['downstream'] != 0):
                path[i+1] = dict(filter(lambda station: station['_id'] == path[i]['downstream'])
                i += 1
        else:
            while(path[i]['_id'] != ending['_id'] && path[i]['upstream'] != 0):
                path[i+1] = dict(filter(lambda station: station['_id'] == path[i]['upstream'])
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
        params = {'station_start': station_start, 'station_end': station_end}
        path = []

        collection = db['stations']
        #get stations
        stations = json.loads(dumps(stations.find({}, projection={'locationtext':1,'milepost':1, 'upstream':1, 'downstream':1})))

        return stations
