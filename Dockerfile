# Use an Azure App Service base image for Python 3.9
FROM mcr.microsoft.com/azure-app-service/python:3.9

# Set the working directory in the container
WORKDIR /home/site/wwwroot

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Command to run the bot
CMD ["python", "app.py"]
