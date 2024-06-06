# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install ffmpeg and flac
RUN apt-get update && \
    apt-get install -y ffmpeg flac

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run setup.py to create necessary folders
RUN python setup.py

# Define environment variable
ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]
