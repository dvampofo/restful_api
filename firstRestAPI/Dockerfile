FROM python:3.10
ENV APP1 ./firstRestAPI/app.python
WORKDIR /app
COPY ./firstRestAPI/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "${APP1}:create_app()" ]