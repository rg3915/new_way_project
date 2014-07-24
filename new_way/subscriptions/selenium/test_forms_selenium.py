# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from generate_random_values import *
from list_firstname import get_firstname
from list_lastname import get_lastname

# chrome = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
ffox = webdriver.Firefox()
ffox.get('http://localhost:8000/inscricao/')

nome = get_firstname()

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = ffox.find_element_by_id('id_firstname')
campo_busca.send_keys(nome)
campo_busca.send_keys(Keys.ENTER)  # Simular o ENTER

campo_busca = ffox.find_element_by_id('id_lastname')
campo_busca.send_keys(get_lastname())
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_cpf')
campo_busca.send_keys(str(generate_cpf()))
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_date_of_birth')
campo_busca.send_keys(generate_date())
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_email')
campo_busca.send_keys(nome.lower() + '@email.com')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_phone')
campo_busca.send_keys(str(generate_phone()))
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_cell')
campo_busca.send_keys(str(generate_cell()))
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_address')
campo_busca.send_keys('Rua Um, 100')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_complement')
campo_busca.send_keys('Apto 303')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_district')
campo_busca.send_keys('Centro')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_city')
campo_busca.send_keys('Sao Paulo')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_uf')
campo_busca.send_keys('SP')
campo_busca.send_keys(Keys.ENTER)

campo_busca = ffox.find_element_by_id('id_cep')
campo_busca.send_keys(str(generate_cep()))
