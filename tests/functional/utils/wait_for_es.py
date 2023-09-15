import time

from elasticsearch import Elasticsearch

# TODO still trouble with PATHS
# TODO from functional.settings import test_settings

if __name__ == '__main__':
    es_client = Elasticsearch(hosts='http://elasticsearch:9200')
    while True:
        response = es_client.ping()
        if not response:
            continue
        health_response = es_client.cluster.health(wait_for_status="yellow", timeout="20s")
        if not health_response:
            continue
        if health_response['status'] == 'yellow':
            break
        time.sleep(1)
    es_client.close()
