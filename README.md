1337
====
#Installation
###Create Virtualenv
```
virtualenv env --no-site-packages
```
###Install all requirements
```
. env/bin/activate
pip install -r requirements/base.txt
```
###Configure application
There are dev/production settings templates you can use in directory 'pro_tips/settings'.
####Set database in chosen settings file. Default:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pro_tips',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
####Create database structure
```
python manage.py syncdb --settings=pro_tips.settings.chosen_settings_file
python manage.py runserver --settings=pro_tips.settings.chosen_settings_file
```


django project 
our inspiration
http://codingstyleguide.com/
