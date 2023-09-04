import os

from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = '.env' if os.path.exists('.env') else None


class RedisConf(BaseSettings):
    """
    Configuration settings for Redis.

    :param host: The Redis host address.
    :param port: The Redis port.
    :param cache_expire_in_second: Default cache expiration time in seconds.
    :param cache_expire_low_in_second: Low-priority cache expiration time in seconds.
    """

    model_config = SettingsConfigDict(env_file=env_file, env_prefix='REDIS_')

    host: str = 'redis'
    port: int = 6379
    cache_expire_in_second: int = 180
    cache_expire_low_in_second: int = 30


class ElasticConf(BaseSettings):
    """
    Configuration settings for Elasticsearch.

    :param host: The Elasticsearch host address.
    :param port: The Elasticsearch port.
    """
    model_config = SettingsConfigDict(env_file=env_file, env_prefix='ELASTIC_')

    host: str = 'elasticsearch'
    port: int = 9200


class FastApiConf(BaseSettings):
    """
    Configuration settings for the FastAPI application.

    :param name: The name of the FastAPI application.
    """
    model_config = SettingsConfigDict(env_file=env_file, env_prefix='PROJECT_')

    name: str = 'movies'
