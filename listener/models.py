from django.db import models

class MandrillResponse(models.Model):
    event = models.CharField(max_length=50, null=True, blank=True)
    event_id = models.IntegerField(null=True, blank=True)
    ts = models.CharField(max_length=50, null=True, blank=True)
    message_ts = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    sender = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

    #message ID is the primary key
    message_id = models.IntegerField(primary_key=True)
    time_opened = models.CharField(max_length=50, null=True, blank=True)
    time_clicked = models.CharField(max_length=50, null=True, blank=True)
    url_clicked = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.email}'