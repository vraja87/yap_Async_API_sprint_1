# TODO написать самим.
import time

from elasticsearch import Elasticsearch
from redis.asyncio import Redis

if __name__ == '__main__':
    es_client = Redis(hosts='http://localhost:9200')
    while True:
        if es_client.ping():
            break
        time.sleep(1)
