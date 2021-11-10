.ONESHELL:
SHELL=bash

.EXPORT_ALL_VARIABLES:
USER_UID=$(shell id -u)
USER_GID=$(shell id -g)
DOCKER_USER=$$USER_UID:$$USER_GID
USER_NAME=dev
USER_PASSWORD=test
ROOT_PASSWORD=test

.PHONY: usage
usage:
	@cat - <<EOF
		Targets:
		* build: create .env file and build images
		* logs: display jekyll service logs
		* up: start containers
		* down: stop containers
		* term: open tmux on each container
	EOF

.env:
	DOCKER_USER=$$USER_UID:$$USER_GID
	cat > .env <<EOF
	USER_UID=$${USER_UID}
	USER_GID=$${USER_GID}
	DOCKER_USER=$${USER_UID}:$${USER_GID}
	USER_NAME=$${USER_NAME}
	USER_PASSWORD=$${USER_PASSWORD}
	ROOT_PASSWORD=$${ROOT_PASSWORD}
	EOF

.PHONY: build
build: .env
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs jekyll

.PHONY: run
term:
	@figlet -t $@
	tmux start-server
	tmux new -d -s ghp -n bash
	tmux new-window -t ghp:1 -n python_app
	tmux send-keys -t ghp:1 "docker-compose exec python_app bash" C-m
	tmux select-window -t 1
	tmux attach -t ghp