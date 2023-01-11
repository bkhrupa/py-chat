FROM python:3.7.16
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py