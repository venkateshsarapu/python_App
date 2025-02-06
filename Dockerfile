# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY app.py requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the Flask app
EXPOSE 80

# Run the Flask application
CMD ["python", "app.py"]
