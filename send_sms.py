from twilio.rest import Client

account_sid = "AC5d165adc4b836c2e80e46a6ba4547cac"
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

def message(content):
    sms = client.messages.create(
        to="your_phone_number", 
        from_="your_twilio_phone_number", 
        body=content)
    print(sms.sid)