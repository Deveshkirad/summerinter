# Dockerized Python Application

## Objective

This project demonstrates a Dockerized Python application using the official Python 3.12 Slim image.

The application prints:

- Current Python version
- Current Date and Time

---

## Project Structure

docker-python-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

---

## Build Docker Image

```bash
docker build -t python-info-app .