all: paper.pdf

paper.pdf: $(wildcard *.tex secs/*.tex figs/*.pdf figs/*.png)
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	rm -f paper.aux paper.log paper.bbl paper.blg paper.brf

wc: paper.pdf
	./wordcount.pl

clean:
	-rm -f paper.aux paper.log paper.bbl paper.blg paper.brf paper.dvi paper.txt paper.pdf
