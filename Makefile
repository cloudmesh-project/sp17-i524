
.PHONY: test

test: test-papers
	./test-papers paper*/*




.PHONY: docker-image docker-run

docker-image: Dockerfile
	docker build -t badi/texlive .

docker-run: docker-image
	time docker run \
	  -e HOST_UID=$(shell id -u) \
	  -e HOST_GID=$(shell id -g) \
	  -v $(shell pwd):/data \
	  -it \
	  --rm \
	  badi/cloudmesh_classes:latest \
	  make

