# Model Service

Serviço responsável por predizer o recebimento ou não do auxílio por um determidado aluno. O projeto consome os dados da fila `model`, enviados pelo serviço de limpeza, realiza a predição e atualiza o status do aluno no banco de dados.

## Padrões utilizados

Implementei um singleton básico no [singleton.py](https://github.com/willidert/auxilio-estudantil-microservice/blob/main/model/singleton.py) que uso para gerenciar a conexão com o mongodb, isso evita que várias conexões sejam abertas em paralelo desperdiçando recursos. Também há um singleton no model.py para que haja apenas uma instância do modelo em execução.

![Singleton](https://media.discordapp.net/attachments/640981909777940521/874833411494256660/unknown.png?width=853&height=453)
