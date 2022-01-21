from django.shortcuts import render
from .models import MandrillResponse

def render_index(request):
    # Obtain all response data from the database for listing on the frontend. 

    data = MandrillResponse.objects.all()
    context_dict = {
        'data' : data,
    }
    return render(request, 'index.html', context = context_dict)

def save_to_database(data):
    """
    To prevent duplication of message objects in the database,
    - Try to obtain the data object by message_id (primary key) to update the click and open times. 
    - Create a new object if it does not exist in the database. 

    - This function is invoked as a task by Celery
    """

    try:
        db_obj = MandrillResponse.objects.get(message_id = data['message_id'])

        # Update time when an email is opened or URL is clicked
        db_obj.time_opened = data['time_opened']
        db_obj.time_clicked = data['time_clicked']
        db_obj.save()

    except MandrillResponse.DoesNotExist:
        db_data = MandrillResponse.objects.create(
            event = data['event'],
            event_id = data['event_id'],
            ts = data['ts'],
            message_ts = data['message_ts'],
            subject = data['subject'],
            email = data['email'],
            sender = data['sender'],
            tags = data['tags'],
            state = data['state'],
            message_id = data['message_id'],
            time_opened = data['time_opened'],
            time_clicked = data['time_clicked']
        )
        return db_data