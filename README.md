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
- docker-compose django ./manage.py loaddata ...

Available endpoints
-------------------

**List of floors**
[http://localhost:8000/api/v1/floor/](http://localhost:8000/api/v1/floor/)

Example to use query params
- [GET] [http://localhost:8000/api/v1/floor/?last_days=1](http://localhost:8000/api/v1/floor/?last_days=1) Average rainfall in the last days, between 1 and 7 days.
- [GET] [http://localhost:8000/api/v1/floor/?precipitations__gt=100.5](http://localhost:8000/api/v1/floor/?precipitations__gt=100.5) Filters those soils where their historical precipitation is higher than the declared value.


**List of rains**
[http://localhost:8000/api/v1/rain/](http://localhost:8000/api/v1/rain/)
Example to use query params
- [GET] [http://localhost:8000/api/v1/rain/?floor__name=name1](http://localhost:8000/api/v1/rain/?floor__name=name1) Filter precipitation by soil name
- [GET] [http://localhost:8000/api/v1/rain/?floor__id=1](http://localhost:8000/api/v1/rain/?floor__id=1) Filter precipitation by soil id


**Create rain**
[POST] [http://localhost:8000/api/v1/rain/](http://localhost:8000/api/v1/rain/)
