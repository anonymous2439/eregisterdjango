from django.db import models


class EventType(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    organizer = models.ForeignKey('accounts.user', on_delete=models.DO_NOTHING)
    event_type = models.ForeignKey('events.EventType', on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
