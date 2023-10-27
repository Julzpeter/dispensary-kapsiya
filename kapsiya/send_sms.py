from twilio.rest import Client


def sendsms():
    account_sid = 'AC3d7f9883779af7b5ac9e95e43e7f4fa9'
    auth_token = '91e80e8e3474e0b02440dc4d9ee84129'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello, this is a reminder of your medical appointment at Kapsiya Dispensary on this day",
        from_='+18177569565',
        to='+254717170902',
    )
    print('message sent successfully')

