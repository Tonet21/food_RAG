# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose any necessary ports (if applicable)
EXPOSE 8000

# Define the command to run the application
CMD ["python", "main.py"]
