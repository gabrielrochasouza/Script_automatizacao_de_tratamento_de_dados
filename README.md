# Script Python para Automatização de leitura de dados de csv para tratamento de dados


## Sobre o projeto:

Este projeto foi desenvolvido para o teste técnico de back end da empresa Cognitivo. E tem como objetivo ler uma arquivo csv que possui inúmeras linhas, e tratar os dados, criando um output com 3 arquivos sendo eles do tipo: json, csv e um banco de dados local.

Além disso, foram feitas consultas na api v2 do Twitter para consultar o número de citações (nos últimos 7 dias) das aplicação com maior número de avaliações.

## Tecnologias utilizadas:

- Python
- Pandas
- ipdb (para debugar o código)
- pytwitter
  
## Comandos para iniciar o projeto:
```
python -m venv venv 
(Cria pasta venv para ter um ambiente isolado)

source venv/bin/activate
(Para ativar o ambiente virtual isolado) 

pip install -r requirements.txt
(Instala as dependências utilizadas no projeto)

python main.py
(Para rodar o script)
```

### Comando de uma linha para iniciar:
```
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python main.py
```

<br>
<br>
<img src="./print_do_teste.png" alt="Print do teste" />

