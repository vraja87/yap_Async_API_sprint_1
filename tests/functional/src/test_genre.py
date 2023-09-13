import pytest
from functional.testdata.es_mapping import our_genres


@pytest.mark.asyncio
@pytest.mark.fixt_data(es_index='genres', es_id_field='uuid')
@pytest.mark.parametrize(
    'query_data, expected_answer',
    [
        (
            {},
            {'status': 200, 'length': 30}
        ),
        (
            {'page_number': 0},
            {'status': 200, 'length': 30}  # start page 0
        ),
        (
            {'page_number': 1},  # TODO hz why 404 and not bad request
            {'status': 404, 'length': 1}
        ),
        (
            {'page_number': -1},  # incorrect
            {'status': 422, 'length': 1}
        ),
        (
            {'page_number': 100},  # too big
            {'status': 400, 'length': 1}
        ),
        (
            {'page_number': 'Mashed potato'},  # not int
            {'status': 422, 'length': 1}
        ),
        (
            {'page_size': 10},
            {'status': 200, 'length': 10}
        ),
        (
            {'page_size': 20},
            {'status': 200, 'length': 20}
        ),
        (
            {'page_size': 0},
            {'status': 422, 'length': 1}
        ),
        (
            {'page_size': -1},
            {'status': 422, 'length': 1}
        ),
        (
            {'page_size': 5000},
            {'status': 200, 'length': 30}
        ),
    ]
)
async def test_all_genres_page_num_size(
        make_get_request, es_write_data_OLD,
        query_data: dict, expected_answer: dict
):
    """Test different page_size and page_number combinations"""

    await es_write_data_OLD(our_genres)
    body, headers, status = await make_get_request(
        f'/api/v1/genres/', query_data
    )

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']


@pytest.mark.asyncio
@pytest.mark.fixt_data(es_index='genres', es_id_field='uuid')
@pytest.mark.parametrize(
    'query_data, expected_answer',
    [
        (
            {'page_number': 2, 'page_size': 10},
            {'status': 200, 'length': 10}
        ),
    ]
)
async def test_all_genres_format_sorting_consistency(
        make_get_request, es_write_data_OLD,
        query_data: dict, expected_answer: dict
):
    """Test data consistency on some page, genre format, sorting by names"""
    await es_write_data_OLD(our_genres)
    body, headers, status = await make_get_request(f'/api/v1/genres/',
                                                   query_data)

    genres_slice = sorted(our_genres, key=lambda x: x['name'])[
                   query_data['page_number'] * query_data['page_size']:]

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']
    assert genres_slice == body
    assert body[0]['name'] < body[1]['name']


@pytest.mark.asyncio
@pytest.mark.fixt_data(es_index='genres', es_id_field='uuid')
@pytest.mark.parametrize(
    'test_data, expected_answer',
    [
        (
            {'uuid': 'e5780277-9d62-4540-98e6-e7abeba51557'},
            {'body': our_genres[4],
             'status': 200}
        ),
        (
            {'uuid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
            {'body': {'detail': 'Genre not found.'},
             'status': 404}
        ),
    ]
)
async def test_genre_details(
        es_write_data_OLD, make_get_request,
        test_data, expected_answer
):
    await es_write_data_OLD(our_genres)
    body, headers, status = await make_get_request(
        f'/api/v1/genres/{test_data["uuid"]}', None
    )

    assert status == expected_answer['status']
    assert body == expected_answer['body']
