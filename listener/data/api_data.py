import requests
from .sample_mandrill import mandrill_data 
import json
from random import randint
from datetime import datetime


def get_api_data():
    # The mandril URL goes here. Activate block if Authenticated API from Mandrill is available
    # mandrill_data = '#url_here'
    # data = requests(mandrill_data)

    """ 
    Data generation to mimic live responses from Mandrill

    1. Importing the sample response data in json format - 'sample_mandrill.py
    2. Randomizing the response selection sequence to mimic the live API
    """ 
    
    response = json.loads(mandrill_data)
    random_integer = randint(0,9)
    # Note: Deactivate the block above if Authenticated API from Mandrill is available. 

    data = response[random_integer]
    message =  data['msg']


    # create a dictionary to unify data from the response by key-value combination with simpler db-focused references
    response_details = {}

    response_details = {
        'event':data['event'],
        'event_id' : data['_id'],
        'ts': str(datetime.fromtimestamp(data['ts'])),
        'message_ts': str(datetime.fromtimestamp([message][0]['ts'])),
        'subject': message['subject'],
        'email': message['email'],
        'sender': message['sender'],
        'tags': message['tags'],
        'state': message['state'],
        'message_id': message['_id'],
    }

    """
    - For data streams with no click time, open time, or url data, create dictionary keys with an empty list to create 
      consistency in data saved to database and prevent potential errors. 
    - Populate the keys with relevant data reflecting empty inputs. 
    """

    response_details['time_opened'] = str(datetime.fromtimestamp(message['opens'][0]['ts'])) if message.get('opens',[]) else 'Not Opened'
    response_details['time_clicked'] = str(datetime.fromtimestamp(message['clicks'][0]['ts'])) if message.get('clicks',[]) else '-'
    response_details['url_clicked'] = message['clicks'][0]['url'] if message.get('clicks',[]) else 'No URL'

    
    return response_details


