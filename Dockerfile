FROM python
WORKDIR /test
COPY . /test
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords punkt
CMD [ "python", "A2_python_code.py" ]