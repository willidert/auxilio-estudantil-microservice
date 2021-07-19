FROM python:3.7.5

RUN pip install -r requirements.txt

WORKDIR /notifyer

COPY . .

CMD python3 email_notifyer.py

EXPOSE 465