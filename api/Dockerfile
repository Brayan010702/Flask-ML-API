FROM python:3.8.13 as base

# Append /home/app/.local/bin/ to PATH variable because
# gunicorn is installed there.
ENV PYTHONPATH=$PYTHONPATH:/src/
ENV PATH=$PATH:/home/app/.local/bin/

COPY ./ /src

WORKDIR /src

RUN pip install --upgrade pip && pip install -r requirements.txt

# Ensure the static/uploads directory exists and set permissions
RUN mkdir -p /src/static/uploads && chmod -R 777 /src/static/uploads

FROM base as test
RUN ["pytest", "-v", "/src/tests"]

FROM base as build
ENTRYPOINT ["gunicorn", "--workers=8", "--bind", "0.0.0.0:5000", "app:app"]
