# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# set the working directory
WORKDIR /app

# copy the application
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port FastApi will run
EXPOSE 5000

# COMMAND TO RUN THE FastAPI app
CMD [ "python3", "app.py" ]

