FROM python:3.12.3

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local'

COPY . /app
WORKDIR /app

# Install poetry & dependencies
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry lock
RUN poetry install --no-interaction --no-ansi

CMD ["bash", "entrypoint.sh"]
