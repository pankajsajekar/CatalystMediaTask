FROM python:3.10

ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY .  /app
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./entrypoint.sh /app/entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Make port 80 available to the world outside this container
# EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]