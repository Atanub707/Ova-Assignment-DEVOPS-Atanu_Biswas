FROM python:3.9
COPY server.py /app/server.py
WORKDIR /app
RUN pip install --no-cache-dir Flask
EXPOSE 5000
CMD ["python", "chatbot.py"]