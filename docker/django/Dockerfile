FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (cache layer)
COPY requirements/base.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy project
COPY app /app

# Create non-root user
RUN useradd -m django
USER django

# Add ruff
RUN pip install --no-cache-dir ruff

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
