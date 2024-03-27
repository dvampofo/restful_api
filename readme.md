# Building a RESTful API

## Introduction
I will be guided in creating simple, intermediate, and advanced REST APIs including authentication, deployments, databases, and much more.

Using Flask and popular extensions Flask-Smorest, Flask-JWT-Extended, and Flask-SQLAlchemy, I will dive right into developing complete, solid, production-ready REST APIs. I will be using [Insomnia](https://insomnia.rest/) to send payloads to my endpoints.

I will also look into essential technologies like Git and database migrations with Alembic.

I'll demonstrate how to:
- Create resource-based, production-ready REST APIs using Python, Flask, and popular Flask extensions.
- Handle secure user registration and authentication with Flask.
- Use SQLAlchemy and Flask-SQLAlchemy to easily and efficiently store resources to a database.
- Understand the complex intricacies of deployments of Flask REST APIs.
- Use Docker to simplify running and deploying my REST APIs.

## But what is a REST API anyway?

A REST API is an application that accepts data from clients and returns data back. For example, a REST API could accept text data from me, such as a username and password, and return whether that is a valid user in the database.

When developing REST APIs, our clients are usually web apps or mobile apps. That's in contrast to when I make websites, where the clients are usually the users themselves.

I'll develop a REST API that not only allows clients to authenticate but also to store and retrieve any data I want from a database. Learning this will help me develop any REST API that I need for my own projects!

## Docker Instructions

To build with Docker:

```
docker build -t <---- IMAGE-NAME ----> .
docker run -dp 5050:5000 -w /app -v "$(pwd):/app" <---- IMAGE-NAME ----> sh -c "flask run --host 0.0.0.0"
```