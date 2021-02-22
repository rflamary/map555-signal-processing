
build:
	latexmk -pdf poly.tex
	lwarpmk html
	python post_process.py 


clean:
	latexmk -c -pdf poly.tex
	lwarpmk cleanall
