black = black -S -l 120 --target-version py38
isort = isort -w 120

.PHONY: install
install:
	pip install -U setuptools pip
	pip install -U .
	pip install -r tests/requirements.txt

.PHONY: format
format:
	$(isort) pydf tests
	$(black) pydf tests

.PHONY: lint
lint:
	python setup.py check -rms
	flake8 pydf tests
	$(isort) --check-only pydf tests
	$(black) --check pydf tests

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
