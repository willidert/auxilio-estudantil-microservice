FROM python:3.7

WORKDIR /notifyer

COPY . .

RUN pip install -r requirements.txt

CMD python3 email_notifyer.py

EXPOSE 465
