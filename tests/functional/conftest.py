from pprint import pprint
from typing import List

import aiohttp
import pytest
import json

import pytest_asyncio

from functional.settings import test_settings
from elasticsearch import AsyncElasticsearch


@pytest.fixture
def es_write_data_OLD():
    async def inner(data: List[dict]):
        bulk_query = get_es_bulk_query(data, test_settings.es_index, test_settings.es_id_field)
        # str_query = '\n'.join(bulk_query) + '\n'

        es_client = AsyncElasticsearch(hosts=[test_settings.es_host])
        response = await es_client.bulk(operations=bulk_query, refresh=True)
        await es_client.close()
        if response['errors']:
            raise Exception('Ошибка записи данных в Elasticsearch')
    return inner


@pytest.fixture(scope='session')
async def es_client():
    client = AsyncElasticsearch(hosts=[test_settings.es_host])
    yield client
    await client.close()


@pytest.fixture
def es_write_data(es_client: AsyncElasticsearch):
    async def inner(data: list[dict]):
        print('HERE1')
        print(test_settings.es_index,test_settings.es_id_field)
        bulk_query = get_es_bulk_query(data, test_settings.es_index,
                                       test_settings.es_id_field)
        print('HERE2')
        response = await es_client.bulk(operations=bulk_query,
                                        refresh=True)  # it works...
        print('HERE3')
        if response['errors']:
            raise Exception('Ошибка записи данных в Elasticsearch')

    print('HERE4')
    return inner


def get_es_bulk_query(es_data: list[dict], es_index: str, es_id_field: str):
    bulk_query = []
    for row in es_data:
        bulk_query.extend([
            json.dumps({'index': {'_index': es_index,
                                  '_id': row[es_id_field]}}),
            json.dumps(row)
        ])
    return bulk_query


@pytest.fixture(scope='session')
async def http_session():
    async with aiohttp.ClientSession() as session:
        yield session


@pytest.fixture
def make_get_request():
    async def inner(path, query_data):
        async with aiohttp.ClientSession() as session:
            url = f'{test_settings.service_url}{path}'
            async with session.get(url, params=query_data) as response:
                return await response.json(), response.headers, response.status
    return inner

