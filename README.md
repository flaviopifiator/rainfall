Rainfall
========
RestAPI of precipitation in soils.

Requirements
------------
- docker
- docker-compose

Run project
------------
- docker-compose up -d
- docker exec django ./manage.py loaddata initial_data.json

Auth Admin
----------
- username: admin
- password: admin

Available endpoints
-------------------

**List of floors**
[http://localhost:8000/api/v1/floor/](http://localhost:8000/api/v1/floor/)

Example to use query params
- [GET] [http://localhost:8000/api/v1/floor/?last_days=2](http://localhost:8000/api/v1/floor/?last_days=2) Average rainfall in the last days, between 1 and 7 days.
- [GET] [http://localhost:8000/api/v1/floor/?precipitations__gt=555](http://localhost:8000/api/v1/floor/?precipitations__gt=555) Filters those soils where their historical precipitation is higher than the declared value.


**List of rains**
[http://localhost:8000/api/v1/rain/](http://localhost:8000/api/v1/rain/)
Example to use query params
- [GET] [http://localhost:8000/api/v1/rain/?floor__name=campo1](http://localhost:8000/api/v1/rain/?floor__name=campo1) Filter precipitation by soil name
- [GET] [http://localhost:8000/api/v1/rain/?floor__id=2](http://localhost:8000/api/v1/rain/?floor__id=2) Filter precipitation by soil id


**Create rain**
- [POST] [http://localhost:8000/api/v1/rain/](http://localhost:8000/api/v1/rain/)
