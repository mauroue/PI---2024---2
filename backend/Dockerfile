# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install PostgreSQL development libraries and other dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Expose the port
EXPOSE 8000

CMD ["python", "manage.py", "migrate"]

