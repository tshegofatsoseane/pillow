# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY backend/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY backend/ /app/

# Expose port 8000 for the app
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "pillow_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"]
