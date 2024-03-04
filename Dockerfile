# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies
RUN pip install --no-cache-dir Flask

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "chatbot.py"]
