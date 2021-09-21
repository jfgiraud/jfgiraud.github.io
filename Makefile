.ONESHELL:
SHELL=bash


.PHONY: usage
usage:
	@cat - <<EOF
		Targets:
		* run: run server
	EOF

.PHONY: run
run:
	YIP=$(shell ip a | grep 'inet 192' | awk '{ print $$2 }' | sed -e 's#/.*##')
	echo "http://$$YIP:4000/blog/"
	docker run --rm --volume="$$PWD:/srv/jekyll" --publish $$YIP:4000:4000 jekyll/jekyll jekyll serve

up:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose up -d --build

down:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose down

pyterm:
	export DOCKER_USER="$(shell id -u):$(shell id -g)"
	docker-compose exec python_app bash