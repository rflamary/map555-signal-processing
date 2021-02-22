
build:
	latexmk -pdf poly.tex
	lwarpmk html


clean:
	latexmk -c -pdf poly.tex
	lwarpmk cleanall
