from django.db import models

# Create your models here.

class ProfileBot(models.Model):
  botid = models.CharField(max_length=20,null = True, blank=True)
  botname = models.CharField(max_length=50,null = True, blank=True)
  botdetail = models.CharField(max_length=100,null = True, blank=True)
  platform = models.CharField(max_length=100,null = True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True,null = True, blank=True)

class ProfileUser(models.Model):
  bot = models.ForeignKey(ProfileBot, on_delete=models.CASCADE)
  userid = models.CharField(max_length=50,null = True, blank=True)
  username = models.CharField(max_length=100,null = True, blank=True)
  userdetail = models.CharField(max_length=100,null = True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True,null = True, blank=True)

class MessageData(models.Model):
  bot = models.ForeignKey(ProfileBot, on_delete=models.CASCADE)
  send_from = models.CharField(max_length=50,null = True, blank=True)
  receive = models.CharField(max_length=50,null = True, blank=True)
  type_message = models.CharField(max_length=100,null = True, blank=True)
  message = models.JSONField(null = True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True,null = True, blank=True)

class EnpointBot(models.Model):
  bot = models.ForeignKey(ProfileBot, on_delete=models.CASCADE)
  endpoint = models.CharField(max_length=50,null = True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True,null = True, blank=True)
