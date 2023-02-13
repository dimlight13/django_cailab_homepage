# Cailab Homepage

## Library

| name                                                                               | version | description                                                                          |
| ---------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------ |
| [django](https://www.djangoproject.com/)                                           | 4.1.4   | web server framework                                                                 |
| [django-hitcount](https://django-hitcount.readthedocs.io/en/latest/)               | 1.3.5   | track the number of hits (views) for a particular object                             |
| [pandas](https://pandas.pydata.org/)                                               | 1.5.2   | data analysis and manipulation tool                                                  |
| [Pillow](https://pillow.readthedocs.io/en/stable/)                                 | 9.3.0   | Python Imaging Library                                                               |
| [autopep8](https://pypi.org/project/autopep8/)                                     | 2.0.0   | python code formatter                                                                |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/)                             | 3.0.10  | A Python library to read/write Excel 2010                                            |
| [django-jazzmin](https://django-jazzmin.readthedocs.io/)                           | 2.6.0   | django admin adminlte3 theme                                                         |
| [django-admin-ip-restrictor](https://pypi.org/project/django-admin-ip-restrictor/) | 2.2.0   | A Django middleware to restrict the access to the Django admin based on incoming IPs |

## Command

- default setting

```shell
virtualenv venv
venv/Scripts/activate
pip install -r requirements.txt
```

- run server

```shell
python manage.py runserver
```

- migration

```shell
python manage.py makemigrations
python manage.py migrate
```

- build static file

```shell
python manage.py collectstatic
```
