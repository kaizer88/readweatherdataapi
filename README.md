# Weather API

This APIView simply post requested weather forecast, a user need to request the city and number of days of the forecast. 

This API limits you to 3 cities and 5 days of forecast max.

You can only search for towns below:

```bash
[Cape Town, Durban, Johannesburg]
```

## Link

[App link](https://lukhanyo.pythonanywhere.com/) 

## Installation

### Setting up environment
```
python3 -m venv venv
source env/bin/activate
pip3 install -r requirements.txt
```
## Running application
```
cd readweatherdataapi\src
python3 manage.py runserver
```
