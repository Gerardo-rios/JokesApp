create-dev-env:
			python3 -m venv .venv && \
			. .venv/bin/activate && \
			pip install poetry && \
			poetry install;
			export PYTHONPATH=$(pwd):$PYTHONPATH;

override AUTOFLAKE_FORMAT=echo Run autoflake...; autoflake \
		--remove-all-unused-imports \
		--remove-unused-variables \
		--recursive \
		--in-place adapters/ api/ core/ factories \
		--exclude=__init__.py;

start:
	docker run -d -p 8000:8000 -it jokes-app-backend

test:
	export PYTHONPATH=$(pwd):$PYTHONPATH;
	pytest -v;

format:
	${AUTOFLAKE_FORMAT}
	echo Run black...; black adapters/ api/ core/ factories;
	echo Run isort...; isort adapters/ api/ core/ factories;
	echo Run flake8...; flake8 adapters/ api/ core/ factories;
	echo Run mypy...; mypy adapters/ api/ core/ factories;