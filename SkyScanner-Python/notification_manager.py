# This class is responsible for sending notifications with the deal flight details.
import smtplib
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.account_sid = "AC93e19b78d5dd89a630369bacf1756743"
        self.auth_token = "18c3073a9cb98df5db0444cffdfa9adf"
        self.my_email = "cesar.canto.0709@gmail.com"
        self.password = "Jap2022#C"

    def notify_this_fight(self,flight,is_direct):
        # send_sms(flight,is_direct)
        self.send_emails(flight,is_direct)

    def send_emails(self,flight,is_direct):
        users=[{"firstName":"Cesar","lastName":"Canto","email":"ing.cesar.canto@gmail.com"}]
        subject = f"Cheap Flight from {flight['cityFrom']} to {flight['cityTo']}"
        body1 = f"Low price alert! Only £{flight['price']} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} to " \
                f"{flight['cityTo']}-{flight['cityCodeTo']}, from {(flight['local_departure']).split('T')[0]} to "\
                f"{(flight['local_arrival']).split('T')[0]}\n"
        body2=""
        print(body1)
        if not is_direct:
            body2=f"Flight has 1 stop over, via {flight['route'][0]['cityTo']}\n\n"
            print(body2)
        departure_date=flight['local_departure'].split('T')[0]
        arrival_date=flight['local_arrival'].split('T')[0]
        body3= f"https://www.google.com/travel/flights?q=Flights%20to%20{flight['cityCodeTo']}%20from%20{flight['cityCodeFrom']}%20on%20{departure_date}%20through%20{arrival_date}"
        print(body3)
        body = body1+body2+body3
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs=users[0]['email'],
                                msg=f"Subject:{subject}\n\n{body}".encode('utf-8'))


    def send_sms(self,flight,is_direct):

        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert! Only {flight['price']} to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} to "
              f"{flight['cityTo']}-{flight['cityCodeTo']}, from {(flight['local_departure']).split('T')[0]} to "
              f"{(flight['local_arrival']).split('T')[0]}",
            from_='+19206670709',
            to='+522225726722'
        )
        print(message.status)