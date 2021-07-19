#Create a ubuntu base image with python 3 installed.
FROM python:3.7

#Set the working directory
WORKDIR /app

RUN apt-get update
RUN apt install -y netcat
#copy all the files
COPY . .

# RUN pip install -U pip
#Install the dependencies
RUN pip install -r requirements.txt
# RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh wait-for-it.sh 

RUN chmod +x wait-for-it.sh

#Run the command
CMD ["python3", "receive.py"]

# ENTRYPOINT [ "/bin/bash", "-c" ]
