FILE=output/plots/plot*.png

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
OPENCMD=open
endif
ifeq ($(UNAME), Linux)
OPENCMD=xdg-open
endif

all: deploy install run view delete

benchmark:
	scripts/benchmark.sh $(num_nodes)

real-clean: clean
	echo '' > ansible/inventory

clean:
	rm -rf *~ output

deploy:
	scripts/deploy.sh $(num_nodes)

install:
	scripts/install.sh

run:
	scripts/run.sh

delete:
	scripts/delete.sh

view:
	scripts/view.sh
	$(OPENCMD) ${FILE}

.PHONY: all clean view fast watch
