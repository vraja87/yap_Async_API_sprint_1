import time

from elasticsearch import Elasticsearch

# TODO steel trouble with PATHS
# TODO from functional.settings import test_settings

if __name__ == '__main__':
    es_client = Elasticsearch(hosts='http://elasticsearch:9200')
    while True:
        response = es_client.ping()
        if response:
            break
        time.sleep(1)
    es_client.close()
