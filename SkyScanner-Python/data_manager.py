# This class is responsible for talking to the Google Sheet.
import requests

class DataManager:
    def __init__(self):
        #Check if the iataCode is missing
        #In case is missing it will find it
        self.verify_and_create_iata_codes()

    def get_iata_codes(self):
        try:
            sheety_endpoint = "https://api.sheety.co/523ab65e2f6a0c1fad7bd965ed7d0947/flightDeals/prices"
            response2 = requests.get(url=sheety_endpoint)
            prices = response2.json()['prices']
        except:
            prices = [{"city":"Paris","iataCode":"PAR","lowestPrice":"54"},
                      {"city":"Bali","iataCode":"DPS","lowestPrice":"501"},
                      {"city":"Berlin","iataCode":"BER","lowestPrice":"42"}]
        return prices

    def verify_and_create_iata_codes(self):
            prices = self.get_iata_codes()

            if len(prices[0]['iataCode'])==0:

                sheety_update_endpoint = "https://api.sheety.co/523ab65e2f6a0c1fad7bd965ed7d0947/flightDeals/prices"
                for row in range(2,len(prices)+2):
                    city_name = prices[row-2]['city']
                    body = {
                        "price": {
                            "city": city_name,
                            "iataCode": create_iata_code(city_name),
                            "lowestPrice": f"{prices[row-2]['lowestPrice']}"
                        }
                    }

                    response3 = requests.put(url=f"{sheety_update_endpoint}/{row}", json=body)
                    response3.raise_for_status()

def create_iata_code(city_name:str):
        location_search_header = {
            "apikey": "_mj-uNIvS2uFQqJ0v0NexbEP0DE_5E5o"
        }
        flight_search_endpoing = "https://tequila-api.kiwi.com/locations/query"

        location_data = {
            "term": city_name
        }

        response = requests.get(url=flight_search_endpoing, headers=location_search_header, params=location_data)
        response.raise_for_status()
        iata_code = response.json()['locations'][0]['code']
        return iata_code

