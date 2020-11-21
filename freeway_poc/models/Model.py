"""
    Model.py includes the calls for each query we need to be able to execute
"""


class Model:
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

    def find_route(self, start_station, end_station):
        """
        Returns list of all stations, and their mileposts from start to end
        :param start_station: string
        :param end_station: string
        :return: list of dictionaries
        """
        pass

    def update_station(self, station_name, milemarker):
        """
        Returns previous milepost and updated milepost
        :param start_station: string
        :param end_station: string
        :return: list of dictionaries
        """
        pass

    def get_station_names(self):
        """
        Returns a list of dictionaries, NB and SB with sation names for each
        """

        pass
        
