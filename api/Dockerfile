# docker build --progress=plain -t my-api .

FROM python:3.11-slim

LABEL version="1.0.0"
LABEL description="FastAPI backend for the web application"
LABEL maintainer="Kaveh"

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# fastapi run main.py --port 8000
ENTRYPOINT [ "fastapi", "run", "main.py", "--port", "8000" ]
