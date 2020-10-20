CURRENT_DIRECTORY := $(shell pwd)

SERVER_SERVICE = server
TEST_SERVICE = server_test

ifneq ("$(wildcard ./docker-compose.override.yml)","")
    DC_FILE := docker-compose.override.yml
else
    DC_FILE := docker-compose.yml
endif

DC_CMD = docker-compose -f ${DC_FILE}


.PHONY: up stop restart cli build pip-compile


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  stop               stop all containers"
	@echo "  up                 run all containers"
	@echo "  restart            stop + up"
	@echo "  cli                to run a container console"
	@echo "  build              to make all docker assembly images"
	@echo "  pip-compile        to make pip-compile"
	@echo "  test               Run all tests"
	@echo ""
	@echo "See contents of Makefile for more targets."

stop:
	$(DC_CMD) down

up:
	$(DC_CMD) up $(SERVER_SERVICE) $(CLIENT_SERVICE) db

restart: stop up

cli:
	$(DC_CMD) run --rm $(SERVER_SERVICE) python src/shell.py

build:
	$(DC_CMD) build

pip-compile:
	$(DC_CMD) run --rm --no-deps $(SERVER_SERVICE) pip-compile


test:
	$(DC_CMD) run --rm $(TEST_SERVICE) python -m pytest -s -vvv
