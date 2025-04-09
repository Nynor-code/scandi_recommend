# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /src

# Expose port (8080 is the standard port for streamlit, but it will change automatically if the port gets busy)
EXPOSE 8080

# Run  streamlit
CMD ["streamlit", "run", "src/app.py", "--server.port=8080", "--server.address=0.0.0.0"]
