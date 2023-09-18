import asyncio
import time

import aiohttp
import pytest
import json

from redis.asyncio import Redis

import pytest_asyncio
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from loguru import logger
import functional.testdata.es_backup as es_mapping
from functional.settings import test_settings


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


# @pytest.fixture
# def es_write(es_write_data_idx):
#     async def inner(es_idx, data: List[dict]):
#         await es_write_data_idx(es_idx, test_settings.es_id_field, data)
#     return inner


# @pytest.fixture
# @pytest.fixture(scope='function')
# def es_write_data_idx():
#     async def inner(es_index, es_id_field, data: List[dict]):
#         bulk_query = get_es_bulk_query(data, es_index, es_id_field)
#         es_client = AsyncElasticsearch(hosts=[test_settings.es_host])
#         response = await es_client.bulk(operations=bulk_query, refresh=True)
#         await es_client.close()
#         if response['errors']:
#             raise Exception('Ошибка записи данных в Elasticsearch')
#     return inner


def get_es_bulk_query(es_data: list[dict], es_index: str, es_id_field: str):
    bulk_query = []
    for row in es_data:
        bulk_query.extend([
            json.dumps({'index': {'_index': es_index,
                                  '_id': row[es_id_field]}}),
            json.dumps(row)
        ])
    return bulk_query


# @pytest.fixture
# def make_get_request():
#     async def inner(path, query_data):
#         async with aiohttp.ClientSession() as session:
#             url = f'{test_settings.service_url}{path}'
#             async with session.get(url, params=query_data) as response:
#                 return await response.json(), response.headers, response.status
#     return inner


# @pytest.fixture
# def es_write_data_OLD(request):  # TODO del(?) refactor
#     async def inner(data: List[dict]):
#         marker = request.node.get_closest_marker("fixt_data")
#         if marker is None:
#             es_index = test_settings.es_index_movies
#             es_id_field = test_settings.es_id_field
#         else:
#             es_index = marker.kwargs['es_index']
#             es_id_field = marker.kwargs['es_id_field']
#
#         bulk_query = get_es_bulk_query(data, es_index, es_id_field)
#
#         es_client = AsyncElasticsearch(hosts=[test_settings.es_host])
#         response = await es_client.bulk(operations=bulk_query, refresh=True)
#         await es_client.close()
#         if response['errors']:
#             raise Exception('Ошибка записи данных в Elasticsearch')
#     return inner
# =======


@pytest_asyncio.fixture(scope="session", autouse=True)
async def es_fill_indexes():
    """
    Asynchronously create and fill Elasticsearch indices for testing.

    This fixture runs automatically before the test session and
    - Creates an Elasticsearch client
    - Checks if the index exists; if so, deletes it
    - Creates a new index with settings and mappings
    - Fills the index with data
    - Refreshes all indices

    Yields:
        client: The Elasticsearch client.
    """


    logger.info("Create elasticsearch client.")

    async with AsyncElasticsearch(hosts=[test_settings.es_host]) as client:
        for index_name in test_settings.es_indexes:
            if await client.indices.exists(index=index_name):
                await client.indices.delete(index=index_name)
            logger.info(f"Create {index_name} index.")
            await client.indices.create(index=index_name,
                                        settings=es_mapping.index[index_name]['settings'],
                                        mappings=es_mapping.index[index_name]['mappings'])

        for index_name in test_settings.es_indexes:
            logger.info(f"Fill {index_name} index.")
            actions = [
                {
                    "_index": index_name,
                    "_id": doc.get("uuid", None),
                    "_source": doc
                }
                for doc in es_mapping.data[index_name]
            ]
            await async_bulk(client, actions)

        await client.indices.refresh(index="_all")
        for index_name in test_settings.es_indexes:
            await client.cluster.health(index=index_name, wait_for_status='yellow')

        yield client
        for index in test_settings.es_indexes:
            logger.info(f"Clear {index_name} index.")
            await client.options(ignore_status=[400, 404]).indices.delete(index=index)


@pytest.fixture(scope="session")
def event_loop():
    """
    Create and yield a new event loop for the test session.

    :yield: aiohttp client session.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session')
async def http_session():
    """
    Asynchronously create and yield an aiohttp client session for the test session.

    Yields:
        session: The aiohttp client session.
    """
    async with aiohttp.ClientSession() as session:
        yield session


@pytest_asyncio.fixture
async def make_get_request(http_session):
    """
    Asynchronously make a GET request using the aiohttp client session.

    :param http_session: aiohttp client session.
    :return: A function that takes a URL path and query data, performs a GET request,
             and returns the response object augmented with the response time and body.
    """
    async def inner(path: str, query_data: dict | None = None):
        url = f'{test_settings.service_url}{path}'
        start = time.time()
        async with http_session.get(url, params=query_data) as response:
            response.body = await response.json()
            response.response_time = time.time() - start
            return response
    return inner
# >>>>>>> origin/feature/tests_films
