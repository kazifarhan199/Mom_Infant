from django.db import models
from django.db.models.signals import post_save
from .signals import postSaveRawDataSignal
import json

class RawData(models.Model):
    date = models.DateTimeField(auto_now=True)
    data = models.TextField()
    tag = models.CharField(max_length=200)
    main = models.CharField(max_length=200)

    def __str__(self):
        return str(self.tag) + " ==> " + str(self.date.date())+ " ==> "+ str(self.date.time().hour) + ":"+ str(self.date.time().minute) + " ==> " + str(self.tag)

    def get_json(self):
        return json.loads(self.data)

post_save.connect(postSaveRawDataSignal, sender=RawData)