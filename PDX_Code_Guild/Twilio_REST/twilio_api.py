from api_credentials import FROM_NUM, TO_NUM, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client


class Message:

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def __init__(self, text):
        self.text = text
        self.from_num = FROM_NUM

    def check(self, to_num):
        if len(to_num) != 12 or not to_num.startswith('+'):
            raise ValueError("Phone number must start with a '+' and be a total of 12 characters long.")
        else:
            return to_num
    def send(self, to_num):
        '''Sends a message to a given number via Twilio API'''


        # call = client.api.account.calls\
        #       .create(to=TO_NUM,  # Any phone number
        #               from_=FROM_NUM, # Must be a valid Twilio number
        #               url="https://drive.google.com/open?id=0BxwVfppX-_KLdG11MHl6Q0Y1STg")
        valid_number = self.check(to_num)

        Message.client.messages.create(to=valid_number, from_=self.from_num,
                                   body=self.text)

if __name__ == '__main__':
    new_message = Message("Here's a message from my command line app!")
    new_message.send(TO_NUM)