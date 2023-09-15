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
    "uuid": "3aa862e6-08dc-40c2-a787-b41975946aac",
    "name": "Nature"
  },
  {
    "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
    "name": "Comedy"
  },
  {
    "uuid": "9cf532d7-b26f-4019-a193-39cdeca0adc6",
    "name": "Historical"
  },
  {
    "uuid": "14bb19ce-b2cc-4d15-9387-65bfb7e5d8f2",
    "name": "Detective"
  },
  {
    "uuid": "9a46b816-5f1c-4306-bc4f-13d2a006f373",
    "name": "Vampire"
  },
  {
    "uuid": "c8e571f4-b32a-4698-8190-31610d71a04c",
    "name": "Zombie"
  },
  {
    "uuid": "5e073c6d-4565-4637-8f58-b3d325437e64",
    "name": "Documentary"
  },
  {
    "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
    "name": "Crime"
  },
  {
    "uuid": "1702ef39-6a5d-4ef4-b807-da5a8b9c6c68",
    "name": "Biography"
  },
  {
    "uuid": "90c8fe15-4593-4174-9678-02cb28bd2c86",
    "name": "Family"
  },
  {
    "uuid": "2381485b-ba4b-4a4f-94db-95cae5c250b4",
    "name": "Cyberpunk"
  },
  {
    "uuid": "6679a19e-3c93-4257-a76e-44e2316ae60a",
    "name": "Epic"
  },
  {
    "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
    "name": "Science Fiction"
  },
  {
    "uuid": "036eef26-c456-41f8-9222-71da54a3c9f6",
    "name": "Supernatural"
  },
  {
    "uuid": "e7efd97f-4300-4c06-8257-0892bb04bf13",
    "name": "Psychological"
  },
  {
    "uuid": "707baf13-2a31-423a-8564-584fae5783f7",
    "name": "Legal"
  },
  {
    "uuid": "cac1d46e-0ff3-41fd-a4aa-f68d184b7f6e",
    "name": "Thriller"
  },
  {
    "uuid": "3ea514ef-0bc5-4918-beac-9452eef30452",
    "name": "Short Film"
  },
  {
    "uuid": "11ebeb36-f492-4214-a047-be67af9274dc",
    "name": "Art House"
  },
  {
    "uuid": "ba1b0ce1-7198-4788-b963-2e59ef353e41",
    "name": "News"
  },
  {
    "uuid": "0bf6a4f7-6508-4ea9-a1a6-ee92cfed92aa",
    "name": "Author Cinema"
  },
  {
    "uuid": "66ee2d08-4ea5-43a0-9d4d-e756f1325de6",
    "name": "Reality TV"
  },
  {
    "uuid": "685f97b2-fe23-4afa-86cd-d853a31ef06a",
    "name": "Urban"
  },
  {
    "uuid": "c61e0bf7-4d39-48a9-ae69-a313f6ff068c",
    "name": "War"
  },
  {
    "uuid": "ade4ed69-d05a-4593-a3e7-e298b67ec887",
    "name": "Time Travel"
  },
  {
    "uuid": "b2217f69-51d2-45b1-8821-a3ad1a1f2850",
    "name": "Musical"
  },
  {
    "uuid": "908393a2-2601-47ab-ad16-26177964e8e6",
    "name": "Post-Apocalyptic"
  },
  {
    "uuid": "c167b631-c490-4818-90a2-a04060c64b3d",
    "name": "Horror"
  },
  {
    "uuid": "de1b3627-bc46-47bb-a75c-e5a72699b4fc",
    "name": "Drama"
  },
  {
    "uuid": "808c5f85-8393-4d73-841b-4696ca92f954",
    "name": "Western"
  }
]

our_persons = [
  {
    "uuid": "aba9bdb6-c0a2-4fa4-95d1-bb58a6006011",
    "full_name": "David Torres",
    "films": [
      "f790a5ce-b737-47c9-908c-295ad4b665f9",
      "1a0ee1c8-4426-4b18-8b35-12fc16c11004",
      "8a309134-b282-47bb-a152-dc07c9173cd6",
      "28af29e3-099f-49fb-a5b7-f9e9d7ad461f"
    ]
  },
  {
    "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
    "full_name": "Linda Page",
    "films": [
      "3cc3a80c-b88a-487f-8f26-5de641d3afb7",
      "b2fd87a8-b8be-4d75-af99-274e164bfae9",
      "f790a5ce-b737-47c9-908c-295ad4b665f9",
      "28af29e3-099f-49fb-a5b7-f9e9d7ad461f",
      "5a7895f7-83af-4453-9457-83b3d224da99",
      "1a0ee1c8-4426-4b18-8b35-12fc16c11004",
      "9c7092c9-727b-48dc-82c8-6493ba5d61c6"
    ]
  },
  {
    "uuid": "5e80ed50-e3af-463d-a6e1-1f39a8d4168a",
    "full_name": "Brian Jones",
    "films": [
      "5a7895f7-83af-4453-9457-83b3d224da99",
      "28af29e3-099f-49fb-a5b7-f9e9d7ad461f",
      "be6585ff-97f9-4091-9730-1574f0567fbb"
    ]
  },
  {
    "uuid": "29060b42-909b-432e-8ce3-01e13c5d252b",
    "full_name": "Renee Larson",
    "films": [
      "3cc3a80c-b88a-487f-8f26-5de641d3afb7",
      "9334d717-cebc-4d51-8abb-63eb7161e07e",
      "8a309134-b282-47bb-a152-dc07c9173cd6",
      "35c15cf0-6e2b-431f-acdb-1cdd47e8a485"
    ]
  },
  {
    "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
    "full_name": "Christopher Jones",
    "films": [
      "b2fd87a8-b8be-4d75-af99-274e164bfae9",
      "5a7895f7-83af-4453-9457-83b3d224da99",
      "35c15cf0-6e2b-431f-acdb-1cdd47e8a485",
      "527980a9-f350-4707-9790-d561d814d4a8",
      "ef0c5e93-5f9d-4097-9535-c4febb73d8c3"
    ]
  },
  {
    "uuid": "e100288b-ba2c-42af-b988-d42089363355",
    "full_name": "Tiffany Smith",
    "films": [  # TODO стереть фильмы
      # "3cc3a80c-b88a-487f-8f26-5de641d3afb7",
      # "cc2c5fcd-62ee-4c46-af5c-779f6e9dd0dd",
      # "b6486130-325a-4efb-af0b-54f79b216067",
      # "ef0c5e93-5f9d-4097-9535-c4febb73d8c3",
      # "db8cc444-10b6-44e9-8992-747bd7c8d5b8"
    ]
  },
  {
    "uuid": "ce0846ba-2f8a-43c8-87b9-bf60e49c9a1b",
    "full_name": "Amber Horn",
    "films": [
      "53049cc7-7088-4594-95f3-96058fc38697",
      "47564fa7-24f9-4ae0-a69e-fd00afaad60a",
      "db8cc444-10b6-44e9-8992-747bd7c8d5b8",
      "9334d717-cebc-4d51-8abb-63eb7161e07e"
    ]
  },
  {
    "uuid": "efac829d-ddb7-4b6a-9c56-80a4d51be4ec",
    "full_name": "Tyler Morrison",
    "films": [
      "527980a9-f350-4707-9790-d561d814d4a8",
      "8b479568-618c-40b0-b51f-fdd121a47b21",
      "cc2c5fcd-62ee-4c46-af5c-779f6e9dd0dd",
      "7111f3ab-d429-4b7a-b92c-e14d2540cc1c"
    ]
  },
  {
    "uuid": "976d5fc8-9aaf-46cd-8a46-89a4e5a0fec1",
    "full_name": "Joshua Grimes",
    "films": [
      "53049cc7-7088-4594-95f3-96058fc38697",
      "b6486130-325a-4efb-af0b-54f79b216067",
      "f790a5ce-b737-47c9-908c-295ad4b665f9"
    ]
  },
  {
    "uuid": "040dc70f-ece9-4288-82ac-7d15540c982e",
    "full_name": "Alicia Rodriguez",
    "films": [
      "8b479568-618c-40b0-b51f-fdd121a47b21"
    ]
  }
]


our_persons_films = [  # TODO yeah, that is hoorible
  {
    "uuid": "28af29e3-099f-49fb-a5b7-f9e9d7ad461f",
    "imdb_rating": 1.9166826622226696,
    "title": "Organized mobile paradigm",
    "genre": [
      "Cyberpunk",
      "War",
      "Biography"
    ],
    "genre_full": [
      {
        "uuid": "c61e0bf7-4d39-48a9-ae69-a313f6ff068c",
        "name": "War"
      },
      {
        "uuid": "2381485b-ba4b-4a4f-94db-95cae5c250b4",
        "name": "Cyberpunk"
      },
      {
        "uuid": "1702ef39-6a5d-4ef4-b807-da5a8b9c6c68",
        "name": "Biography"
      }
    ],
    "description": "Politics turn son state. Provide city new force discussion.\nAmong door already institution. Kind best smile yourself firm team. Range result left whether help likely girl when.",
    "directors_names": [
      "David Torres"
    ],
    "actors_names": [],
    "writers_names": [
      "Linda Page",
      "Brian Jones"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      },
      {
        "uuid": "5e80ed50-e3af-463d-a6e1-1f39a8d4168a",
        "name": "Brian Jones"
      }
    ],
    "directors": [
      {
        "uuid": "aba9bdb6-c0a2-4fa4-95d1-bb58a6006011",
        "name": "David Torres"
      }
    ]
  },
  {
    "uuid": "8a309134-b282-47bb-a152-dc07c9173cd6",
    "imdb_rating": 3.2186704840258953,
    "title": "Universal maximized utilization",
    "genre": [
      "Legal",
      "Detective"
    ],
    "genre_full": [
      {
        "uuid": "707baf13-2a31-423a-8564-584fae5783f7",
        "name": "Legal"
      },
      {
        "uuid": "14bb19ce-b2cc-4d15-9387-65bfb7e5d8f2",
        "name": "Detective"
      }
    ],
    "description": "Candidate this fish guess. Return nor along participant. Mother foreign company leg support ok.",
    "directors_names": [
      "David Torres"
    ],
    "actors_names": [],
    "writers_names": [
      "Renee Larson"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "29060b42-909b-432e-8ce3-01e13c5d252b",
        "name": "Renee Larson"
      }
    ],
    "directors": [
      {
        "uuid": "aba9bdb6-c0a2-4fa4-95d1-bb58a6006011",
        "name": "David Torres"
      }
    ]
  },
  {
    "uuid": "b6486130-325a-4efb-af0b-54f79b216067",
    "imdb_rating": 6.426605247881449,
    "title": "Reduced needs-based orchestration",
    "genre": [
      "Crime",
      "Comedy",
      "News",
      "Author Cinema"
    ],
    "genre_full": [
      {
        "uuid": "ba1b0ce1-7198-4788-b963-2e59ef353e41",
        "name": "News"
      },
      {
        "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
        "name": "Comedy"
      },
      {
        "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
        "name": "Crime"
      },
      {
        "uuid": "0bf6a4f7-6508-4ea9-a1a6-ee92cfed92aa",
        "name": "Author Cinema"
      }
    ],
    "description": "Could term defense surface. Ground language many protect miss marriage though. Between story establish ask lead. Wife capital measure although class bank.",
    "directors_names": [
      "Joshua Grimes"
    ],
    "actors_names": [],
    "writers_names": [
      "Tiffany Smith"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "e100288b-ba2c-42af-b988-d42089363355",
        "name": "Tiffany Smith"
      }
    ],
    "directors": [
      {
        "uuid": "976d5fc8-9aaf-46cd-8a46-89a4e5a0fec1",
        "name": "Joshua Grimes"
      }
    ]
  },
  {
    "uuid": "1a0ee1c8-4426-4b18-8b35-12fc16c11004",
    "imdb_rating": 4.143390689555069,
    "title": "Reduced 3rdgeneration interface",
    "genre": [
      "Crime",
      "Epic",
      "Science Fiction",
      "Biography",
      "Vampire"
    ],
    "genre_full": [
      {
        "uuid": "1702ef39-6a5d-4ef4-b807-da5a8b9c6c68",
        "name": "Biography"
      },
      {
        "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
        "name": "Crime"
      },
      {
        "uuid": "9a46b816-5f1c-4306-bc4f-13d2a006f373",
        "name": "Vampire"
      },
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      },
      {
        "uuid": "6679a19e-3c93-4257-a76e-44e2316ae60a",
        "name": "Epic"
      }
    ],
    "description": "Dream receive listen. World coach painting or. Give place positive action such business PM. Such just common process thus.",
    "directors_names": [],
    "actors_names": [
      "Linda Page",
      "David Torres"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      },
      {
        "uuid": "aba9bdb6-c0a2-4fa4-95d1-bb58a6006011",
        "name": "David Torres"
      }
    ],
    "writers": [],
    "directors": []
  },
  {
    "uuid": "b2fd87a8-b8be-4d75-af99-274e164bfae9",
    "imdb_rating": 8.052032866140571,
    "title": "Self-enabling foreground process improvement",
    "genre": [
      "Crime",
      "Comedy",
      "Cyberpunk",
      "Vampire"
    ],
    "genre_full": [
      {
        "uuid": "2381485b-ba4b-4a4f-94db-95cae5c250b4",
        "name": "Cyberpunk"
      },
      {
        "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
        "name": "Comedy"
      },
      {
        "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
        "name": "Crime"
      },
      {
        "uuid": "9a46b816-5f1c-4306-bc4f-13d2a006f373",
        "name": "Vampire"
      }
    ],
    "description": "Role program either themselves human head beyond. Sing business image third sport adult blue.\nVoice true response bring senior. Bill evening audience economy activity bring.",
    "directors_names": [
      "Linda Page"
    ],
    "actors_names": [],
    "writers_names": [
      "Christopher Jones"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
        "name": "Christopher Jones"
      }
    ],
    "directors": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      }
    ]
  },
  {
    "uuid": "7111f3ab-d429-4b7a-b92c-e14d2540cc1c",
    "imdb_rating": 9.394388057186084,
    "title": "Robust tangible customer loyalty",
    "genre": [
      "Crime",
      "Science Fiction",
      "War",
      "Biography",
      "Art House"
    ],
    "genre_full": [
      {
        "uuid": "11ebeb36-f492-4214-a047-be67af9274dc",
        "name": "Art House"
      },
      {
        "uuid": "1702ef39-6a5d-4ef4-b807-da5a8b9c6c68",
        "name": "Biography"
      },
      {
        "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
        "name": "Crime"
      },
      {
        "uuid": "c61e0bf7-4d39-48a9-ae69-a313f6ff068c",
        "name": "War"
      },
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      }
    ],
    "description": "Buy realize idea begin skin. Notice road defense year administration management people. Guess price share bag newspaper possible.",
    "directors_names": [],
    "actors_names": [],
    "writers_names": [
      "Tyler Morrison"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "efac829d-ddb7-4b6a-9c56-80a4d51be4ec",
        "name": "Tyler Morrison"
      }
    ],
    "directors": []
  },
  {
    "uuid": "ef0c5e93-5f9d-4097-9535-c4febb73d8c3",
    "imdb_rating": 5.586249000823028,
    "title": "Switchable maximized contingency",
    "genre": [
      "Art House",
      "News",
      "Zombie"
    ],
    "genre_full": [
      {
        "uuid": "ba1b0ce1-7198-4788-b963-2e59ef353e41",
        "name": "News"
      },
      {
        "uuid": "11ebeb36-f492-4214-a047-be67af9274dc",
        "name": "Art House"
      },
      {
        "uuid": "c8e571f4-b32a-4698-8190-31610d71a04c",
        "name": "Zombie"
      }
    ],
    "description": "Cut her strategy college yard city. Surface focus record page help.\nBoy movement speak accept once each time. By whatever none friend. Few television woman senior pass let visit.",
    "directors_names": [
      "Christopher Jones"
    ],
    "actors_names": [
      "Tiffany Smith"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "e100288b-ba2c-42af-b988-d42089363355",
        "name": "Tiffany Smith"
      }
    ],
    "writers": [],
    "directors": [
      {
        "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
        "name": "Christopher Jones"
      }
    ]
  },
  {
    "uuid": "47564fa7-24f9-4ae0-a69e-fd00afaad60a",
    "imdb_rating": 3.2419420188768022,
    "title": "Persistent national groupware",
    "genre": [
      "Supernatural",
      "News",
      "Reality TV"
    ],
    "genre_full": [
      {
        "uuid": "ba1b0ce1-7198-4788-b963-2e59ef353e41",
        "name": "News"
      },
      {
        "uuid": "036eef26-c456-41f8-9222-71da54a3c9f6",
        "name": "Supernatural"
      },
      {
        "uuid": "66ee2d08-4ea5-43a0-9d4d-e756f1325de6",
        "name": "Reality TV"
      }
    ],
    "description": "Determine despite case trade power plant type second. Strategy list store form use ten.\nBoy weight wear nation particular all.",
    "directors_names": [],
    "actors_names": [
      "Amber Horn"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "ce0846ba-2f8a-43c8-87b9-bf60e49c9a1b",
        "name": "Amber Horn"
      }
    ],
    "writers": [],
    "directors": []
  },
  {
    "uuid": "db8cc444-10b6-44e9-8992-747bd7c8d5b8",
    "imdb_rating": 4.463659661705025,
    "title": "Self-enabling interactive frame",
    "genre": [
      "Historical",
      "Epic",
      "Vampire"
    ],
    "genre_full": [
      {
        "uuid": "6679a19e-3c93-4257-a76e-44e2316ae60a",
        "name": "Epic"
      },
      {
        "uuid": "9cf532d7-b26f-4019-a193-39cdeca0adc6",
        "name": "Historical"
      },
      {
        "uuid": "9a46b816-5f1c-4306-bc4f-13d2a006f373",
        "name": "Vampire"
      }
    ],
    "description": "Effort answer certainly crime bill rule impact. Exactly later while everything rate edge certainly. Level so six.",
    "directors_names": [
      "Amber Horn"
    ],
    "actors_names": [
      "Tiffany Smith"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "e100288b-ba2c-42af-b988-d42089363355",
        "name": "Tiffany Smith"
      }
    ],
    "writers": [],
    "directors": [
      {
        "uuid": "ce0846ba-2f8a-43c8-87b9-bf60e49c9a1b",
        "name": "Amber Horn"
      }
    ]
  },
  {
    "uuid": "527980a9-f350-4707-9790-d561d814d4a8",
    "imdb_rating": 4.870828934768973,
    "title": "Multi-lateral homogeneous protocol",
    "genre": [
      "Thriller",
      "Detective"
    ],
    "genre_full": [
      {
        "uuid": "cac1d46e-0ff3-41fd-a4aa-f68d184b7f6e",
        "name": "Thriller"
      },
      {
        "uuid": "14bb19ce-b2cc-4d15-9387-65bfb7e5d8f2",
        "name": "Detective"
      }
    ],
    "description": "Radio top message here dark decide dream. Season audience prove. Report artist carry rich development dark dinner official.",
    "directors_names": [],
    "actors_names": [
      "Tyler Morrison"
    ],
    "writers_names": [
      "Christopher Jones"
    ],
    "actors": [
      {
        "uuid": "efac829d-ddb7-4b6a-9c56-80a4d51be4ec",
        "name": "Tyler Morrison"
      }
    ],
    "writers": [
      {
        "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
        "name": "Christopher Jones"
      }
    ],
    "directors": []
  },
  {
    "uuid": "3cc3a80c-b88a-487f-8f26-5de641d3afb7",
    "imdb_rating": 1.1754330694502668,
    "title": "Implemented 24hour array",
    "genre": [
      "Comedy",
      "Art House",
      "Zombie"
    ],
    "genre_full": [
      {
        "uuid": "11ebeb36-f492-4214-a047-be67af9274dc",
        "name": "Art House"
      },
      {
        "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
        "name": "Comedy"
      },
      {
        "uuid": "c8e571f4-b32a-4698-8190-31610d71a04c",
        "name": "Zombie"
      }
    ],
    "description": "Throughout none exactly American look foreign special. Economy together rise federal police. Somebody later dog.",
    "directors_names": [
      "Renee Larson"
    ],
    "actors_names": [
      "Linda Page"
    ],
    "writers_names": [
      "Tiffany Smith"
    ],
    "actors": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      }
    ],
    "writers": [
      {
        "uuid": "e100288b-ba2c-42af-b988-d42089363355",
        "name": "Tiffany Smith"
      }
    ],
    "directors": [
      {
        "uuid": "29060b42-909b-432e-8ce3-01e13c5d252b",
        "name": "Renee Larson"
      }
    ]
  },
  {
    "uuid": "9c7092c9-727b-48dc-82c8-6493ba5d61c6",
    "imdb_rating": 7.478627370589944,
    "title": "Quality-focused fault-tolerant intranet",
    "genre": [
      "Comedy",
      "Zombie"
    ],
    "genre_full": [
      {
        "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
        "name": "Comedy"
      },
      {
        "uuid": "c8e571f4-b32a-4698-8190-31610d71a04c",
        "name": "Zombie"
      }
    ],
    "description": "Former bag more month such. Majority pull usually lead most hospital unit. Resource agree trouble wind prevent yard.\nWatch travel left assume population act. Music east believe season.",
    "directors_names": [],
    "actors_names": [],
    "writers_names": [
      "Linda Page"
    ],
    "actors": [],
    "writers": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      }
    ],
    "directors": []
  },
  {
    "uuid": "8b479568-618c-40b0-b51f-fdd121a47b21",
    "imdb_rating": 0.22204103026954192,
    "title": "Implemented 5thgeneration project",
    "genre": [
      "Crime",
      "Science Fiction",
      "Nature",
      "Time Travel"
    ],
    "genre_full": [
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      },
      {
        "uuid": "ade4ed69-d05a-4593-a3e7-e298b67ec887",
        "name": "Time Travel"
      },
      {
        "uuid": "3aa862e6-08dc-40c2-a787-b41975946aac",
        "name": "Nature"
      },
      {
        "uuid": "cf225740-679e-4c7a-be7f-fd48b84790fd",
        "name": "Crime"
      }
    ],
    "description": "Management central country whose start few four.\nKitchen tough career land figure exactly nice. Benefit plan discussion boy church article.",
    "directors_names": [],
    "actors_names": [
      "Alicia Rodriguez",
      "Tyler Morrison"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "040dc70f-ece9-4288-82ac-7d15540c982e",
        "name": "Alicia Rodriguez"
      },
      {
        "uuid": "efac829d-ddb7-4b6a-9c56-80a4d51be4ec",
        "name": "Tyler Morrison"
      }
    ],
    "writers": [],
    "directors": []
  },
  {
    "uuid": "9334d717-cebc-4d51-8abb-63eb7161e07e",
    "imdb_rating": 6.239801258913715,
    "title": "Future-proofed zero tolerance focus group",
    "genre": [
      "Epic",
      "Science Fiction"
    ],
    "genre_full": [
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      },
      {
        "uuid": "6679a19e-3c93-4257-a76e-44e2316ae60a",
        "name": "Epic"
      }
    ],
    "description": "Western suffer think represent record attack. Expect future down would system trade.\nReflect trial student choice arm white reality. Happen these say major vote seem machine.",
    "directors_names": [],
    "actors_names": [
      "Renee Larson",
      "Amber Horn"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "29060b42-909b-432e-8ce3-01e13c5d252b",
        "name": "Renee Larson"
      },
      {
        "uuid": "ce0846ba-2f8a-43c8-87b9-bf60e49c9a1b",
        "name": "Amber Horn"
      }
    ],
    "writers": [],
    "directors": []
  },
  {
    "uuid": "cc2c5fcd-62ee-4c46-af5c-779f6e9dd0dd",
    "imdb_rating": 7.4960639401341655,
    "title": "Proactive object-oriented focus group",
    "genre": [
      "Vampire",
      "Horror",
      "Nature",
      "Legal"
    ],
    "genre_full": [
      {
        "uuid": "707baf13-2a31-423a-8564-584fae5783f7",
        "name": "Legal"
      },
      {
        "uuid": "3aa862e6-08dc-40c2-a787-b41975946aac",
        "name": "Nature"
      },
      {
        "uuid": "c167b631-c490-4818-90a2-a04060c64b3d",
        "name": "Horror"
      },
      {
        "uuid": "9a46b816-5f1c-4306-bc4f-13d2a006f373",
        "name": "Vampire"
      }
    ],
    "description": "Dark after picture score rather. Score list computer plant. Support kitchen fill.\nHospital themselves later teacher.\nCompare stock professor lead different all. Apply artist about oil wife.",
    "directors_names": [
      "Tiffany Smith",
      "Tyler Morrison"
    ],
    "actors_names": [],
    "writers_names": [],
    "actors": [],
    "writers": [],
    "directors": [
      {
        "uuid": "e100288b-ba2c-42af-b988-d42089363355",
        "name": "Tiffany Smith"
      },
      {
        "uuid": "efac829d-ddb7-4b6a-9c56-80a4d51be4ec",
        "name": "Tyler Morrison"
      }
    ]
  },
  {
    "uuid": "53049cc7-7088-4594-95f3-96058fc38697",
    "imdb_rating": 2.3242603273563667,
    "title": "Synergistic bi-directional info-mediaries",
    "genre": [
      "Horror",
      "Psychological"
    ],
    "genre_full": [
      {
        "uuid": "c167b631-c490-4818-90a2-a04060c64b3d",
        "name": "Horror"
      },
      {
        "uuid": "e7efd97f-4300-4c06-8257-0892bb04bf13",
        "name": "Psychological"
      }
    ],
    "description": "Fly it nice friend staff election finish personal. Three bad writer call less cultural forget.\nNotice financial letter million learn right evening. Affect talk listen ever. Deep throw fund security.",
    "directors_names": [
      "Joshua Grimes"
    ],
    "actors_names": [
      "Amber Horn"
    ],
    "writers_names": [],
    "actors": [
      {
        "uuid": "ce0846ba-2f8a-43c8-87b9-bf60e49c9a1b",
        "name": "Amber Horn"
      }
    ],
    "writers": [],
    "directors": [
      {
        "uuid": "976d5fc8-9aaf-46cd-8a46-89a4e5a0fec1",
        "name": "Joshua Grimes"
      }
    ]
  },
  {
    "uuid": "35c15cf0-6e2b-431f-acdb-1cdd47e8a485",
    "imdb_rating": 0.9063096647574986,
    "title": "Proactive reciprocal middleware",
    "genre": [
      "Western",
      "Musical"
    ],
    "genre_full": [
      {
        "uuid": "808c5f85-8393-4d73-841b-4696ca92f954",
        "name": "Western"
      },
      {
        "uuid": "b2217f69-51d2-45b1-8821-a3ad1a1f2850",
        "name": "Musical"
      }
    ],
    "description": "Tough six why window various every record. True could clear create group. Force safe know figure.\nCollection then head probably. Break why discuss.",
    "directors_names": [
      "Renee Larson",
      "Christopher Jones"
    ],
    "actors_names": [],
    "writers_names": [],
    "actors": [],
    "writers": [],
    "directors": [
      {
        "uuid": "29060b42-909b-432e-8ce3-01e13c5d252b",
        "name": "Renee Larson"
      },
      {
        "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
        "name": "Christopher Jones"
      }
    ]
  },
  {
    "uuid": "5a7895f7-83af-4453-9457-83b3d224da99",
    "imdb_rating": 8.869885471371546,
    "title": "Automated bottom-line task-force",
    "genre": [
      "Detective",
      "Short Film",
      "Post-Apocalyptic"
    ],
    "genre_full": [
      {
        "uuid": "908393a2-2601-47ab-ad16-26177964e8e6",
        "name": "Post-Apocalyptic"
      },
      {
        "uuid": "3ea514ef-0bc5-4918-beac-9452eef30452",
        "name": "Short Film"
      },
      {
        "uuid": "14bb19ce-b2cc-4d15-9387-65bfb7e5d8f2",
        "name": "Detective"
      }
    ],
    "description": "Walk explain drive identify. Up success year military side. Again goal draw way speak play.",
    "directors_names": [
      "Christopher Jones"
    ],
    "actors_names": [
      "Linda Page"
    ],
    "writers_names": [
      "Brian Jones"
    ],
    "actors": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      }
    ],
    "writers": [
      {
        "uuid": "5e80ed50-e3af-463d-a6e1-1f39a8d4168a",
        "name": "Brian Jones"
      }
    ],
    "directors": [
      {
        "uuid": "4c450994-07d5-4e80-b16e-50c1d0f64eac",
        "name": "Christopher Jones"
      }
    ]
  },
  {
    "uuid": "f790a5ce-b737-47c9-908c-295ad4b665f9",
    "imdb_rating": 6.917426083087255,
    "title": "Networked intermediate leverage",
    "genre": [
      "Reality TV",
      "Science Fiction",
      "Documentary",
      "Comedy",
      "Western"
    ],
    "genre_full": [
      {
        "uuid": "808c5f85-8393-4d73-841b-4696ca92f954",
        "name": "Western"
      },
      {
        "uuid": "66ee2d08-4ea5-43a0-9d4d-e756f1325de6",
        "name": "Reality TV"
      },
      {
        "uuid": "d7543506-4cc4-4f99-bb20-4cbedd028ded",
        "name": "Comedy"
      },
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      },
      {
        "uuid": "5e073c6d-4565-4637-8f58-b3d325437e64",
        "name": "Documentary"
      }
    ],
    "description": "Food figure world prepare. Purpose development understand visit too staff wait. Success Democrat stop leg.\nTotal fine like million. Community cold nothing. Its time similar company song.",
    "directors_names": [],
    "actors_names": [
      "Joshua Grimes",
      "David Torres"
    ],
    "writers_names": [
      "Linda Page"
    ],
    "actors": [
      {
        "uuid": "976d5fc8-9aaf-46cd-8a46-89a4e5a0fec1",
        "name": "Joshua Grimes"
      },
      {
        "uuid": "aba9bdb6-c0a2-4fa4-95d1-bb58a6006011",
        "name": "David Torres"
      }
    ],
    "writers": [
      {
        "uuid": "b474b556-2962-4bf6-b9d0-588a2f7c70e0",
        "name": "Linda Page"
      }
    ],
    "directors": []
  },
  {
    "uuid": "be6585ff-97f9-4091-9730-1574f0567fbb",
    "imdb_rating": 4.6362991203692,
    "title": "Organized 5thgeneration migration",
    "genre": [
      "Horror",
      "Thriller",
      "Science Fiction",
      "Musical"
    ],
    "genre_full": [
      {
        "uuid": "8bfe61a9-e859-48fa-bbc4-90e4d5f9d9e4",
        "name": "Science Fiction"
      },
      {
        "uuid": "cac1d46e-0ff3-41fd-a4aa-f68d184b7f6e",
        "name": "Thriller"
      },
      {
        "uuid": "b2217f69-51d2-45b1-8821-a3ad1a1f2850",
        "name": "Musical"
      },
      {
        "uuid": "c167b631-c490-4818-90a2-a04060c64b3d",
        "name": "Horror"
      }
    ],
    "description": "Into pressure need start hard arrive so. Must follow enjoy ball everybody take leg.\nGame his PM animal dark make common daughter. Realize learn end interest significant job. Leave unit do.",
    "directors_names": [
      "Brian Jones"
    ],
    "actors_names": [],
    "writers_names": [],
    "actors": [],
    "writers": [],
    "directors": [
      {
        "uuid": "5e80ed50-e3af-463d-a6e1-1f39a8d4168a",
        "name": "Brian Jones"
      }
    ]
  }
]