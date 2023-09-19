FROM python:latest
WORKDIR /app

# Copy only requirements, to cache them in docker layer
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all other files
COPY . .

CMD ["python", "./index.py"]

EXPOSE 5000
