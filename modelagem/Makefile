pdf_modelagem:
	latexmk -pdf modelagem02
	latexmk -c
	convert -density 300 modelagem02.pdf modelagem02.jpg
	ls -la
preview_modelagem:
	subl modelagem02.tex &
	evince modelagem02.pdf &
	latexmk -pdf -pvc modelagem02
pdf_tabelas:
	latexmk -pdf tabelas
	latexmk -c
	convert -density 300 tabelas.pdf tabelas.jpg
	ls -la
preview_tabelas:
	subl tabelas.tex &
	evince tabelas.pdf &
	latexmk -pdf -pvc tabelas
