# Model Service

Serviço responsável pela predição do recebimento ou não do auxílio por um determidado aluno.

## Rodando o serviço

O projeto utiliza uma API REST implementada em [Flask](https://flask.palletsprojects.com/en/2.0.x/) que está na porta 5000.

```
python main.py
```

O serviço espera um `POST` com atributos do aluno no endpoint `/predicao/` e retorna um json `{'res': {resposta}}` contendo 1 para a aprovação e 0 para não aprovação.

O python permite o uso de [decoradores](https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/) para adicionar funcionalidades as funções que uso no endpoint.
