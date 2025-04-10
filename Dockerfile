# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to avoid some interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python3, pip3, vim, and curl
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \
    curl \
    && apt-get clean

# Set working directory in the container
WORKDIR /app/

# Copy the requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copy all project files into the container
COPY . .

# Copy the .env file for environment variable configuration
COPY .env .env

# Expose the port the app will run on
EXPOSE 1122

# Command to run FastAPI and Telegram bot (use python3 instead of python)
CMD ["sh", "-c", "uvicorn main_web:app --host 0.0.0.0 --port 1122 & python3 telegram_bot.py"]