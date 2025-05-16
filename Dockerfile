FROM python:3.10-slim
 
WORKDIR /app
 
# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app /app/app
COPY templates /app/templates
COPY static /app/static
COPY main.py /app/main.py

# Ensure template and static directories exist
RUN mkdir -p /app/templates /app/static
 
EXPOSE 8000
 
# Run with production settings
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]