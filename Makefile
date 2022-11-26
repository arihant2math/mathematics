all: test build

test:
	python3 -m pytest .

build:
	python3 setup.py sdist

clean:
	rm -rf "mathematics.egg-info"
	rm -rf "dist"
	rm -rf ".pytest_cache"

cleandocs:
	rm -rf "docs_build"
