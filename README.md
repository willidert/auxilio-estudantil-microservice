## Auxílio Estudantil Microservice

## Time 

|Nome|Matricula|
|-|-|
|Mateus Bentes Marreira| 2019003154|
|William Bentes Marreira| 1231 | 
|Matheus Fernandes Bentes Marreira| 123|
|Marios Guilherme Bentes Marreira| 123

## Descrição do Problema

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas velit, commodo molestie est tristique in. Cras

elementum ante a quam lacinia ullamcorper. Integer pulvinar purus ut tellus faucibus scelerisque. Morbi quis ex vel dui 

commodo vestibulum eget a erat. Ut volutpat mauris auctor rutrum tincidunt. Vestibulum et ante tempor, porta lorem eleifend, 

porta augue. Etiam tincidunt arcu eros, in lacinia dolor vehicula nec

## Arquitetura

![This is a alt text.](https://cdn.discordapp.com/attachments/640981909777940521/866457695653855232/arch2.png)

### Tecnologias utilizadas

* Inteface gráfica (frontend):  Angular 
* Load Balancer/API Gateway: NGINX 
* Microservice 1: APIService (Typescript + MongoDB) 
* Microservice 2: Mensageria (RabbitMQ) 
* Microservice 3: TreatmentService (Python) 
* Microservice 4: ModelService (Python) 
* Microservice 5: NotifyService (Python) 

|Nome|Service|Language|Description|Justification|
|-|-|-|---------------------|-|
|Mateus Bentes|[Frontend](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/web)|Angular|Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas|a|
|Mateus Bentes|[APIService](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/api)|Node.js (Typescript)|Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas|a|
|Shakka|[TreatmentService]()|Python|Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas|a|
|William|[ModelService](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/model)|Python|Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas|a|
|Mario|[NotifyService]()|Python|Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fermentum egestas|a|


## Executando o projeto 

Clone o respositório para a sua máquina e execute o comando abaixo: 

```
git clone https://github.com/willidert/auxilio-estudantil-microservice
```
Entre no projeto clonado: 
```
cd microservices-test/
```
Na raiz do projeto  digite: 
```
docker-compose up 
```
