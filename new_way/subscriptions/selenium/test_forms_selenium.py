# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from generate_random_values import *
from list_cep import get_cep
from list_email import get_email
from cep import Correios
import names

# chrome = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
ffox = webdriver.Firefox()
ffox.get('http://localhost:8000/inscricao/')

fname = names.get_first_name()
lname = names.get_last_name()
email = fname.lower() + get_email()

ncep = get_cep()
c = Correios()
r = c.consulta(ncep, primeiro=True)

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = ffox.find_element_by_id('id_firstname')
campo_busca.send_keys(fname)

campo_busca = ffox.find_element_by_id('id_lastname')
campo_busca.send_keys(lname)

campo_busca = ffox.find_element_by_id('id_cpf')
campo_busca.send_keys(str(generate_cpf()))

campo_busca = ffox.find_element_by_id('id_date_of_birth')
campo_busca.send_keys(generate_date())

campo_busca = ffox.find_element_by_id('id_email')
campo_busca.send_keys(email)

campo_busca = ffox.find_element_by_id('id_phone')
campo_busca.send_keys(str(generate_phone()))

campo_busca = ffox.find_element_by_id('id_cell')
campo_busca.send_keys(str(generate_cell()))

campo_busca = ffox.find_element_by_id('id_address')
campo_busca.send_keys(r['Logradouro'])

campo_busca = ffox.find_element_by_id('id_complement')
campo_busca.send_keys('Apto xyz')

campo_busca = ffox.find_element_by_id('id_district')
campo_busca.send_keys(r['Bairro'])

campo_busca = ffox.find_element_by_id('id_city')
campo_busca.send_keys(r['Localidade'])

campo_busca = ffox.find_element_by_id('id_uf')
campo_busca.send_keys(r['UF'])

campo_busca = ffox.find_element_by_id('id_cep')
campo_busca.send_keys(r['CEP'])

# campo_busca.send_keys(Keys.ENTER)  # Simular o ENTER
