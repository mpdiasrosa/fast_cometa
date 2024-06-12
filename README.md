# FastAPI do Zero - Notas de aula

**Link do material:** https://fastapidozero.dunossauro.com/

## Consultas rápidas

**pyenv** 3.1.1

**Poetry** (version 1.8.3)


## Aula 01 - Configurando o ambiente

### Instalando o pyenv para Windows T_T

**Guia para instalar o pyenv:** https://pyenv-win.github.io/pyenv-win/

```
$ pyenv --version
pyenv 3.1.1
```

```
$ pyenv update
$ pyenv install --list
``` 

Foi mencionado no material que poderia ocorrer um bug intermitente no Windows durante as instalações com *:latest* e ocorreu...

`$ pyenv install 3.12:latest` ❌

`$ pyenv install 3.12.4` ✅

## Instalando o Poetry

**Link para instalação do Poetry:** https://python-poetry.org/docs/#installation 


**Solução para o problema na instalação do Poetry:**
https://stackoverflow.com/questions/70003829/poetry-installed-but-poetry-command-not-found

`export PATH="$HOME/.poetry/bin:$PATH"` 


## Criação do Projeto FastAPI e Instalação das Dependências

`$ poetry new fast_zero`

`$ cd fast_zero`

`$ pyenv local 3.12.4` -> Gera o arquivo _.python-version_

Atualizar o arquivo `pyproject.toml` com a versão `python = "3.12.*" `

`$ poetry install` gera o ambiente venv

`poetry add fastapi` adiciona o fastAPI no venv


### Hello, World! 
Até q enfim....

`$ python -i fast_zero/app.py` - Rodando o app com o terminal interativo (REPL)

`poetry shell` - Habilita o ambiente virtual

`fastapi dev fast_zero/app.py` - iniciar servidor dev FastAPI da aplicação

A aplicação ficará disponível em: http://127.0.0.1:8000

Para parar a execução do FastAPI: `Ctrl+C`

**Uvicorn** - Servidor para disponibilizar a API e ser possível visualizar no navegador (ou outras aplicações clientes). É chamado automaticamente durante a execução do FastAPI.

## Outras ferramentas de desenvolvimento

**Ferramentas:** taskipy, pytest, ruff, httpx

`$ poetry add --group dev pytest pytest-cov taskipy ruff httpx`

`task lint` - informa sobre erros

`task format` - corrige o arquivo

`task test` - executa os testes

`task post_test` - 