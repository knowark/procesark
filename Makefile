
clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage

test:
	pytest

PROJECT = procesark
COVFILE ?= .coverage

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov-branch \
	--cov=$(PROJECT) tests/ --cov-report term-missing -x -s -vv \
	-W ignore::DeprecationWarning -o cache_dir=/tmp/serproser/cache

serve:
	python -m $(PROJECT) serve

deploy:
	./setup/deploy.sh procesark

PART ?= patch

version:
	bump2version $(PART) $(PROJECT)/__init__.py --tag --commit
