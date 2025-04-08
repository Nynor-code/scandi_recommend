# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (you can customize this)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]