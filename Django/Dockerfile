# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Set PYTHONPATH to include the base directory
ENV PYTHONPATH=/app 

# Install dependencies
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    apt-get clean

# Copy only requirements first (to leverage Docker cache)
COPY requirements.txt . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project
COPY . .

# Set the working directory to the subfolder containing manage.py
WORKDIR /app/app 

# Expose the Django port
EXPOSE 8000

# Run migrations and start Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
