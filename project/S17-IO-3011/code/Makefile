FILE=report

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
OPENCMD=open
endif
ifeq ($(UNAME), Linux)
OPENCMD=xdg-open
endif

all: install run view

real-clean: clean
	echo '' > ansible/inventory

clean:
	rm -rf *~

deploy:
	scripts/deploy.sh

install:
	scripts/install.sh

run:
	scripts/run.sh

delete:
	scripts/delete.sh

view:
	$(OPENCMD) ${FILE}.pdf

.PHONY: all clean view fast watch
