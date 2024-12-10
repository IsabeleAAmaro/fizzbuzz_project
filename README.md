# Implementação do FizzBuzz como REST API

API simples que gera a lista FizzBuzz com base no número fornecido, hospedada no endereço: https://fizzbuzz-project.onrender.com/

## Uso
URL do endpoint principal: https://fizzbuzz-project.onrender.com/api/fizzbuzz/

Método HTTP: POST

Formato de Requisição: JSON

Formato de Resposta: JSON

## Requisição
Para usar a API, envie uma requisição POST para o endpoint com o número n no corpo da requisição no formato JSON.

Exemplo de Requisição

```bash

curl -X POST https://fizzbuzz-project.onrender.com/api/fizzbuzz/ \
-H "Content-Type: application/json" \
-d '{"n": 15}'

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
