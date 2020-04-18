
clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage

test:
	pytest

PROJECT = procesark

coverage: 
	pytest -x --cov=$(PROJECT) tests/ --cov-report term-missing -s -vv

serve:
	python -m $(PROJECT) serve

PART ?= patch

version:
	bump2version $(PART) $(PROJECT)/__init__.py --tag --commit
