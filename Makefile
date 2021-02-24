
build:
	python convert_notations.py
	latexmk -pdf poly.tex
	lwarpmk pdftosvg imgs/*/*.pdf
	lwarpmk html
	python post_process.py 

clean:
	latexmk -c -pdf poly.tex
	lwarpmk cleanall
