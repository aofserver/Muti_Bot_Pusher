import mysql.connector
import pandas as pd
import json

host="127.0.0.1"
user="root"
password=""
database="line_test"
port='3306'

def GetAllMember(id=None):
    mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
            )
    cursor = mydb.cursor()
    if id is None:
        sql_cmd = f"SELECT * FROM app_profileuser JOIN app_profilebot ON app_profileuser.bot_id = app_profilebot.id"
    else:
        sql_cmd = f"SELECT * FROM app_profileuser JOIN app_profilebot ON app_profileuser.bot_id = app_profilebot.id WHERE app_profileuser.bot_id = {id}"
    cursor.execute(sql_cmd)
    df = pd.DataFrame(data=list(cursor),columns = cursor.column_names)
    allUser = {}
    for index, row in df.iterrows():
        if row["bot_id"] in allUser.keys():
            allUser[row["bot_id"]]["member"] = { row["userid"]: {
                                                                    "name":row["username"],
                                                                    "userid":row["userid"]
                                                               }
                                               } 
        else:
            allUser[row["bot_id"]] = {
                                            "botid":row["botid"],
                                            "botname":row["botname"],
                                            "member":{}
                                     }
            allUser[row["bot_id"]]["member"] = { row["userid"]: {
                                                                    "name":row["username"],
                                                                    "userid":row["userid"]
                                                               }
                                               } 
    cursor.close()
    return allUser
# allUser : {
#                 idbot:{
#                         botid:str,
#                         botname:str,
#                         member,{
#                                 userid:{
#                                         name:str,
#                                         userid:str
#                                         }
#                         }
#                 }
#           }



def GetHistoryMessage(data):
    mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
            )
    cursor = mydb.cursor()
    sql_cmd = f"SELECT * FROM app_messagedata WHERE (send_from='{data['userId']}' OR receive='{data['userId']}') AND bot_id={data['idbot']}"
    cursor.execute(sql_cmd)
    df = pd.DataFrame(data=list(cursor),columns = cursor.column_names)
    message_list = []
    for index, row in df.iterrows():
        data = {"from":row.send_from,"to":row.receive,"type_message":row.type_message,"message":json.loads(row.message),"timestamp":row.timestamp.to_pydatetime().isoformat()}
        message_list.append(data)
    cursor.close()
    return message_list

# message_list : {
#                     from:str,
#                     to:str,
#                     type_message:str,
#                     message":json,
#                     timestamp:str
#                }


def GetEnpointBot(data):
    mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
            )
    cursor = mydb.cursor()
    sql_cmd = f"SELECT * FROM app_enpointbot WHERE bot_id={data['idbot']}"
    cursor.execute(sql_cmd)
    df = pd.DataFrame(data=list(cursor),columns = cursor.column_names)
    cursor.close()
    return df.iloc[0]['endpoint']

# http://localhost:8001


    











