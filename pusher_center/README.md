# pusher_center
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
edit file `pusher_center/app/database.py` to set `host,user,password,database,port`

# Config pusher
edit file `pusher_center/app/views.py` to set `app_id,key,secret,cluster` in `line 16` 

# Run
```
$ python3 manage.py runserver 0.0.0.0:8000
```


# Front-end Test
```
http://127.0.0.1:8000
```
