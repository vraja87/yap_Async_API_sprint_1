import os

from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = '.env' if os.path.exists('.env') else None


class TestSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_prefix='TESTS_')

    es_host: str = 'http://elasticsearch:9200'
    redis_host: str = 'redis://redis:6379'
    es_index_movies: str = 'movies'
    es_index_persons: str = 'persons'
    es_index_genres: str = 'genres'
    es_id_field: str = 'uuid'
    # es_index_mapping: dict = ''  # TODO need to fill
    service_url: str = 'http://fastapi:8000'


test_settings = TestSettings()
