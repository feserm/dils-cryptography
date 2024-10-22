FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["litestar", "run", "--debug", "--reload", "--port", "8000", "--host", "0.0.0.0"]
