# Use Python slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app


# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY loadmodelfromgit/ ./loadmodelfromgit/

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Set the entrypoint
ENTRYPOINT ["python", "main.py"]

# Default command shows help
CMD ["--help"]