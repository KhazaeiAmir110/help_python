import redis

redis_ = redis.Redis(db=3)

redis_.set('name', 'amir')
redis_.set('age', 33)
