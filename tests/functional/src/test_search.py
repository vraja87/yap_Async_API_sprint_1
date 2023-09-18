import pytest

from functional.settings import test_settings
from functional.testdata.es_mapping import es_search_films, our_persons_films


@pytest.mark.asyncio
@pytest.mark.fixt_data(es_index='movies', es_id_field='uuid')
@pytest.mark.parametrize(
    'query_data, expected_answer',
    [
        (
                {'query': 'Right-sized'},
                {'status': 200, 'length': 100}
        ),
        (
                {'query': 'Mashed potato'},
                {'status': 404, 'length': 1}
        )
    ]
)
async def test_search(
        es_write_data_OLD, es_write, make_get_request,
        redis_cleanup, es_del_idx,
        query_data, expected_answer
):
    await es_write_data_OLD(es_search_films)
    # await es_write(test_settings.es_index_movies, es_search_films)  # TODO refactor

    body, headers, status = await make_get_request(
        '/api/v1/films/search/', query_data
    )

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']
    await redis_cleanup()
    await es_del_idx(test_settings.es_index_movies)
