from twilio.rest import Client


def sendsms():
    account_sid = 'AC3d7f9883779af7b5ac9e95e43e7f4fa9'
    auth_token = 'cda6742b43556a4f6a173c5cf77bc9b2'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello, this is a reminder of your medical appointment at Kapsiya Dispensary on this day",
        from_='+18177569565',
        to='+254717170902',
    )
    print('message sent successfully')

