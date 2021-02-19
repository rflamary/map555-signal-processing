
clean:
	latexmk -c -pdf poly.tex
	lwarpmk cleanall
build:
	latexmk -pdf poly.tex
	lwarpmk html
