# Use the official Python image from the Docker Hub

FROM python:3.8.2

# Expose app on port 8000
EXPOSE 8000

# Make a new directory to put our code in.

RUN mkdir /code

# Change the working directory.

WORKDIR /code

# Copy to code folder

COPY . /code/

# Install the requirements.

RUN pip install -r requirements.txt

# Run the application:

CMD python manage.py runserver 0.0.0.0:8000
