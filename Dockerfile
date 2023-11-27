FROM python:3.12.0-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .flake8 .

COPY src/ .

# Use tail -f /dev/null to keep the container running
CMD ["tail", "-f", "/dev/null"]
