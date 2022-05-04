#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
my_flights_info_list = data_manager.get_iata_codes()
flight_search = FlightSearch()
notification_manager = NotificationManager()
for desired_flight in my_flights_info_list:
    cheapest_flight_info, is_direct = flight_search.get_flight(desired_flight)
    notification_manager.notify_this_fight(cheapest_flight_info,is_direct)