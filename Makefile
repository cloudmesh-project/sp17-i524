
.PHONY: test

test: test-papers
	./test-papers paper*/*


all:
	cd paper1; make
	cd paper2; make
	cd project; make
	git commit -a -m "chg:usr: update proceedings"
	git push

.PHONY: docker-image docker-run

docker-image: Dockerfile
	docker build -t badi/texlive .

docker-run:
	time docker run \
	  -e HOST_UID=$(shell id -u) \
	  -e HOST_GID=$(shell id -g) \
	  -v $(shell pwd):/data \
	  -it \
	  --rm \
	  badi/cloudmesh_classes:latest \
	  make

