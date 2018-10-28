# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from flask import Flask, render_template, request

# Your Account Sid and Auth Token from twilio.com/console
account_sid = '{replace with your account sid}'
auth_token = '{replace with your auth token}'
client = Client(account_sid, auth_token)

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

# myapp will get the user phone number and then create an outbound message from twilio to user
@app.route('/submit')
def submit():
    phone_number = request.values.get('phoneNumber')
    print ("Phone %s" % phone_number)
    phone_number = '+%s' % phone_number
    print("Phone %s" % phone_number)
    message = client.messages.create(
        from_='{replace with your twilio number}',
        body='Test submit',
        to= phone_number
    )
    print(message.sid)
    return render_template('success.html')

# User sends a message to twilio number. 
# Twilio will trigger myapp to response the message below back to user.
@app.route('/smsmycountry')
def smsmycountry():
    from_country = request.values.get('FromCountry', None)
    response = MessagingResponse()
    response.message('Hi! It looks like your phone was located in %s' % from_country)
    print (str(response))
    return str(response)
