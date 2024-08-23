# Validador Documentos - BR

Descrição. 
O pacote validador_documentos_br é utilizado para validar alguns documentos comuns no Brasil:
	- CPF (Cadastro de Pessoa Física)
	- CNPJ (Cadastro de Pessoa Jurídica)
	- PIS (Cadastro no INSS)
	- RENAVAM (Cadastro de veículos)

## Instalação

Use o gerenciadaor de pacotes  [pip](https://pip.pypa.io/en/stable/) para instalar validador_documentos_br

```bash
pip install validador_documentos_br
```

## Utilização

```python
from validador_documentos_br import cpf
cpf.validar_cpf(<<CPF a ser validado>>)
```

## Autor
Daniel BINS

## License
[MIT](https://choosealicense.com/licenses/mit/)
