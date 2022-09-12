# Desafio-RESTful-API-Capyba

## Como rodar

1. Clonar o repositório.

  * `git clone https://github.com/gustavopsm/Desafio-RESTful-API-Capyba.git`

2. Abrir o terminal e baixar as dependências:

  * Estão em requirements.txt

3. Criar o .env com o seguinte modelo para usar a função de enviar email de confirmação:

```
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

4. Agora, com as dependências baixadas, dar o start.

 * `python manage.py runserver`

5. Pronto! Agora você está rodando :D

## Como rodar os testes

1. Após realizar o procedimento do tópico Como rodar:

   * `python manage.py test {nome do app a ser testado}`
