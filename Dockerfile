# Use the Python base image for Azure Web App
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

# Set working directory
WORKDIR /home/site/wwwroot

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
