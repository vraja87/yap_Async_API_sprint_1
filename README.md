# Async API

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/telemachor/Async_API_sprint_1)

## Setup

- Create and fill out a `.env` using `.env.example`.
- **Start Docker Containers**: Simply run the `make` command to start all necessary containers and initialize the project:
  - Build and start all Docker services defined in `docker-compose.yaml`.
  - Apply database migrations to set up your database schema.
  - Collect static files for the admin panel.
  - Create a superuser for admin access.
  - Generate initial data for the application (e.g., sample movies, genres, etc.).

## Description
This project provides an admin panel and API for searching and retrieving information about movies, genres, and persons. 

You can filter movies based on various parameters such as genre, IMDb rating, and sorting. Pagination is also supported for easy viewing of large data sets.

# Usage Guide

The Makefile provides a set of commands to manage and interact with project using Docker Compose.  Here's how you can use them:

#### Base Makefile Commands

| Command          | Description                                                                          |
|------------------|--------------------------------------------------------------------------------------|
| `make`           | Initialize the project (start, migrations, create superuser, data generation, etc.). |
| `make up`        | Start all Docker containers in the background.                                       |
| `make down`      | Stop all Docker containers.                                                          |
| `make hard_down` | Remove all Docker containers and networks. Deletes initialization flag.              |
| `make migrate`   | Apply database migrations.                                                           |

#### API Endpoints

> For more details on the API, refer to the Swagger documentation at `/api/openapi`

- **GET /api/v1/films/**: Retrieve a list of films with the option to filter by genre, IMDb rating, etc.
- **GET /api/v1/films/search/**: Search for films with optional filtering and "soft" search.
- **GET /api/v1/films/{film_id}**: Retrieve detailed information about a film by its ID.
- **GET /api/v1/genres/**: Retrieve a list of all genres.
- **GET /api/v1/persons/search/**: Search for persons by name with optional "soft" search.
