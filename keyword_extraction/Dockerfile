FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader stopwords
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]