FROM python:3.9-slim-buster
RUN pip install flask
WORKDIR /app
COPY src/ .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]