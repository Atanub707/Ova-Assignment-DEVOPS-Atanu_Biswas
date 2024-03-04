FROM python:3.9
COPY server.py /app/server.py
WORKDIR /app
CMD ["python", "-u", "server.py"]