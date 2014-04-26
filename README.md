Agiler
======

Django based application to simplify some Scrum routines


## Initial setup

Create SQLite3 database file by running the following command:
```bash
$ python manage.py syncdb --noinput
```
Load initial data into new database:
```bash
$ python manage.py loaddata essentialdata.json
$ python manage.py loaddata initialdata.json
```
