#!/usr/bin/python
# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

"""
 This sample demonstrates how to do common operations in temporary signature way
 on OBS using the OBS SDK for Python.
"""

from __future__ import print_function
import sys
from obs import ObsClient, CorsRule, const
from obs.convertor import Convertor
from obs.util import base64_encode, md5_encode

AK = ''
SK = ''
bucketName = ''
objectKey = ''
server = ''
AccessDomainName = ""

IS_PYTHON2 = sys.version_info.major == 2 or sys.version < '3'

if IS_PYTHON2:
    from urlparse import urlparse
    import httplib
else:
    import http.client as httplib
    from urllib.parse import urlparse

# Constructs a obs client instance with your account for accessing OBS
obsClient = ObsClient(access_key_id=AK, secret_access_key=SK, server=server, is_secure=False, signature='obs')


def doAction(msg, method, url, headers=None, content=None):
    url = urlparse(url)
    if headers is None:
        headers = {}
    conn = httplib.HTTPConnection(url.hostname, url.port)
    path = url.path + '?' + url.query
    conn.request(method, path, headers=headers)
    if content is not None:
        if not IS_PYTHON2 and not isinstance(content, bytes):
            content = content.encode('UTF-8')
        conn.send(content)
    result = conn.getresponse(True) if const.IS_PYTHON2 else conn.getresponse()
    status = result.status
    responseContent = result.read()
    if status < 300:
        print(msg + 'successfully.')
    else:
        print(msg + 'failed!!')
    
    return status < 300





def Uploadfile(bucketName,pathfile,objectKey,permisstion,bot_id,userid):
    #create folder
    obsClient.putContent(bucketName, "{}/{}/".format(bot_id,userid), '')

    #upload public file 
    obsClient.putFile(bucketName, "{}/{}/{}".format(bot_id,userid,objectKey), pathfile)

    #set permisstion file 
    permisstionlist = ['private','public-read','public-read-write']
    method = 'PUT'
    headers = {'x-obs-acl': permisstionlist[permisstion]}
    resp = obsClient.createSignedUrl(method, bucketName, "{}/{}/{}".format(bot_id,userid,objectKey), specialParam='acl', headers=headers)
    urlfile = ''
    if doAction('Upload object: ', method, resp['signedUrl'], resp['actualSignedRequestHeaders']):
        urlfile = "https://{ADN}/{bot_id}/{uerid}/{objectKey}".format(ADN=AccessDomainName,bot_id=bot_id,uerid=userid,objectKey=objectKey)
    return urlfile



def Deletefile(bucketName,objectKey,botid,userid):
    method = 'DELETE'
    res = obsClient.createSignedUrl(method, bucketName, "{}/{}/{}".format(botid,userid,objectKey))
    return doAction('Deleting object: ', method, res['signedUrl'], res['actualSignedRequestHeaders'])


#Test
filename = 'testimg2.png'
botid = "botid"
userid = "userid"
pathfileupload = 'D:/Web3/linebot_pusher/huaweicloud-sdk-python-obs/examples/test2.png'


# Upload object
# urlfile = UploadPublicfile(bucketName,pathfileupload,filename,1,botid,userid)
# print(urlfile)


# Delete object
# Deletefile(bucketName,filename,botid,userid)
