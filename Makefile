
.PHONY: test

test: test-papers
	./test-papers paper*/*




.PHONY: docker-image docker-run

docker-image: Dockerfile
	docker build -t badi/texlive .

docker-run: docker-image
	docker run -v $(PWD):/data -it --rm badi/texlive
