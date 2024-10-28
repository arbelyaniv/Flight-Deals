from data_manager import DataManager
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager


# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# ==================== Search for Flights and making message ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flight("NYC",
                                         destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_month_from_today)

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        message_body = f"Low price alert! Only £{cheapest_flight.price} to fly "
        message_body += f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        message_body += f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."

# ==================== sending message ====================

        # SMS
        notification_manager.send_sms(message_body)
        # Whatsapp
        notification_manager.send_whatsapp(message_body)




