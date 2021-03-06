
import json
import requests

Bot_basic_id = ""
Channel_secret = ""
Channel_access_token = ""

def LineNotify(msg):
  url = 'https://notify-api.line.me/api/notify'
  token = '' #Line Token Notify
  headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
  r = requests.post(url, headers=headers, data = {'message':msg})



def GetProfileUser(userId):
  LINE_API = "https://api.line.me/v2/bot/profile/{}".format(userId)
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
  }
  response = requests.request("GET", LINE_API, headers=headers, data={})
  return json.loads(response.text)


def GetContent(messageId,userid,pathfile):
  LINE_API = "https://api-data.line.me/v2/bot/message/{messageId}/content".format(messageId=messageId)
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
  }
  try:
    response = requests.request("GET", LINE_API, headers=headers, data={})
  
  
    with open(pathfile,'wb') as f:
      f.write(response.content)
    return True
  except:
    return False



def setFomatText(Reply_token,text):
  return {
        "replyToken": Reply_token,
        "messages": [
                      {
                          "type":"text",
                          "text":text
                      },
                    ]
        }


def PushMessage(UserId,Message):
  LINE_API = 'https://api.line.me/v2/bot/message/push'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }

  Message = {
    "to": UserId,
    "messages": [
        {
          "type": "text",
          "text": Message
        }
    ]
  }

  data = Message
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def ReplyMessage(Reply_token,Message):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
        "replyToken": Reply_token,
        "messages": [
                      {
                          "type":"text",
                          "text":Message
                      },
                    ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def ReplyMessageImg(Reply_token,Message,Image):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
        "replyToken": Reply_token,
        "messages": [
                      {
                          "type":"text",
                          "text":Message
                      },
                      {
                          "type": "image",
                          "originalContentUrl": Image,
                          "previewImageUrl": Image
                      }
                    ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def QuickReplyyMessageParams(Reply_token):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  data = {
          "replyToken": Reply_token,
          "messages": [
            {
            "type": "text",
            "text": "????????????????????????????????????????????????",
            "quickReply": {
              "items": [
                        {
                          "type": "action",
                          "action": {
                                    "type":"message",
                                    "label":"Last",
                                    "text":"last"
                                    }
                        },
                        {
                          "type": "action",
                          "action": {
                                    "type":"message",
                                    "label":"Max24hr",
                                    "text":"max24hr"
                                    }
                        },
                        {
                          "type": "action",
                          "action": {
                                    "type":"message",
                                    "label":"Min24hr",
                                    "text":"min24hr"
                                    }
                        }
                      ]
                }
            }
          ]
        }
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)


def LinkRichManuOfUser(userId,display):
  LINE_API = 'https://api.line.me/v2/bot/user/{userId}/richmenu/{display}'.format(userId=userId,display=display)
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  r = requests.post(LINE_API, headers=headers)


def UnlinkRichManuOfUser(userId):
  LINE_API = 'https://api.line.me/v2/bot/user/{userId}/richmenu'.format(userId=userId)
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }
  r = requests.delete(LINE_API, headers=headers)


def TestMessage():
  LINE_API = 'https://api.line.me/v2/bot/message/push'
  Authorization = 'Bearer {}'.format(Channel_access_token)
  headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': Authorization
  }

  # Message = {
  #   "to": "U12162f974ac7a21fc1887b172755cca1",
  #   "messages": [
  #       {
  #         "type": "text",
  #         "text": "TEST"
  #       }
  #   ]
  # }

  Message = {
        "to": "U12162f974ac7a21fc1887b172755cca1",
        "messages": [
            {
                "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "bubble",
                    "direction": "ltr",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "???????????????????????????",
                            "weight": "bold",
                            "align": "center",
                            "contents": []
                        }
                        ]
                    },
                    "hero": {
                        "type": "image",
                        "url": "https://e7.pngegg.com/pngimages/404/606/png-clipart-computer-icons-computer-software-bell-angle-alarm.png",
                        "size": "full",
                        "aspectRatio": "1.51:1",
                        "aspectMode": "fit"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "???????????? BTC ????????????????????? 1000 ?????????????????????",
                            "align": "center",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "????????????????????????????????????????????????????????? 1000000 ?????????",
                            "color": "#FF0000FF",
                            "align": "center",
                            "contents": []
                        }
                        ]
                    }
                    }
            }
        ]
    }

  data = Message
  data = json.dumps(data)  ## dump dict >> Json Object
  r = requests.post(LINE_API, headers=headers, data=data)
