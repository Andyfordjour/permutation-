FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the application file into the container
COPY app.py .

# Run the program when the container starts
CMD ["python", "app.py"]
