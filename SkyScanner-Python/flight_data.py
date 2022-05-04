# This class is responsible for structuring the flight data.
import datetime

class FlightData:
    def __init__(self):
        self.tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_from_tomorrow = (datetime.date.today() + datetime.timedelta(days=6 * 30 + 1)).strftime("%d/%m/%Y")

    def get_info_data(self,destination_code, stop_overs=0):
        flight_search_data = {
            "fly_from": "LON",
            "fly_to": destination_code,
            "date_from": self.tomorrow,
            "date_to": self.six_months_from_tomorrow,
            "flight_type":"oneway",
            "curr":"GBP",
            "max_stopovers":stop_overs,
        }
        return flight_search_data
