# Welcome :wave:

This is a repository to keep track of some deep-dives I will be doing into the land of Python.

I am interested in re-learning some Python to check on the state of the language, as well as diving into further advanced concepts.

## Running :running:
This project is set up using Docker. To run it simply utilize the make commands and run the docker container like a VM.

### Run all the things!
1. `make build`: build the docker image & compose network (alias for `docker-compose build`)
2. `make run`: run the container in detatched state (alias for `docker-compose up -d`)
3. `make shell`: get a bash shell into the container, then run python files as desired
   1. e.g: `python src/basics/03_hello_world.py`

### Additional Commands
- `make stop`: stop the docker compose network (alias for `docker-compose down`)
- `make lint`: run flake8 inside the running docker container to enforce pep8 formatting.
- `make lint-fix`: run autopep8 inside the container to fix simple pep8 errors; will not fix all errors but helps on some of the more tedious ones.