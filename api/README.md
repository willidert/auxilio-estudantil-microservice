# API
### Responsável: Mateus Bentes 

## Funcionalidade 

Esse serviço é responsável em receber o formulário enviado pelo frontend e armazenar em um banco de dados não relacional (MongoDB) e registrar na fila (RabbitMQ) para os demais serviços consumirem.  

Recebe o JSON no seguinte formato:

```json
{
  "email": "mateus.bentes@gmail.com",
  "questionEight": {
    "optionOne": "",
    "optionTwo": "",
    "optionThree": "Desempregado",
    "optionFour": "",
    "optionFive": "Trabalhador Autônomo (Há contribuição - MEI p.ex.)",
    "optionSix": "Pescador/agricultor familiar",
    "optionSeven": "",
    "optionEight": ""
  },
  "questionEighteen": "sim",
  "questionEleven": "Alugada",
  "questionFifteen": "nao",
  "questionFive": "Sim",
  "questionFour": "R$ 816,71 a 952,82",
  "questionFourteen": "nao",
  "questionNine": "renda até um salário",
  "questionNineteen": "nao",
  "questionOne": "nao",
  "questionSeven": "4 ou mais membros",
  "questionSeventeen": "sim",
  "questionSix": "Dependente financeiramente dos pais",
  "questionSixteen": "sim",
  "questionTen": "Sim, no mesmo município do campus",
  "questionThirteen": "1 a 2 conduções",
  "questionThree": "nao",
  "questionTwelve": "transporte Público",
  "questionTwenty": "3",
  "questionTwentyOne": "Ensino Superior",
  "questionTwentyTwo": "Ensino Superior",
  "questionTwo": "sim"
}
```

Guarda no Banco de Dados (MongoDB): 
![Dados no MongoDB](https://cdn.discordapp.com/attachments/640981909777940521/866513446454165534/unknown.png)

E Registra no RabbitMQ: 
![image](https://user-images.githubusercontent.com/36206555/126096366-94a8760d-b15f-45ba-a18a-ad1ecce22128.png)

## Design Patterns utilizados 

### Singleton 

Em Javascript/Typescript é possível exportar uma única instância que vai ser utilizada em toda a aplicação. Ele faz isso de uma forma diferente do que o GoF declara, porém o funcionamento é o mesmo. Ex.: 

![carbon(2)](https://user-images.githubusercontent.com/36206555/126096719-09ffe19f-52aa-418d-b8a0-8ddfa420a41d.png)


