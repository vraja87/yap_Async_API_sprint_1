import datetime
import uuid
import pytest


@pytest.mark.parametrize(
    'query_data, expected_answer',
    [
        (
                {'query': 'Right-sized'},
                {'status': 200, 'length': 60}  # TODO they think that 50 entries will be returned.
        ),
        (
                {'query': 'Mashed potato'},
                {'status': 200, 'length': 0}  # TODO they think that wrong search it is 200 and maybe empty list. we have 404
        )
    ]
)
@pytest.mark.asyncio
async def test_search(es_write_data_OLD, es_write_data, make_get_request, query_data, expected_answer):
    # 1. Генерируем данные для ES

    es_data = [{
        'id': str(uuid.uuid4()),
        'imdb_rating': 8.5,
        'genre': ['Action', 'Sci-Fi'],
        'title': 'The Star',
        'description': 'New World',
        'director': ['Stan'],
        'actors_names': ['Ann', 'Bob'],
        'writers_names': ['Ben', 'Howard'],
        'actors': [
            {'id': '111', 'name': 'Ann'},
            {'id': '222', 'name': 'Bob'}
        ],
        'writers': [
            {'id': '333', 'name': 'Ben'},
            {'id': '444', 'name': 'Howard'}
        ],
        'created_at': datetime.datetime.now().isoformat(),
        'updated_at': datetime.datetime.now().isoformat(),
        'film_work_type': 'movie'
    } for _ in range(60)]

    es_data = [
        {
            "uuid": str(uuid.uuid4()),
            "imdb_rating": 5.749010583956972,
            "title": "Right-sized user-facing moderator",
            "genre": [
                "Urban",
                "Epic",
                "Sport",
                "Cyberpunk",
                "Disaster"
            ],
            "genre_full": [
                {
                    "uuid": "f94b4fab-1cb2-4e36-ad2c-28121e5592a3",
                    "name": "Epic"
                },
                {
                    "uuid": "4776e4f4-99c0-4f22-900b-064de1fb27c4",
                    "name": "Sport"
                },
                {
                    "uuid": "14c1c22d-751a-4576-afaa-e981cbe2def7",
                    "name": "Cyberpunk"
                },
                {
                    "uuid": "5e5b0cfc-4435-4c64-ba4c-8bb4d19c241d",
                    "name": "Urban"
                },
                {
                    "uuid": "834cf2fe-c799-41d5-97ff-f4f2fc795292",
                    "name": "Disaster"
                }
            ],
            "description": "Consider forget reason. Research star well become shoulder discuss may none. Conference most organization improve cost hold member.",
            "directors_names": [
                "Brianna Arias",
                "David Rodriguez",
                "James Raymond",
                "Eric Carter",
                "Christopher Shaw",
                "Nathan David",
                "Michelle Gonzalez",
                "Alexander Greene"
            ],
            "actors_names": [
                "Douglas Gibbs",
                "Bonnie Tran",
                "Eileen Franklin",
                "Angela Woodward",
                "Thomas Levy"
            ],
            "writers_names": [],
            "actors": [
                {
                    "uuid": "a559e4e7-e310-4084-97fe-b192ebf05805",
                    "name": "Douglas Gibbs"
                },
                {
                    "uuid": "7ae5f422-3a3e-42c0-aa78-a9db44baa24d",
                    "name": "Bonnie Tran"
                },
                {
                    "uuid": "8cc4a99a-f0e5-47b8-8dfc-e63ab1f2a6c4",
                    "name": "Eileen Franklin"
                },
                {
                    "uuid": "3bf53b0b-12ad-4bb3-8f68-823bdbb24aad",
                    "name": "Angela Woodward"
                },
                {
                    "uuid": "52dd70c9-6747-42bd-9c40-564035d7775b",
                    "name": "Thomas Levy"
                }
            ],
            "writers": [],
            "directors": [
                {
                    "uuid": "ea7b0281-8d5b-4dbe-b24a-0e53d07e555d",
                    "name": "Brianna Arias"
                },
                {
                    "uuid": "685b65a5-e96d-4056-bdb6-a20fd62a3f61",
                    "name": "David Rodriguez"
                },
                {
                    "uuid": "54b4c5d2-df3e-457a-aea4-b0be72d4073b",
                    "name": "James Raymond"
                },
                {
                    "uuid": "41423bb4-1929-4f47-9b3c-84ce3f53abd4",
                    "name": "Eric Carter"
                },
                {
                    "uuid": "5287c0c3-0e8d-4da4-ad42-d47a6d0485d4",
                    "name": "Christopher Shaw"
                },
                {
                    "uuid": "e5880422-a51e-4d88-a808-4dac8efcde74",
                    "name": "Nathan David"
                },
                {
                    "uuid": "c48a02f3-273e-48e0-8b4c-329dc484e8ae",
                    "name": "Michelle Gonzalez"
                },
                {
                    "uuid": "40c31640-67aa-44ab-a5d4-246cda8cf106",
                    "name": "Alexander Greene"
                }
            ]
        } for _ in range(60)
    ]

    await es_write_data_OLD(es_data)  # TODO why its work?
    # es_write_data(es_data)   # TODO why its NOT work?

    body, headers, status = await make_get_request('/api/v1/films/search/', query_data)

    assert status == expected_answer['status']
    assert len(body) == expected_answer['length']
