from functools import lru_cache

from db.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from models.genre import Genre
from services.base import BaseService

from fastapi import Depends


class GenreService(BaseService):
    """
    Service class to handle operations related to genres.

    :param elastic: The Elasticsearch client.
    """
    index = 'genres'
    model = Genre


@lru_cache()
def get_genre_service(elastic: AsyncElasticsearch = Depends(get_elastic)) -> GenreService:
    """
    Dependency function to get an instance of GenreService.

    :param elastic: The Elasticsearch client.
    :return: An instance of GenreService.
    """
    return GenreService(elastic)
