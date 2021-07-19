# Model Service

Serviço responsável pela predição do recebimento ou não do auxílio por um determidado aluno. O projeto consome os dados da mensageria, enviados pelo serviço de limpeza e salva a predição no mongodb.

## Padrões utilizados

Implementei um singleton básico no database.py para gerenciar a conexão com o mongodb, isso evita que várias conexões sejam abertas em paralelo desperdiçando recursos.

Também há um singleton no model.py para que haja apenas uma instância do modelo em execução.
