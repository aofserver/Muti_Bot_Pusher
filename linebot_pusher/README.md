# linebot_backend
make by sarawut nacwijit

# Requirement 
```
python3
```

# Create a virtual environment
Windows
```
$ pip3 install virtualenv
$ virtualenv venv

activate environment
$ venv\Scripts\activate

deactivate environment
$ deactivate
```

Linux
```
$ sudo apt install virtualenv
$ virtualenv venv

activate environment
$ source venv/bin/activate

deactivate environment
$ deactivate
```

# Install
```
$ pip3 install -r requirements.txt
```

# Config database
```
edit file `linebot_pusher/core/settings.py` to set `host,user,password,database,port` in `line 96`
```

# Config huawei cloud obs
```
edit file `linebot_pusher/app/huawei_cloud_obs.py` to set `host,user,password,database,port` in `line 26`
```

# Config line bot
```
edit file `linebot_pusher/app/linebotapi.py` to set `Bot_basic_id,Channel_secret,Channel_access_toke` in `line 5`
```

# Config pusher
```
edit file `pusher_center/app/views.py` to set `app_id,key,secret,cluster` in `line 21` 
```

# Migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate app
```

# Run
```
$ python3 manage.py runserver 0.0.0.0:8001
```
