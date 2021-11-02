import os
import json
import random
import time
import requests
import pusher
import app.database as databot
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from django import db
from decimal import *



pusher_client = pusher.Pusher(
  app_id='',
  key='',
  secret='',
  cluster='',
  ssl=True
)


def SendEventToWebhook(endpoint,payload):
  url = '{}/webhook_pusher'.format(endpoint)
  print(url)
  token = 'linebotbkk' #set env token
  headers = {'Content-type':'application/json',"Accept":"application/javascript",'Authorization':'Bearer '+token}
  r = requests.post(url, headers=headers, data=json.dumps(payload))

def HistoryMessage(endpoint,payload):
  url = '{}/history_message'.format(endpoint)
  token = 'linebotbkk' #set env token
  headers = {'Content-type':'application/json',"Accept":"application/javascript",'Authorization':'Bearer '+token}
  r = requests.post(url, headers=headers, data=json.dumps(payload))
  return json.loads(r.text)

@csrf_exempt
def Home(request):
  return render(request,'pusher.html')


@csrf_exempt
def Webhook_Pusher(request):
  if request.method == "POST":
    payload = json.loads(request.body)
    print("------------Pusher------------")
    print(payload)
    print("------------------------------")
    for event in payload["events"]:
      dataMessage = json.loads(event["data"])
      if dataMessage['platform'] == 'line':
        endpoint = databot.GetEnpointBot({'idbot':dataMessage['idbot']})
        SendEventToWebhook(endpoint,payload)
    return JsonResponse("ok",safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)



@csrf_exempt
def Pusher_Authentication(request):
  print(request.POST['channel_name'],request.POST['socket_id'])
  if request.method == "POST":
    auth = pusher_client.authenticate(
      channel=request.POST['channel_name'],
      socket_id=request.POST['socket_id']
    )
    return JsonResponse(auth,safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)



@csrf_exempt
def History_Message(request):
  if request.method == "POST":
    payload = json.loads(request.body)
    data = {"userId":payload["userId"],"idbot":payload["idbot"]}
    res = databot.GetHistoryMessage(data)
    return JsonResponse(res,safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)


@csrf_exempt
def AllMember(request):
  if request.method == "POST":
    payload = json.loads(request.body)
    if "idbot" in payload.keys():
      res = databot.GetAllMember(payload["idbot"])
    else:
      res = databot.GetAllMember()
    return JsonResponse(res,safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)
