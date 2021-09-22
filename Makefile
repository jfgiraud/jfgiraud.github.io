.ONESHELL:
SHELL=bash


.PHONY: usage
usage:
	@cat - <<EOF
		Targets:
		* up: start services
		* down: stop services
		* pyterm: open term on python_app
	EOF

up:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose up -d --build

down:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose down

pyterm:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose exec python_app bash