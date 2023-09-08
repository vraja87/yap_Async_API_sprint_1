import time

from redis.asyncio import Redis

from settings import test_settings

if __name__ == '__main__':
    es_client = Redis(host=f'http://{test_settings.redis_host}:9200')
    while True:
        if es_client.ping():
            break
        time.sleep(1)
