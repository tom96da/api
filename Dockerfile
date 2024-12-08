# check=error=true

ARG PYTHON_VERSION=3.12
FROM docker.io/library/python:${PYTHON_VERSION}-slim AS base


WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

FROM base AS development

RUN pip install --upgrade pip

COPY requirements.txt packages.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -r packages.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
