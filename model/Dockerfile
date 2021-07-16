#Create a ubuntu base image with python 3 installed.
FROM python:3.7

#Set the working directory
WORKDIR /app

#copy all the files
COPY . .

# RUN pip install -U pip
#Install the dependencies
RUN pip install -r requirements.txt
# RUN python3 -m pip install --no-cache-dir -r requirements.txt

#Expose the required port
EXPOSE 5000

#Run the command
CMD ["python3", "main.py"]

