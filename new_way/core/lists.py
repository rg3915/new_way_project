""" List of values for use in choices in models. """

gender_list = [('M', 'masculino'), ('F', 'feminino')]

treatment_list = (
    ('a', 'Arq.'),
    ('aa', 'Arqa.'),
    ('d', 'Dona'),
    ('dr', 'Dr.'),
    ('dra', 'Dra.'),
    ('e', 'Eng.'),
    ('ea', u'Engª.'),
    ('p', 'Prof.'),
    ('pa', 'Profa.'),
    ('sr', 'Sr.'),
    ('sra', 'Sra.'),
    ('srta', 'Srta.'),
)

type_address_list = (
    ('i', 'indefinido'),
    ('c', 'comercial'),
    ('r', 'residencial'),
    ('o', 'outros'),
)

uf_list = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', 'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Brasília'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', 'Tocantins'),
)

type_phone_list = (
    ('pri', 'principal'),
    ('com', 'comercial'),
    ('res', 'residencial'),
    ('cel', 'celular'),
    ('cl', 'Claro'),
    ('oi', 'Oi'),
    ('t', 'Tim'),
    ('v', 'Vivo'),
    ('n', 'Nextel'),
    ('fax', 'fax'),
    ('o', 'outros'),
)

fueltype_list = (
    ('g', 'gasolina'),
    ('a', 'álcool'),
    ('d', 'diesel'),
    ('f', 'flex'),
    ('e', 'elétrico'),
)

transmissiontype_list = (
    ('a', 'automático'),
    ('m', 'manual'),
)

status_list = (
    ('c', 'cancelado'),
    ('p', 'pendente'),
    ('a', 'aprovado'),
)
