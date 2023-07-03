from twilio.rest import Client

def sendmsg():
    account_sid = 'YOUR ACCOUNT SID'
    auth_token = 'YOUR AUTH TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_ = 'SENDING/YOUR BOUGHT NUMBER',
        body = 'Unauthorized access in system',
        to = 'RECEIVING MOBILE NUMBER'
    )

    print(message.sid)
