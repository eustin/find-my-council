SHELL := /bin/bash

.PHONY: install-server
install-server:
	@cd server &&\
	python3 -m venv venv &&\
	source venv/bin/activate &&\
	python3 -m pip install -r requirements.txt

.PHONY: build-shapely-file
build-shapely-file:
	@cd server &&\
	source venv/bin/activate &&\
	python3 src/scripts/build_shapely_file.py

	
