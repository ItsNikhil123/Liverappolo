# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy pyproject.toml for dependency installation
COPY pyproject.toml .

# Install dependencies using pip
RUN pip install --no-cache-dir \
    fastapi>=0.137.2 \
    imblearn>=0.0 \
    matplotlib>=3.11.0 \
    numpy>=2.4.6 \
    pandas>=3.0.3 \
    scikit-learn>=1.9.0 \
    seaborn>=0.13.2 \
    uvicorn>=0.49.0

# Copy application code
COPY app.py .
COPY models/ ./models/
COPY templates/ ./templates/

# Expose port for FastAPI
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/docs')" || exit 1

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
