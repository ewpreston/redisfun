import redis

redis = redis.Redis(
    host='localhost',
    port='6379')

redis.delete('numbers')
redis.delete('vehicles')

redis.zadd('vehicles', {'car': 3})
redis.zadd('vehicles', {'bike': 2})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)

for i in range(0, 100):
    redis.zadd('numbers', {i + 1: i})

numbers = redis.zrange('numbers', 0, -1)
print(numbers)

print(redis.zrevrange('numbers', 0, -1))
