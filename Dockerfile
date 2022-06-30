# Pull the base from 
FROM python:3.8

# Set the environment variables

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory
WORKDIR /test_project

RUN pip install --upgrade pip
# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /test_project/