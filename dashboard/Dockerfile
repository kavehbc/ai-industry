# docker build --progress=plain -t my-dash:latest -t my-dash:v1 .

FROM python:3.11-slim

LABEL version="1.0.0"
LABEL description="Streamlit frontend for the web application"
LABEL maintainer="Kaveh"

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

# streamlit run app.py
ENTRYPOINT [ "streamlit", "run", "app.py" ]
