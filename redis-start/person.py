import json

import redis

redis_connect = redis.Redis(db=2)

with open("persons.json") as js:
    date = json.load(js)

with redis_connect.pipeline(date) as pipe:
    for id_data, person in enumerate(date, start=1):
        pipe.hsetnx("person", id_data, str(person))
    pipe.execute()
