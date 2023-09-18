from typing import List

import aiohttp
import pytest
import json

import pytest_asyncio
from redis.asyncio import Redis

from functional.settings import test_settings
from elasticsearch import AsyncElasticsearch


@pytest.fixture(scope='session')
def redis_cleanup():
    """Cleanup redis cache."""
    async def inner():
        redis_client = Redis.from_url(test_settings.redis_host)
        await redis_client.flushall()
    return inner


@pytest.fixture(scope='session')
def es_del_idx():
    """Clean up whole elasticsearch index."""
    async def inner(es_idx):
        client = AsyncElasticsearch(hosts=[test_settings.es_host])
        await client.indices.delete(index=es_idx)
        await client.close()
    return inner


@pytest.fixture
async def es_write_persons(es_write_data_idx, es_del_idx):  # TODO del(?)
    async def inner(data: List[dict]):
        await es_write_data_idx(test_settings.es_index_persons, test_settings.es_id_field, data)
    return inner


@pytest.fixture(scope='function')
async def es_write_genres(es_write_data_idx, es_del_idx):  # TODO del(?)
    async def inner(data: List[dict]):
        await es_write_data_idx(test_settings.es_index_genres, test_settings.es_id_field, data)
    return inner


@pytest.fixture
async def es_write_movies(es_write_data_idx):  # TODO del(?)
    async def inner(data: List[dict]):
        await es_write_data_idx(test_settings.es_index_movies, test_settings.es_id_field, data)
    return inner


@pytest.fixture
def es_write(es_write_data_idx):
    async def inner(es_idx, data: List[dict]):
        await es_write_data_idx(es_idx, test_settings.es_id_field, data)
    return inner


# @pytest.fixture
@pytest.fixture(scope='function')
def es_write_data_idx():
    async def inner(es_index, es_id_field, data: List[dict]):
        bulk_query = get_es_bulk_query(data, es_index, es_id_field)
        es_client = AsyncElasticsearch(hosts=[test_settings.es_host])
        response = await es_client.bulk(operations=bulk_query, refresh=True)
        await es_client.close()
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


@pytest.fixture
def make_get_request():
    async def inner(path, query_data):
        async with aiohttp.ClientSession() as session:
            url = f'{test_settings.service_url}{path}'
            async with session.get(url, params=query_data) as response:
                return await response.json(), response.headers, response.status
    return inner


@pytest.fixture
def es_write_data_OLD(request):  # TODO del(?) refactor
    async def inner(data: List[dict]):
        marker = request.node.get_closest_marker("fixt_data")
        if marker is None:
            es_index = test_settings.es_index_movies
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