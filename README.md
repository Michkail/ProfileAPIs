# ProfileAPIs
```
For requirements or additional libarary you can click
on the 'requirements.txt' or you can see below
```

### The requirements.txt
```
asgiref==3.4.1
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.9
cryptography==36.0.1
defusedxml==0.7.1
Django==3.2
django-allauth==0.47.0
django-rest-auth==0.9.5
djangorestframework==3.13.1
idna==3.3
oauthlib==3.1.1
Pillow==8.4.0
psycopg2==2.9.2
pycparser==2.21
PyJWT==2.3.0
python3-openid==3.2.0
pytz==2021.3
requests==2.26.0
requests-oauthlib==1.3.0
six==1.16.0
sqlparse==0.4.2
urllib3==1.26.7
```

## Folder Structure
```
    ProfileAPIs
        |\_____ apisprofile
        |         |\_____ __pycache__
        |         |         |\_____ __init__.cpython-39.pyc
        |         |         |\_____ settings.cpython-39.pyc
        |         |         |\_____ urls.cpython-39.pyc
        |         |          \_____ wsgi.cpython-39.pyc
        |         |  
        |         |\_____ __init__.py
        |         |\_____ settings.py
        |         |\_____ urls.py
        |          \_____ wsgi.py
        |
        |\_____ clients
        |         |\_____ token-auth-test0.py
        |          \_____ token-auth-test1.py
        |
        |\_____ profiles
        |         |\_____ __pycache__
        |         |         |\_____ __init__.cpython-39.pyc
        |         |         |\_____ admin.cpython-39.pyc
        |         |         |\_____ apps.cpython-39.pyc
        |         |         |\_____ models.cpython-39.pyc
        |         |          \_____ signals.cpython-39.pyc
        |         |    
        |         |\_____ api
        |         |         |\_____ __pycache___
        |         |         |         |\permissions.cpython-39.pyc
        |         |         |         |\serializers.cpython-39.pyc
        |         |         |         |\urls.cpython-39.pyc
        |         |         |          \views.cpython-39.pyc
        |         |         |
        |         |         |\_____ permissions.py
        |         |         |\_____ serializers.py
        |         |         |\_____ urls.py
        |         |          \_____ views.py
        |         |
        |         |\_____ migrations
        |         |         |\_____ __pycache__
        |         |         |         |\_____ __init__.cpython-39.pyc
        |         |         |          \_____ 0001_initial.cpython-39.pyc
        |         |         |
        |         |         |\_____ __init__.py
        |         |          \_____ 0001_initial.py
        |         |
        |         |\_____ __init__.py
        |         |\_____ admin.py
        |         |\_____ apps.py
        |         |\_____ models.py
        |         |\_____ signals.py
        |         |\_____ tests.py
        |          \_____ views.py
        |
        |\_____ uploads.py       
        |\_____ manage.py       
         \_____ requirements.py       
```

## Only two model is needed for the project, you can call it Profile & ProfileStatus. It must have the following fields:
### Model for Profile
```
♬  user
♫  bio
♩  city
♪  avatar
```

### Model for ProfileStatus
```
♬  user_profile
♫  status_content
♩  created_at
♪  updated_at
```