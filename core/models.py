from django.db import models
from django.utils import timezone


class TimeSheetPediod(models.Model):

    start_time = models.DateTimeField(default=timezone.now)
