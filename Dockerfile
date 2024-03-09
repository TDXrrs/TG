
FROM mcr.microsoft.com/azure-app-service/python:3.9  # Use a base image optimized for Azure App Service

WORKDIR /home/site/wwwroot  # Default working directory in Azure App Service

COPY requirements.txt ./  # Copy requirements.txt first for caching
RUN pip install -r requirements.txt

COPY ./app/ /home/site/wwwroot/  # Copy the entire app contents

EXPOSE 8000  # Expose port for web app (if applicable)

# Run the app with appropriate startup command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]  # Adjust as needed
