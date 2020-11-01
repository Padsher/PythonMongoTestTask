# Python test task

Was tested on python 3.7.4

## Pre install
### Install dependencies
```
python -m pip install -r ./requirements.txt
```

### Fill configs
```
./config/database.py
./config/server.py
```

### Start your MongoDB
For example
```
docker run -d -p 27017:27017 mongo
```

## Run server
```
python main.py
```

## List of cURL test commands
Those commands for server on localhost, 8080 port
### Fill with various data
Firstly clear all products (route for several tests in a row)
```
curl --request DELETE \
  --url http://localhost:8080/product
```
---------------------------------------------
3 products, two with equal name, two with equal property
```
curl --request POST \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "name": "phone",
        "description": "luxury phone",
        "properties": {
            "price": 120000,
            "color": "red"
        }
    }'

curl --request POST \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "name": "phone",
        "description": "budget phone",
        "properties": {
            "price": 20000,
            "color": "blue"
        }
    }'

curl --request POST \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "name": "laptop",
        "description": "luxury laptop",
        "properties": {
            "price": 120000,
            "color": "blue"
        }
    }'
``` 
-------------------------
Then lets test filtering
```
Get 1 and 2
```
```
curl --request GET \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "name": "phone"
    }'
```
```
Get 1 and 3
```
```
curl --request GET \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "properties": { "price": 120000 }
    }'
```
```
Get 2 and 3
```
```
curl --request GET \
  --url http://localhost:8080/product \
  --header 'content-type: application/json' \
  --data '{
        "properties": { "color": "blue" }
    }'
```

--------------------------
Then get by id (Put your id after ...product/)
```
curl --request GET \
  --url http://localhost:8080/product/5f9c3a0955084919feee1b7b
```