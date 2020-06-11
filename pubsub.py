# this code will help to fetch new messages from pubsub and process it sequentially. #june-2020

import firebase_admin
from firebase_admin import firestore,storage
from firebase_admin import credentials
from google.cloud import pubsub

subscription_name = 'subscription_name'
project_id = 'project_id'

class PubsubMessageHandler():

    def PubsubCallback(self,message):
        print(message)
        msg_id =  message.message_id
        print(msg_id)
        sub_data = message.data.decode('utf-8') #decoding Pubsub message 
        data = json.loads(sub_data)
        print(data)
        
        #add  your code below
        
def main():
    
    # Below three lines would trigger the processing of the message from uploads subscription
    handler = PubsubMessageHandler()
    subscriber = pubsub.SubscriberClient()
    future = subscriber.subscribe(subscription_path,handler.PubsubCallback) # this line will fetch new message from pubsub
    subscription_name = subscription_name
    subscription_path = "projects/{0}/subscriptions/(1)".format(project_id,subscription_name)
    try:
        future.result()
        print("message processed",future.result())

    except KeyboardInterrupt:
        # User  exits the script early.
        future.cancel()             #to cancel the process with keyboard interrupt Ctrl+c
    print("terminated")        

if __name__ == '__main__':
    main()
