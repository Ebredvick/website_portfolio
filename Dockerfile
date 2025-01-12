# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app/

# Copy the current directory contents into the container at /usr/src/app
COPY ./app /app

# Install any needed packages specified in pyproject.toml
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev -vvv

# Make port 8000 available to the world outside this container
EXPOSE 8000