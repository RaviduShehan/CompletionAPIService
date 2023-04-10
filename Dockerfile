FROM python:buster
WORKDIR /CompletionApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5002
ENTRYPOINT ["python", "./src/completion.py"]