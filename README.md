# aux_est_micro

## Iniciando o projeto

```
docker-compose up && docker-compose rm -fvs
```

## Preencher o formulário automaticamente.

### Esteja na pasta web/

```
./node_modules/.bin/cypress run --spec ./cypress/integration/1-getting-started/fill-the-form.spec.js --headed --no-exit
```
