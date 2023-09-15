from pprint import pprint

import pytest
from functional.testdata.es_mapping import our_persons, our_persons_films

@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_data, expected_answer',
    [
        (
            {'uuid': '4c450994-07d5-4e80-b16e-50c1d0f64eac'},
            {'body': {'films': [{'roles': ['writer'],
                                 'uuid': 'b2fd87a8-b8be-4d75-af99-274e164bfae9'},
                                {'roles': ['director'],
                                 'uuid': '5a7895f7-83af-4453-9457-83b3d224da99'},
                                {'roles': ['director'],
                                 'uuid': '35c15cf0-6e2b-431f-acdb-1cdd47e8a485'},
                                {'roles': ['writer'],
                                 'uuid': '527980a9-f350-4707-9790-d561d814d4a8'},
                                {'roles': ['director'],
                                 'uuid': 'ef0c5e93-5f9d-4097-9535-c4febb73d8c3'}],
                      'full_name': 'Christopher Jones',
                      'uuid': '4c450994-07d5-4e80-b16e-50c1d0f64eac'},
             'status': 200}
        ),
        (
            {'uuid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
            {'body': {'detail': 'person not found'},
             'status': 404}
        ),
        (
            {'uuid': 'xxxxxxxx'},
            {'body': {'detail': 'person not found'},
             'status': 404}
        ),
        (
            {'uuid': 327},  # TODO лишние тесты
            {'body': {'detail': 'person not found'},
             'status': 404}
        ),
    ]
)
async def test_person_details(
        es_write_movies, es_write_persons, make_get_request,
        test_data, expected_answer
):
    await es_write_movies(our_persons_films)
    await es_write_persons(our_persons)
    body, headers, status = await make_get_request(
        f'/api/v1/persons/{test_data["uuid"]}', None
    )

    assert status == expected_answer['status']
    assert body == expected_answer['body']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_data, expected_answer',
    [
        (
            {'uuid': '4c450994-07d5-4e80-b16e-50c1d0f64eac'},
            {'body': [{'imdb_rating': 8.052032866140571,
                       'title': 'Self-enabling foreground process improvement',
                       'uuid': 'b2fd87a8-b8be-4d75-af99-274e164bfae9'},
                      {'imdb_rating': 8.869885471371546,
                       'title': 'Automated bottom-line task-force',
                       'uuid': '5a7895f7-83af-4453-9457-83b3d224da99'},
                      {'imdb_rating': 0.9063096647574986,
                       'title': 'Proactive reciprocal middleware',
                       'uuid': '35c15cf0-6e2b-431f-acdb-1cdd47e8a485'},
                      {'imdb_rating': 4.870828934768973,
                       'title': 'Multi-lateral homogeneous protocol',
                       'uuid': '527980a9-f350-4707-9790-d561d814d4a8'},
                      {'imdb_rating': 5.586249000823028,
                       'title': 'Switchable maximized contingency',
                       'uuid': 'ef0c5e93-5f9d-4097-9535-c4febb73d8c3'}],
             'status': 200}
        ),
        (
            {'uuid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
            {'body': {'detail': 'person not found'},
             'status': 404}
        ),
        (
            {'uuid': "e100288b-ba2c-42af-b988-d42089363355"},  # exist person has no films
            {'body': {'detail': 'films with person were not found'},
             'status': 404}
        ),
        (
            {'uuid': 327},
            {'body': {'detail': 'person not found'},
             'status': 404}
        ),
    ]
)
async def test_person_films(
        es_write_movies, es_write_persons, make_get_request,
        test_data, expected_answer
):
    await es_write_movies(our_persons_films)
    await es_write_persons(our_persons)
    body, headers, status = await make_get_request(
        f'/api/v1/persons/{test_data["uuid"]}/film', None
    )
    assert status == expected_answer['status']
    assert body == expected_answer['body']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_data, expected_answer',
    [
        (
            {'query': 'Christopher Jones',  # exact answer
             'fuzziness': 0,
             'page_number': 0,
             'page_size': 1},
            {'body': [{'full_name': 'Christopher Jones',
                       'uuid': '4c450994-07d5-4e80-b16e-50c1d0f64eac',
                       'films': [{'roles': ['writer'],
                                  'uuid': 'b2fd87a8-b8be-4d75-af99-274e164bfae9'},
                                 {'roles': ['director'],
                                  'uuid': '5a7895f7-83af-4453-9457-83b3d224da99'},
                                 {'roles': ['director'],
                                  'uuid': '35c15cf0-6e2b-431f-acdb-1cdd47e8a485'},
                                 {'roles': ['writer'],
                                  'uuid': '527980a9-f350-4707-9790-d561d814d4a8'},
                                 {'roles': ['director'],
                                  'uuid': 'ef0c5e93-5f9d-4097-9535-c4febb73d8c3'}]
                       }],
             'status': 200}
        ),
        (
            # exact answer. second of two persons. if 'page_number', 'page_size' are working correctly
            {'query': 'Christopher Jones',
             'fuzziness': 0,
             'page_number': 1,
             'page_size': 1},
            {'body': [{'full_name': 'Brian Jones',
                       'uuid': '5e80ed50-e3af-463d-a6e1-1f39a8d4168a',
                       'films': [{'roles': ['writer'],
                                  'uuid': '5a7895f7-83af-4453-9457-83b3d224da99'},
                                 {'roles': ['writer'],
                                  'uuid': '28af29e3-099f-49fb-a5b7-f9e9d7ad461f'},
                                 {'roles': ['director'],
                                  'uuid': 'be6585ff-97f9-4091-9730-1574f0567fbb'}],
                       }],
             'status': 200}
        ),
        (
            {'query': '',  # empty
             'fuzziness': 0,
             'page_number': 0,
             'page_size': 10},
            {'body': {'detail': 'persons not found'},
             'status': 404}
        ),
        (
            {'query': ' ',  # space
             'fuzziness': 0,
             'page_number': 0,
             'page_size': 10},
            {'body': {'detail': 'persons not found'},
             'status': 404}
        ),
        (
            {'query': 'Stephen Hawking',  # no one
             'fuzziness': 3,
             'page_number': 0,
             'page_size': 10},
            {'body': {'detail': 'persons not found'},
             'status': 404}
        ),
        # fuzinness tests are useless for persons
    ]
)
async def test_persons_search(
        es_write_movies, es_write_persons, make_get_request,
        test_data, expected_answer
):
    await es_write_movies(our_persons_films)
    await es_write_persons(our_persons)
    body, headers, status = await make_get_request(
        f'/api/v1/persons/search/', test_data
    )

    assert status == expected_answer['status']
    assert body == expected_answer['body']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_data, expected_answer',
    [
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 0,
             'page_size': 10},
            {'length': 2,
             'status': 200}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 1,
             'page_size': 10},
            {'length': 1,
             'status': 404}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': -1,
             'page_size': 10},
            {'length': 1,
             'status': 422}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 100,
             'page_size': 10},
            {'length': 1,
             'status': 404}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 0,
             'page_size': 0},
            {'length': 1,
             'status': 422}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 0,
             'page_size': -1},
            {'length': 1,
             'status': 422}
        ),
        (
            {'query': 'Jones',
             'fuzziness': 3,
             'page_number': 0,
             'page_size': 1000},
            {'length': 2,
             'status': 200}
        ),
    ]
)
async def test_persons_page_num_size(
        es_write_movies, es_write_persons, make_get_request,
        test_data, expected_answer
):
    await es_write_movies(our_persons_films)
    await es_write_persons(our_persons)
    body, headers, status = await make_get_request(
        f'/api/v1/persons/search/', test_data
    )
    # print('body, headers, status')
    # pprint((body, headers, status))

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']
