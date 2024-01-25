.PHONY: help run test
DEFAULT_GOAL := help

help:
	@echo "make run"
	@echo "       run prompt"
	@echo "make test"
	@echo "       test all python code"

run:
	pdm run python src/main.py

test:
	pdm run pytest tests

typecheck:
	pdm run mypy src