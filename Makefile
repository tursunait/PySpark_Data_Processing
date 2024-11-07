# Install dependencies
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests using pytest and generate coverage
test:
	python -m pytest -vv --cov=main --cov= test_*.py

# Run unittests directly
unittest:
	python -m unittest discover -s . -p "test_*.py"


# Format code with black
format:
	black *.py 

# Lint code with ruff (for faster linting)
lint:
	ruff check *.py 

# Lint Dockerfile with hadolint
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

# Refactor: run format and lint
refactor: format lint

# Deploy target (implementation needed)
deploy:
	# deploy goes here

# Run all steps (install, lint, test, format, deploy)
all: install lint test format deploy
