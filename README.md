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

## Installation

- 작동을 위해 NAS에서 `data`, `meida`, `db.sqlite3`를 이 프로젝트 폴더로 다운받으세요.

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

## Todo

- [x] [upload multi image](https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/)
- [x] [news template group by year](https://stackoverflow.com/questions/8678336/django-grouping-querysets-by-a-certain-field-in-template)
- [x] dockerizing
- [x] CI/CI: Docker deployment automation

### Refactoring

- [x] Bootstrap file -> cdn

#### DB화

> 빈번하게 업데이트가 발생하는 데이터에 대해서 DB화를 통해 관리를 용이하게 하기 위함

- [x] news
- [ ] alumini
- [ ] main
- [ ] publications

#### 중복 제거

> 유지보수 용이하게 하기 위함

- [ ] common: html header
- [ ] area: 동일한 css class화

#### Error

- [x] Research/Project: CSS 레이아웃 다름
- [x] Research/Project: dropdown 작동하지 않는 문제
