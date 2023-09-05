from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    es_host: str = Field('http://127.0.0.1:9200', env='ELASTIC_HOST')
    es_index: str = 'movies'  # TODO ? movies genres persons
    es_id_field: str = ''  # TODO need to fill
    es_index_mapping: dict = ''  # TODO need to fill

    redis_host: str = Field('redis', env='REDIS_HOST')
    service_url: str = ''  # TODO need to fill

test_settings = TestSettings()
