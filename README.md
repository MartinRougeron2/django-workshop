# django-workshop
# use this
```
python3 -m venv .venv
source .venv/bin/activate
# install python python3-dev(el)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver
```