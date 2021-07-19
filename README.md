## Auxílio Estudantil Microservice

## Time 

|Nome|Matricula|
|-|-|
|Mateus Bentes Marreira| 2019003154 |
|William dos Santos Teixeira| 2019002916 | 
|Matheus Fernandes Oliveira| 2019008007 |
|Mario Guilherme Carvalho| 2019007940 |

## Descrição do Problema

Anualmente muitos alunos acessam o sistema para participarem das inscrições para o PNAES, como forma de auxiliar a equipe de assistência social do campus foi desenvolvido um modelo para realizar as predições dos alunos que podem ou não receber auxílio do campus. Considerando o pico de acessos em determinados períodos do ano e que as inscrições para o PNAES podem ser feitas de forma independete do resto do sistema, foi implementada uma arquitetura em microsserviços para servir o modelo que faz a predição.

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

## Funcionalidades e Padrões de Projetos 
A descrição de cada funcionalidade e os Padrões de Projeto utilizados estão separados em cada serviço que um membro da equipe implementou. Eles podem ser acessados pelos links na coluna "Serviço" da tabela abaixo:

|Nome|Serviço|Linguagem|Descrição|Justificativa|
|-|-|-|---------------------|-|
|Mateus Bentes|[Frontend](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/web)|Angular|Angular é uma framework de aplicações web de código-fonte aberto e plataforma de desenvolvimento para a criação de aplicativos de página única eficientes e sofisticados.|Angular é uma escolha popular para desenvolvimento de aplicações web, diferente de seus semelhantes, angular tem várias ferramentas built-in que auxiliam no desenvolvimento. É um framework opinativo e possui uma arquitetura escalável e bem sofisticada.|
|Mateus Bentes|[APIService](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/api)|Node.js (Typescript)|Node.JS é uma plataforma baseada no interpretador V8 do Google e que permite a execução de códigos JavaScript fora de um navegador web, comumente no backend de uma aplicação. Ele utiliza Javascript como sua linguagem padrão, mas neste projeto usaremos Typescript que é um superset de Javascript e nos permite utilizar recursos de Orientação a Objetos mais robustos.|Node.JS é uma boa opção para lidar com requisições por ser I/O não bloqueante ele consegue lidar com uma grande número de requisições. Como não vamos trabalhar com processos que utilizam muito da CPU, ele passa a ser uma opção decente para este propósito.|
|Shakka|[TreatmentService]()|Python|Python é uma linguagem de programação de alto nível, a linguagem oferece recursos como tipagem dinâmica e forte, orientação a objetos, multiparadigmas, além de recursos poderosos em biblioteca padrão e via módulos e frameworks desenvolvidos pela comunidade, muito utilizada também na ciência de dados.| Python é uma boa ferramenta para tratar dados de forma mais efetiva, utilizando das bibliotecas pandas e numpy|
|William|[ModelService](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/model)|Python|Python é uma linguagem de programação de alto nível, a linguagem oferece recursos como tipagem dinâmica e forte, orientação a objetos, multiparadigmas, além de recursos poderosos em biblioteca padrão e via módulos e frameworks desenvolvidos pela comunidade, muito utilizada também na ciência de dados.|a|
|Mario|[NotifyService](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/notifyer)|Python|Python é uma linguagem de programação de alto nível, a linguagem oferece recursos como tipagem dinâmica e forte, orientação a objetos, multiparadigmas, além de recursos poderosos em biblioteca padrão e via módulos e frameworks desenvolvidos pela comunidade, muito utilizada também na ciência de dados.|Python foi utilizado, pois há bibliotecas que implementam alguns dos padrões de projetos conhecidos, como um obsever. A facilidade de uso de python bem como a implementação de algumas bibliotecas.|


## Executando o projeto 

Clone o respositório para a sua máquina e execute o comando abaixo: 

```
git clone https://github.com/willidert/auxilio-estudantil-microservice
```
Entre no projeto clonado: 
```
cd auxilio-estudantil-microservice/
```
Na raiz do projeto  digite: 
```
docker-compose up 
```
