FROM python:3.10
# ENV PYTHONPATH "${PYTHONPATH}:/firstRestAPI/app"
WORKDIR /app
COPY ./firstRestAPI/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "app1234:create_app()" ]