# Stage 1: Base image
FROM python:3

# Set working directory
WORKDIR /app

# 2. Copy files
COPY . /app

RUN pip install -r /app/requirements.txt

# Run python
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]