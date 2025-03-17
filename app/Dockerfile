# ---------- Stage 1: Build dependencies ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install system build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install to target dir
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/python_packages -r requirements.txt

# ---------- Stage 2: Minimal runtime image using Distroless ----------
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy application code
COPY app.py .

# Copy installed Python packages
COPY --from=builder /app/python_packages /app/python_packages

# Set PYTHONPATH so Python knows where to find the packages
ENV PYTHONPATH="/app/python_packages"

# Use non-root user
USER nonroot

# Expose port
EXPOSE 80

# Run app
CMD ["app.py"]

