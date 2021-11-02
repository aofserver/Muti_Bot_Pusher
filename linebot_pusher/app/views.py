import os
import json
import time
import pusher
import app.linebotapi as bot
import app.huawei_cloud_obs as obs
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from django.db.models import Q
from app.models import ProfileBot, ProfileUser, MessageData
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django import db
from botnoi import scrape as sc
from decimal import *



pusher_client = pusher.Pusher(
  app_id='',
  key='',
  secret='',
  cluster='',
  ssl=True
)


def GetContentAndUpload(messageID,userID,pathfile,filename):
  urlfile = ''
  if bot.GetContent(messageID,userID,pathfile):
    urlfile = obs.Uploadfile(obs.bucketName,pathfile,filename,1,bot.Bot_basic_id,userID)
    os.remove(pathfile)
  return urlfile

def SaveUserProfile(userID):
  id = ProfileBot.objects.filter(botid=bot.Bot_basic_id)[0].id
  data_query = ProfileUser.objects.filter(userid=userID,bot_id=id)
  if len(data_query) == 0:
    profileuser = bot.GetProfileUser(userID)
    s = ProfileUser(userid=userID,username=profileuser["displayName"],userdetail='',bot_id=id)
    s.save()

def SaveMessage(send_from,receive,type_message,message):
  botid = ProfileBot.objects.filter(botid=bot.Bot_basic_id)[0].id
  s = MessageData(send_from=send_from,receive=receive,type_message=type_message,message=message,bot_id=botid)
  s.save()

def AutoReplyMessage(message,userID,Reply_token):
  listtext = ['สวัสดี','หวัดดี']
  if listtext[0] in message or listtext[1] in message:
    Reply_messasge = 'สวัสดีครับ ต้องการสั่งซื้อสินค้าชิ้นไหนสอบถามได้เลยครับ'
    SaveMessage("admin",userID,"text",{'data':Reply_messasge})
    bot.ReplyMessage(Reply_token, Reply_messasge)


@csrf_exempt
def Home(request):
  return render(request,'pusher.html')


@csrf_exempt
def Test(request):
  if request.method == "GET":
    payload = json.loads(request.body)
    print("----------")
    print("[ payload ]          ", payload)
    print("----------")
    return JsonResponse({"msg":"This method GET."},safe=False)
  elif request.method == "POST":
    payload = json.loads(request.body)
    print("----------")
    print("[ payload ]          ", payload)
    print("----------")
    return JsonResponse({"msg":"This method POST."},safe=False)
  else:
    return JsonResponse({"msg":"not subport this method."},safe=False)


@csrf_exempt
def Webhook_Line(request):
  if request.method == "POST":
    payload = json.loads(request.body)
    print("-------------Line-------------")
    print(payload)
    print("------------------------------")

    if payload['events'] == []:
      print("Verify Webhook.")
    else:
      Reply_token = payload['events'][0]['replyToken']
      type_message = payload['events'][0]['message']['type']
      messageID = payload['events'][0]['message']['id']
      userID = payload['events'][0]['source']['userId']

      SaveUserProfile(userID)

      if type_message == 'text':
        message = payload['events'][0]['message']['text']
        SaveMessage(userID,"admin","text",{'data':message})
        idbot = ProfileBot.objects.filter(botid=bot.Bot_basic_id)[0].id
        data = {"userId": userID,"idbot":idbot,"platform":"line","type_message":type_message,"message":message}
        pusher_client.trigger('private-ChannelBot', 'client-MessageUser', data)
        AutoReplyMessage(message,userID,Reply_token)

      if type_message == 'sticker':
        stickerId = messageID = payload['events'][0]['message']['stickerId']
        data = {"stickerId":stickerId}
        SaveMessage(userID,"admin","sticker",{'data':stickerId})
        # Reply_messasge = 'ยังไม่สามารถรับรู้ sticker ได้ในขณะนี้'
        # bot.ReplyMessage(Reply_token, Reply_messasge)

      if type_message == 'image':
        filename = "{}_{}.png".format(userID,time.time())
        pathfile = os.path.join(os.getcwd(),"app","tmp",filename)
        url = GetContentAndUpload(messageID,userID,pathfile,filename)
        SaveMessage(userID,"admin","image",{'data':url})
        idbot = ProfileBot.objects.filter(botid=bot.Bot_basic_id)[0].id
        data = {"userId": userID,"idbot":idbot,"platform":"line","type_message":type_message,"message":url}
        pusher_client.trigger('private-ChannelBot1', 'client-MessageUser', data)
        Reply_messasge = 'ได้รับสลิปจากท่านแล้ว ทางเรากำลังอยู่ระะหว่างการดำเนินการตรวจสอบ'
        SaveMessage("admin",userID,"text",{'data':Reply_messasge})
        bot.ReplyMessage(Reply_token, Reply_messasge)

      if type_message == 'video':
        filename = "{}_{}.mp4".format(userID,time.time())
        pathfile = os.path.join(os.getcwd(),"app","tmp",filename)
        url = GetContentAndUpload(messageID,userID,pathfile,filename)
        SaveMessage(userID,"admin","video",{'data':url})
        idbot = ProfileBot.objects.filter(botid=bot.Bot_basic_id)[0].id
        data = {"userId": userID,"idbot":idbot,"platform":"line","type_message":type_message,"message":url}
        pusher_client.trigger('private-ChannelBot1', 'client-MessageUser', data)
        Reply_messasge = 'ได้รับคลิปวีดีโอจากท่านแล้ว ทางเรากำลังอยู่ระะหว่างการดำเนินการตรวจสอบ'
        SaveMessage("admin",userID,"text",{'data':Reply_messasge})
        bot.ReplyMessage(Reply_token, Reply_messasge)

      if type_message == 'audio':
        filename = "{}_{}.mp3".format(userID,time.time())
        pathfile = os.path.join(os.getcwd(),"app","tmp",filename)
        url = GetContentAndUpload(messageID,userID,pathfile,filename)
        SaveMessage(userID,"admin","audio",{'data':url})
        # Reply_messasge = 'ยังไม่สามารถรับรู้เสียงได้ในขณะนี้'
        # bot.ReplyMessage(Reply_token, Reply_messasge)

      if type_message == 'file':
        filename = "{}_{}.file".format(userID,time.time())
        pathfile = os.path.join(os.getcwd(),"app","tmp",filename)
        url = GetContentAndUpload(messageID,userID,pathfile,filename)
        SaveMessage(userID,"admin","file",{'data':url})
        # Reply_messasge = 'ยังไม่สามารถรับรู้ไฟล์ได้ในขณะนี้'
        # bot.ReplyMessage(Reply_token, Reply_messasge)

      if type_message == 'location':
        latitude = messageID = payload['events'][0]['message']['latitude']
        longitude = messageID = payload['events'][0]['message']['longitude']
        address = messageID = payload['events'][0]['message']['address']
        data = {"latitude":latitude,"longitude":longitude,"address":address}
        SaveMessage(userID,"admin","file",{'data':data})
        # Reply_messasge = 'ยังไม่สามารถรับรู้สถานที่ได้ในขณะนี้'
        # bot.ReplyMessage(Reply_token, Reply_messasge)

    return JsonResponse({"msg":"This Webhook."},safe=False,status=200)

  elif request.method == "GET":
    return JsonResponse({"msg":"Can not 'GET' Webhook."},safe=False,status=400)
  else:
    return JsonResponse({"msg":"not subport this method."},safe=False,status=400)



@csrf_exempt
def Webhook_Pusher(request):
  if request.method == "POST":
    token = request.headers["Authorization"].split(" ")
    print(token[1])
    if token[1] != "linebotbkk": #set env token
      return JsonResponse({"msg":"fail"},safe=False,status=200)
    payload = json.loads(request.body)
    print("------------Pusher------------")
    print(payload)
    print("------------------------------")
    for event in payload["events"]:
      dataMessage = json.loads(event["data"])
      if dataMessage['platform'] == 'line':
        SaveMessage("admin",dataMessage['userId'],dataMessage['type_message'],{'data':dataMessage["message"]})
        bot.PushMessage(dataMessage['userId'],dataMessage["message"])
    return JsonResponse({"msg":"ok"},safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)


@csrf_exempt
def History_Message(request):
  if request.method == "POST":
    token = request.headers["Authorization"].split(" ")
    if token[1] != "linebotbkk": #set env token
      return JsonResponse({"msg":"fail"},safe=False,status=200)
    payload = json.loads(request.body)
    id = ProfileBot.objects.filter(botid=payload["botId"])[0].id
    data_query = MessageData.objects.filter((Q(send_from=payload["userId"]) | Q(receive=payload["userId"])) & Q(bot_id=id))

    message_list = []
    for i in range(len(data_query)):
      data = {"from":data_query[i].send_from,"to":data_query[i].receive,"type_message":data_query[i].type_message,"message":data_query[i].message,"timestamp":data_query[i].timestamp}
      message_list.append(data)

    return JsonResponse(message_list,safe=False,status=200)
  else:
    return JsonResponse({"msg":"Wrong method!"},safe=False,status=400)
