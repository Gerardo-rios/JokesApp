FROM python:3.10.12
ENV POETRY_VERSION=1.7.1

WORKDIR /app
RUN pip install "poetry==$POETRY_VERSION"

COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY . .
COPY .flake8 .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main \
    && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
