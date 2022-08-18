import os

import redis

redis = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASS'))


def print_numbers(numbers):
    for num in numbers:
        print(num.decode())


redis.delete('numbers')
redis.delete('vehicles')

redis.zadd('vehicles', {'car': 3})
redis.zadd('vehicles', {'bike': 2})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)

for i in range(0, 100):
    redis.zadd('numbers', {i + 1: i})

print("Order they were added:")
print_numbers(redis.zrange('numbers', 0, -1))

print("Reverse order:")
print_numbers(redis.zrevrange('numbers', 0, -1))
