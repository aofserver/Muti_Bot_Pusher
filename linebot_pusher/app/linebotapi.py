
import json
import requests



Bot_basic_id = "@678tbhfr"
Channel_secret = "8d9dea0ac4e1dca18b20b8817bed4cb1"
Channel_access_token = 'MEHHmo0chIX8ldVTNcHXeVw5XSjhlFY7jWcOCGf/w0aaWk3qfCKG3uGAfEBrFKNPp2vwgnxbni2tvWMr+hzRD7BMEx2fPlpHq5ouPfR6BDtltkcyuvkkh8ledsXWO6VTMhWD4X7nmuk4YDLF0PLGJwdB04t89/1O/w1cDnyilFU='

def LineNotify(msg):
  url = 'https://notify-api.line.me/api/notify'
  token = 'IkgTg38dY66EjKAewQHCFwmZ3e47bjbBFqdsap8UKK8' #Line Token Notify
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
            "text": "กรุณาเลือกตัวแปร",
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
                            "text": "แจ้งเตือน",
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
                            "text": "ราคา BTC มากกว่า 1000 บาทแล้ว",
                            "align": "center",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "ราคาปัจจุบันอยู่ที่ 1000000 บาท",
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