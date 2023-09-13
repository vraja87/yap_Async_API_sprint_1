from typing import List

import aiohttp
import pytest
import json

from functional.settings import test_settings
from elasticsearch import AsyncElasticsearch


@pytest.fixture
def es_write_data_OLD(request):
    async def inner(data: List[dict]):
        marker = request.node.get_closest_marker("fixt_data")
        if marker is None:
            es_index = test_settings.es_index
            es_id_field = test_settings.es_id_field
        else:
            es_index = marker.kwargs['es_index']
            es_id_field = marker.kwargs['es_id_field']

        bulk_query = get_es_bulk_query(data, es_index, es_id_field)

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
def es_write_data(request, es_client: AsyncElasticsearch):
    async def inner(data: list[dict]):
        marker = request.node.get_closest_marker("fixt_data")
        if marker is None:
            es_index = test_settings.es_index
            es_id_field = test_settings.es_id_field
        else:
            es_index = marker.kwargs['es_index']
            es_id_field = marker.kwargs['es_id_field']
        bulk_query = get_es_bulk_query(data, es_index, es_id_field)
        response = await es_client.bulk(operations=bulk_query,
                                        refresh=True)  # it works...
        if response['errors']:
            raise Exception('Ошибка записи данных в Elasticsearch')
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

