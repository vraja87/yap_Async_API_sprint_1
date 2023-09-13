import uuid

es_search_films = [
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
        "description":
            "Consider forget reason. Research star well become shoulder discuss may none. Conference most organization improve cost hold member.",
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
    } for _ in range(120)
]

our_genres = [
    {
        'uuid': '9389cf56-319d-4b16-a336-010f2b335ded',
        'name': 'News'
    },
    {
        'uuid': '834cf2fe-c799-41d5-97ff-f4f2fc795292',
        'name': 'Disaster'
    },
    {
        'uuid': 'dba62587-07b0-4ba2-92ab-52354c0fff62',
        'name': 'Post-Apocalyptic'
    },
    {
        'uuid': '38db730a-b3c1-478b-9bc3-78ed2795d944',
        'name': 'Legal'
    },
    {
        'uuid': 'e5780277-9d62-4540-98e6-e7abeba51557',
        'name': 'Psychological'
    },
    {
        'uuid': '3166c9b5-00d7-42e3-a56b-4cc7a9386a39',
        'name': 'Road Movie'
    },
    {
        'uuid': '859c166a-e9b9-4080-b457-a4aaace57981',
        'name': 'Supernatural'
    },
    {
        'uuid': 'e3d8dd3a-5c84-4fc9-bbd5-a91288ef7833',
        'name': 'Experimental'
    },
    {
        'uuid': '5e5b0cfc-4435-4c64-ba4c-8bb4d19c241d',
        'name': 'Urban'
    },
    {
        'uuid': 'b9e1a295-b0fd-4e2d-a938-711393329f4e',
        'name': 'Art House'
    },
    {
        'uuid': '705c68ed-2927-45d9-a211-abf85b99b782',
        'name': 'Action'
    },
    {
        'uuid': 'f0766697-0ff1-42a6-a21a-3e44ed1937d4',
        'name': 'Author Cinema'
    },
    {
        'uuid': 'c609758e-b25b-42e6-b197-83fadd7cb7c1',
        'name': 'Romance'
    },
    {
        'uuid': 'f9621029-7087-4439-9ce4-837c8e9a584b',
        'name': 'Horror'
    },
    {
        'uuid': '40559f06-2d76-4197-be4c-3a83a686a23a',
        'name': 'Superhero'
    },
    {
        'uuid': 'a3002921-be37-4b59-90d5-b2f051579c6c',
        'name': 'Time Travel'
    },
    {
        'uuid': '4ccd952c-c38e-4138-b727-a3668e3fff05',
        'name': 'Family'
    },
    {
        'uuid': 'ee32f9dc-7904-45eb-a48a-e70ad975dfea',
        'name': 'Thriller'
    },
    {
        'uuid': '14c1c22d-751a-4576-afaa-e981cbe2def7',
        'name': 'Cyberpunk'
    },
    {
        'uuid': '8a4b39d3-21f1-45a9-95d7-83ded97ecd76',
        'name': 'Teen'
    },
    {
        'uuid': '4776e4f4-99c0-4f22-900b-064de1fb27c4',
        'name': 'Sport'
    },
    {
        'uuid': 'f94b4fab-1cb2-4e36-ad2c-28121e5592a3',
        'name': 'Epic'
    },
    {
        'uuid': 'e0fbd409-7cf5-457d-89fb-6f8df2ba5586',
        'name': 'Animation'
    },
    {
        'uuid': '851b1020-448d-40c7-9a21-df967615fdec',
        'name': 'Drama'
    },
    {
        'uuid': '3969f82d-7591-40c7-909f-54f19f8b26a4',
        'name': 'Crime'
    },
    {
        'uuid': '3b23eff3-0a6b-4a48-9f47-12dffa6c482c',
        'name': 'War'
    },
    {
        'uuid': '24fbbf80-5181-49a4-8381-c05fab3725d5',
        'name': 'Adventure'
    },
    {
        'uuid': '62e91d2c-5015-49ec-a43f-364114b80270',
        'name': 'Historical'
    },
    {
        'uuid': '8376d697-886f-4d44-93d7-8e1dc821aff9',
        'name': 'Short Film'
    },
    {
        'uuid': '447586f7-cab9-4a28-9f0c-777b5ab943b5',
        'name': 'Science Fiction'
    }
]

our_persons = [
    {
        "uuid": "b7d1b5e1-b56a-454e-8ab9-8babde567662",
        "full_name": "Stephanie Cohen",
        "films": [
            "abf26b0e-e5a5-43f8-8b08-c8e6fc6c8393",
            "bc833b52-6d24-47b7-bc5d-8fbbade3f438",
            "9aef0e42-a8e1-48bd-9a13-8948609cd292",
            "69f1643b-a52a-4516-b5a5-374e8d2567f6",
            "cd05b7c7-db43-4616-a706-fd0f77feec3e",
            "88867511-f2ea-4008-9c74-5822e46c78a5",
            "c000321a-1229-4a4c-8bef-43e9a364cfe1",
            "a7c1f68d-939b-48a6-b401-32133715a57a",
            "395b379c-1b07-43b0-ad67-0049abd07587",
            "a7e1ac1e-00af-442a-8d95-39f43b2b4a80",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "ec474cce-521d-42a1-936f-4a76909653c3",
        "full_name": "Tracy Wilkerson",
        "films": [
            "012de269-ef41-44c5-8485-0be33914a234",
            "7bfba9ca-9396-442f-95b1-dbf6e71362e3",
            "9aef0e42-a8e1-48bd-9a13-8948609cd292",
            "7ede7015-62b5-4a63-b1fa-86b4d7201d08",
            "550fae59-3034-4ee9-bea7-ce4562856465",
            "c3af9639-8786-4be5-9e1f-f10d86df5f12",
            "83cfe03f-209a-4f29-8c44-3128c0069a86",
            "9e7dcbe7-c186-4cc1-9ecb-5b3b79551601",
            "64e76a5a-b0c3-48c5-a3f5-a419aee6b3b3",
            "395b379c-1b07-43b0-ad67-0049abd07587",
            "67bd2909-96a3-48ed-b6a0-37f79adf4075",
            "2dbeacc1-331d-4ffd-b966-87c52865b705",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "ff460f85-9ee2-4073-87df-77a87e03f06a",
        "full_name": "Laurie Goodwin",
        "films": [
            "f83b6ac0-432d-4b0d-882c-19ac44fb93f6",
            "9b77ab86-c00c-4ad3-bcc9-44f03afaee7f",
            "52353bbc-4cca-4f97-9e97-e6657f6f7b4a",
            "653dedcc-9165-46fa-9a0c-a2b35d60723b",
            "deeec627-48c8-49c8-ac85-0507e923fc0d",
            "af991650-d0d5-47e2-ab3d-ee12470abc0b",
            "8e1fed52-a701-490f-a1d2-d261281a814e",
            "dc82c154-1f9b-4521-8138-ee2d9e8d9acf",
            "8f414165-7d4b-4ea1-b763-0f2cf0d7d561",
            "60c74863-30a0-46eb-8e25-3791f826e7a0",
            "2a7fc9a1-688e-4fa2-8b05-02eee7515018",
            "0f7c58a1-0ec5-4a07-925e-db9bbfa2d777",
            "75d2c529-9967-49fd-865e-20c55115f1b1",
            "a5fe0cba-3781-430d-b9d0-832c3a698c04",
            "02f71560-00c7-4fc5-8e8a-d40f19c8ec10",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "bf35cd52-4eca-4207-90e7-26044e0682d4",
        "full_name": "Donald Stevenson",
        "films": [
            "034be1e4-f9ca-4883-ace4-baf665b0bac6",
            "bad392e6-9058-47ab-9cac-486badd22604",
            "554a2b20-5439-4087-8908-6cd1369ee47f",
            "1c730f37-017f-47a3-bff5-55f5e9d6428f",
            "0d28e98c-5917-421a-9cd1-9e38da5cfdfd",
            "c599f894-c016-4ef0-a490-70dfb5528581",
            "a45bcf73-4410-4c1c-ad6b-81d3d0c05ceb",
            "61af74b8-9273-4a68-9a8b-1b964055847e",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "25a26130-6dbb-409c-ae4f-72a98c5e8bfc",
        "full_name": "Michael Stewart",
        "films": [
            "5760f86c-0466-45ae-92cd-c3354ef03157",
            "328df999-a8da-4ad9-abae-7d0459cdcea4",
            "1376f093-40b0-494c-b92a-1c301788af3a",
            "e41a615a-9e13-45f7-9db0-a069f965f594",
            "fb5f28f9-5ae0-4e43-befd-8368ed8673a3",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba",
            "10002a37-c882-4aab-a69a-506adef92f7d",
            "615e5be5-89d1-40d5-872f-b069fc538ef0",
            "7b88fa3c-f951-4589-8e2f-32911189fd90",
            "7149e15d-6ed1-4ca7-910d-da1498fa5905",
            "a7e1ac1e-00af-442a-8d95-39f43b2b4a80",
            "147c09fd-afa6-4fa1-9256-b66bba76ebee"
        ]
    },
    {
        "uuid": "65c3c7ff-276e-4109-9739-97de00f50bc2",
        "full_name": "Yesenia Mcdonald",
        "films": [
            "8dfb6f42-7210-4e3e-a613-13cae59c4a67",
            "3cc1f42d-b7ee-4711-bd6d-34ec2282acb7",
            "0f996a5b-91fa-49f4-a12b-98271e3dadcd",
            "7a9f3780-a2c5-4e4a-9c15-9d1cdfb2d4c6",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "4edbde73-5955-47d0-a0e1-efd898192f26",
        "full_name": "Leslie Key",
        "films": [
            "1308152e-0bb1-4272-906f-099c4defe60d",
            "3c7e21db-a528-419b-b62f-bae8798f5f5d",
            "ed7d426e-0142-46b9-b58a-1d904c0c2e61",
            "621fc0b7-7298-4827-b845-e4838b52ce95",
            "e212d73a-b9ca-470e-b352-bbe72d9aeb7b",
            "252490f0-3776-4948-a886-8c755dec1300",
            "aa53c593-1b7c-4682-b48d-1c274db61c70",
            "9dca4cfc-2fc4-4c9a-92ec-c04a97897ad4",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba",
            "d38ddb31-4808-43a8-a36e-ac566775285b",
            "be2d7a63-0f6f-4f99-aa52-7d4381bca2fd",
            "d972c5b4-df07-4bb5-acc2-7c75e8baf15c"
        ]
    },
    {
        "uuid": "2d59a52f-7d06-4ceb-975e-ccf3fe124533",
        "full_name": "Kevin Murphy",
        "films": [
            "313b6fa4-9002-4d7d-83ac-12048ec10eaa",
            "b8797694-e267-47fb-9b96-927c1621b1bb",
            "7604a761-0956-4c06-981b-d1d88a7385b5",
            "38c81188-e859-4cee-99f8-95806e091d08",
            "14a69510-69f2-4898-b71d-f2e377a85135",
            "8dfb6f42-7210-4e3e-a613-13cae59c4a67",
            "c9aaada6-1a72-47fb-955a-046e354d18e0",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba",
            "67db156a-699a-487e-84b3-13bd8741dc45",
            "3448984e-c369-4d2d-ac58-dd1538fc4759",
            "4bafb47e-1cfa-4fd3-91ae-176ce61b7ea6",
            "56693e7f-116d-4829-b426-027247bb3796",
            "a5fe0cba-3781-430d-b9d0-832c3a698c04",
            "b5874a53-9661-4ff1-9bb7-5f91d8c17f23",
            "2c05d6d5-e17b-4476-8c91-f9ba8c32ac40"
        ]
    },
    {
        "uuid": "726665da-d602-4c01-96d3-71e4c54f4dd5",
        "full_name": "Eric Cruz",
        "films": [
            "49a17c5c-770c-4f98-825e-e5ae20ca1c2d",
            "034be1e4-f9ca-4883-ace4-baf665b0bac6",
            "9152b0d2-a04a-4ac5-b673-d85038a97593",
            "41be21a4-ec51-4685-8111-ef9ebdb148a9",
            "653dedcc-9165-46fa-9a0c-a2b35d60723b",
            "76b071e2-34cb-4e71-81ea-689ab6383a62",
            "c3af9639-8786-4be5-9e1f-f10d86df5f12",
            "90dcf794-cf8d-4d53-9a20-7f72ce3a5496",
            "5a9971fd-5119-4d8e-adf5-38fb4e1ff32e",
            "51f9e27b-e6fe-4c32-bfc3-de749a7284f1",
            "2ec6cc68-d860-40d8-99ad-552b7e27790d",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    },
    {
        "uuid": "86121aed-e760-4adc-9047-e2ff77430f04",
        "full_name": "Jeff Davidson",
        "films": [
            "7ede7015-62b5-4a63-b1fa-86b4d7201d08",
            "1082937f-3b56-4823-b994-325304a5e265",
            "47853b2a-ef5f-43f8-9c3b-33ca7c4a7032",
            "05eec260-57b6-4455-b8e6-8c232afd384e",
            "c7328761-6853-4577-88a6-8c934ce0d4fc",
            "cdc8e7ad-f2ca-46d7-a6a5-67abe8fc709c",
            "7075852b-c23d-46a2-be1a-c57414abe9c9",
            "4e3bf853-3b65-4d50-87ed-b761f4745306",
            "01098f7c-ac2d-4fdc-b771-b7522e0b8bba"
        ]
    }
]
