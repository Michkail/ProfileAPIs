# ProfileAPIs

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

## Only one model is needed for the project, you can call it SlurpOffer. It must have the following fields:
```
♬  company_name  
♫  company_email  
♩  job_title
♪  job_description
♬  fee  
♫  city  
♩  created_at
♪  available
```