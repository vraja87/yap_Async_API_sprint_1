import pytest
from functional.testdata.es_mapping import es_search_films

@pytest.mark.asyncio
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
@pytest.mark.fixt_data(es_index='movies', es_id_field='uuid')
async def test_search(
        es_write_data_OLD, es_write_data, make_get_request,
        query_data, expected_answer
):
    await es_write_data_OLD(es_search_films)  # TODO why its work?
    # es_write_data(es_data)   # TODO ...and this DO NOT work?

    body, headers, status = await make_get_request(
        '/api/v1/films/search/', query_data
    )

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']
