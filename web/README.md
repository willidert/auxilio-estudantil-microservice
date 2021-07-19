# Web 

#### Responsável: Mateus Bentes Marreira

## Funcionalidade 

Neste serviço foi implementado a funcionalidade de formuário que o usuário vai preencher no frontend. O formulário tem a seguinte aparência com vários campos para serem preenchidos. 

![Imagem do formuário](https://cdn.discordapp.com/attachments/640981909777940521/866495811109126154/unknown.png)

Ele irá enviar um JSON com os dados do aluno e será mandado para a [API](https://github.com/willidert/auxilio-estudantil-microservice/tree/main/api). Por exemplo: 

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

## Design Patterns utilizados 

### Injeção de Dependência 
Angular nos provê uma forma fácil de injetar as dependencias entre nossos componentes, essa feature é algo nativo do próprio angular **para nos trazer mais produtividade no desenvolvimento e manter em baixo nível o acoplamento entre os módulos**. Angular cria uma instância de Logger para o nosso componente através do construtor por baixo dos panos. Nosso papel é apenas utilizá-lo. Ex.: 
![Injeção de Dependência](https://cdn.discordapp.com/attachments/640981909777940521/866503310432010250/carbon1.png)
