import time

from redis import Redis, ConnectionError

# TODO steel trouble with PATHS
# TODO from functional.settings import test_settings

if __name__ == '__main__':
    redis_client = Redis.from_url('redis://redis:6379')
    while True:
        try:
            response = redis_client.ping()
            if response:
                break
        except ConnectionError:
            pass
        time.sleep(1)
