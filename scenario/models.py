# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Scenario(models.Model):
    task = models.TextField()

class Response(models.Model):
    task = models.ForeignKey(Scenario)
    value = models.TextField()
    count = models.IntegerField()