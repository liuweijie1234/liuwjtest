# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class WeChatUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE)
    motto = models.CharField(max_length=200, null=True, blank=True, default="")
    pic = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=60, null=True, blank=True, default="")
    email = models.CharField(max_length=60, null=True, blank=True, default="")

    def __str__(self):
        return self.user.username

class Status(models.Model):
    user = models.ForeignKey(WeChatUser, models.CASCADE)
    text = models.CharField(max_length=500)
    pics = models.CharField(max_length=200, null=True, blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-id"]
