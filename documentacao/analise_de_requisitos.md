Análise de Requisitos
=====================

Funcionalidades
---------------

- Cadastro
	- Cadastrar o Interessado
	- Cadastrar os carros
	- Cadastrar as concessionárias
	- Cadastrar o vendedor
- Compra
	- Escolher a marca
	- Escolher o modelo
	- Escolher os acessórios do carro (máx. 5 itens)
	- Fazer o pedido de compra
	- Imprimir o pedido
	- Enviar o pedido por e-mail
- Relatórios
	- Pedido de compra
	- Veículos mais consultados por faixa de idade
	- Veículos mais consultados por região
	- Veículos mais vendidos por mês ou por semestre

Itens do projeto
----------------

templates/

	base.html

	index.html

	listas/

		veiculo_lista.html

		marca_lista.html

		kit_lista.html

		acessorio_lista.html

		concessionaria_lista.html

	detalhes/

		veiculo.html

		kit.html

		acessorio.html

	forms/

		veiculo_form.html


static/

	css

	img

	js

admin

	lista de tabelas

		lista de registros

			detalhes do registro

LISTAR TODAS AS TABELAS DO ADMIN.

Cenários
--------

Cenário 01

Dado que temos um interessado, quando ele acessa o endereço ``/inscricao/`` ele vê a página de inscrição e a página possui **um formulário**, e o formulário possui **14 campos** e os campos são:

nome, sobrenome, cpf, data_nasc, email, tel, cel, endereco, complemento, bairro, cidade, uf, cep, criado_em

firstname, lastname, cpf, date_of_birth, email, phone, cell, address, complement, district, city, uf, cep, created_at, 

e o formulário possui **um botão** para inscrever.



Outros
------

Navegação Estrutural (breadcrumb):
	Início > Cadastro > Nomes > Regis

