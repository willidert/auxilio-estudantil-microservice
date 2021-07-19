import smtplib, ssl
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from mongo_observer.observer import Observer
from mongo_observer.operation_handlers import ReactiveCollection

class SendEmail:
    
    def __init__(self, port=465, situation=None, receiver_email=None) -> None:
        with open("credential.txt","r") as credential:
            self.__sender_email = credential.readline().strip("\n")
            self.__password = credential.readline().strip("\n")
            self.__server_email = credential.readline().strip("\n")
        self.__receiver_email = receiver_email
        self.__context = ssl.create_default_context()
        self.__situation = situation
        self.__server = smtplib.SMTP_SSL(self.__server_email, port, context=self.__context)

    def __login(self):
        return self.__server.login(self.__sender_email, self.__password)

    def create_message(self):
        return  f"""\
                        Subject: RESULTADO AUXILIO ESTUDANTIL

                        O Resultado do seu auxilio estudantil: { 'Aprovado'if situation else 'Reprovado'}"""

    def send_email(self):
        self.__login()
        server.sendmail(self.__sender_email, self.__receiver_email, message)



async def run(loop):
    client = AsyncIOMotorClient('mongozao:27017')

    collection_to_observe = client['your_db']['your_collection']
    reactive_collection = await ReactiveCollection.init_async(collection_to_observe)

    observer = await Observer.init_async(oplog=client['local']['oplog.rs'],
                                         operation_handler=reactive_collection,
                                         namespace_filter='your_db.your_collection')

    loop.create_task(observer.observe_changes())


loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))
loop.run_forever()