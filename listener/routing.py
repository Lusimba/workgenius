from django.urls import path
from .consumers import DataConsumer

# Define websocket URL patterns
ws_urlpatterns = [
    path('ws/mandrill/view_all/', DataConsumer.as_asgi())
]