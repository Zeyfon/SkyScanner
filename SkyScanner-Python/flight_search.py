from flight_data import FlightData
import requests

class FlightSearch():
    def __init__(self):
        self.flight_search_endpoing = "https://tequila-api.kiwi.com/v2/search"

        self.header = {
            "apikey": "_mj-uNIvS2uFQqJ0v0NexbEP0DE_5E5o"
        }
    #This class is responsible for talking to the Flight Search API.
    def get_flight(self,flight):
        flight_data = FlightData()
        try:
            flight_info= flight_data.get_info_data(destination_code=flight['iataCode'])
            response = requests.get(url=self.flight_search_endpoing, headers=self.header, params=flight_info)
            response.raise_for_status()
            cheapest_flight = response.json()['data'][0]
            is_direct = True
        except IndexError:
            flight_info= flight_data.get_info_data(destination_code=flight['iataCode'],stop_overs=1)
            response = requests.get(url=self.flight_search_endpoing, headers=self.header, params=flight_info)
            response.raise_for_status()
            cheapest_flight = response.json()['data'][0]
            is_direct=False
        if int(cheapest_flight['price']) < int(flight['lowestPrice']):
            return cheapest_flight,is_direct


