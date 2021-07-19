## Responsável: Mario Guilherme Carvalho

## Funcionalidades e Padrões de Projetos 
O notifyer tem como objetivo observar o banco de dados e a partir da inserção do resultado definido pelo modelo, Aprovado ou Reprovado 
notificar o usuário sobre a situação do seu auxílio.

Utilizou-se o padrão de projeto Singleton para ter apenas uma conexão com o banco de dados em database.py

E seria utilizado um Observer para detectar mudanças e notificar os usuário em email_notifyer.py

