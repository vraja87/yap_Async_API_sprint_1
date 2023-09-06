from api.v1 import films, genres, persons
from core import config
from core.logger import logger
from db import cache, elastic
from db.cache import CacheBackendFactory, CacheClientInitializer
from elasticsearch import AsyncElasticsearch

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

fast_api_conf = config.FastApiConf()

app = FastAPI(
    title=fast_api_conf.name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    """
    Initialize resources when the FastAPI application starts.

    Connects to Redis and Elasticsearch databases.
    """
    cache_conf = config.CacheConf.read_config()
    elastic_conf = config.ElasticConf()
    logger.info('Startup api service.')
    cache.cache = await CacheBackendFactory.create_backend(cache_conf.backend_type, **cache_conf.get_init_params())
    elastic.es = AsyncElasticsearch(hosts=[f'http://{elastic_conf.host}:{elastic_conf.port}'])


@app.on_event('shutdown')
async def shutdown():
    """
    Release resources when the FastAPI application stops.

    Closes connections to Redis and Elasticsearch databases.
    """
    cache_conf = config.CacheConf.read_config()
    logger.info('Shutdown api service.')
    await CacheClientInitializer.close_client(cache_conf.backend_type, cache.cache.client)
    await elastic.es.close()


app.include_router(films.router, prefix='/api/v1/films', tags=['films'])
app.include_router(genres.router, prefix='/api/v1/genres', tags=['genres'])
app.include_router(persons.router, prefix='/api/v1/persons', tags=['persons'])
