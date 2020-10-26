PROJECT_NAME = darker

all:
	@echo "\n\n Compiling document \n\n"
	latex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex #See http://tex.stackexchange.com/questions/111410/compile-sequence-citing-in-the-glossary
	bibtex $(PROJECT_NAME)
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex

clean:
	@echo "\n\n\n*****Cleaning... *******"
	rm -f *.aux *.log *.ps *.toc *.lof *.lot *~ *.dvi *.bbl *.blg *.out *.glo *.ist *.acn *.acr *.gls *.alg *.glg *.bak
	rm -f $(PROJECT_NAME).pdf
