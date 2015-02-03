echo "Criando o templates"
mkdir core/templates
touch core/templates/base.html
touch core/templates/index.html
echo "criando a outras pastas"
mkdir core/templates/listas
mkdir core/templates/detalhes
mkdir core/templates/forms

touch core/templates/listas/veiculo_lista.html
touch core/templates/listas/marca_lista.html
touch core/templates/listas/kit_lista.html
touch core/templates/listas/acessorio_lista.html
touch core/templates/listas/concessionaria_lista.html

touch core/templates/detalhes/veiculo.html
touch core/templates/detalhes/kit.html
touch core/templates/detalhes/acessorio.html

touch core/templates/forms/veiculo_form.html

echo "criando static files"
mkdir core/static/img
mkdir core/static/css
mkdir core/static/js
tree