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


# Migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate app
```

# Run
```
$ python3 manage.py runserver 0.0.0.0:8001
```
