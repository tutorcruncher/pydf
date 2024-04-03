.PHONY: install
install:
	pip install -U setuptools pip
	pip install -U .
	pip install -r tests/requirements.txt

.PHONY: format
format:
	ruff check --fix pydf tests
	ruff format pydf tests

.PHONY: lint
lint:
	python setup.py check -rms
	ruff check pydf tests
	ruff format --check pydf tests

.PHONY: test
test:
	pytest --cov=pydf

.PHONY: testcov
testcov:
	pytest --cov=pydf && (echo "building coverage html"; coverage html)

.PHONY: all
all: testcov lint

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	python setup.py clean
