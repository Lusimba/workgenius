from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from listener.data.api_data import get_api_data
from .views import save_to_database

channel_layer = get_channel_layer()

@shared_task
def get_mandrill_data():
    # Obtain the data by running the 'get_api_data' function imported as above.
    response_details = get_api_data()

    # Run the 'save_to_database' function imported as above.
    save_to_database(response_details)

    # send processed data to the frontend websocket through django channels
    async_to_sync(channel_layer.group_send)('all_data', {'type': 'send_data', 'data' : response_details})