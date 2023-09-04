from functools import lru_cache

from db.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from models.person import Person
from services.base import BaseService

from fastapi import Depends


class PersonService(BaseService):
    """
    Service class to handle operations related to persons.

    :param elastic: The Elasticsearch client.
    """
    index = 'persons'
    model = Person
    search_fields = ['full_name']


@lru_cache()
def get_person_service(elastic: AsyncElasticsearch = Depends(get_elastic)) -> PersonService:
    """
    Dependency function to get an instance of PersonService.

    :param elastic: The Elasticsearch client.
    :return: An instance of PersonService.
    """
    return PersonService(elastic)
