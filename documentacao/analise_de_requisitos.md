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

- templates/
	- base.html
	- index.html
	- listas/
		- veiculo_lista.html
		- marca_lista.html
		- kit_lista.html
		- acessorio_lista.html
		- concessionaria_lista.html
	- detalhes/
		- veiculo.html
		- kit.html
		- acessorio.html
	- forms/
		- subscription_form.html
		- veiculo_form.html

- static/{css, img, js}

- admin
	- lista de tabelas
		- lista de registros
			- detalhes do registro

LISTAR TODAS AS TABELAS DO ADMIN.

Cenários
--------

Cenário 01
^^^^^^^^^^

Dado que temos um interessado, quando ele acessa o endereço ``/inscricao/`` ele vê a página de inscrição e a página possui **um formulário**, e o formulário possui **14 campos** e os campos são:

nome, sobrenome, cpf, data_nasc, email, tel, cel, endereco, complemento, bairro, cidade, uf, cep, criado_em

firstname, lastname, cpf, date_of_birth, email, phone, cell, address, complement, district, city, uf, cep, created_at, 

e o formulário possui **um botão** para inscrever.

Cenário 02
^^^^^^^^^^

Dado que um interessado acessa ``/inscricao/``

Quando ele preenche o formulário e seus dados estão corretos e ele clica em Cadastrar

Então o sistema salva sua inscrição e o redireciona para a página de sucesso.

Cenário 03
^^^^^^^^^^

Dado que um interessado acessa ``/inscricao/``

Quando ele preenche o formulário e seus dados estão incorretos e ele clica em Cadastrar

Então o sistema não salva sua inscrição e exibe a própria página do formulário e indica os campos com erro.



Outros
------

Navegação Estrutural (breadcrumb):
	Início > Cadastro > Nomes > Regis

