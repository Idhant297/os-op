FROM --platform=linux/arm64 python:3.9-slim

WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose port if needed
EXPOSE 8000

CMD ["python", "app.py"]