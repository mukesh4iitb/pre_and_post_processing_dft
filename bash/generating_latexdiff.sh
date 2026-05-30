#!/bin/bash
# source: https://tex.stackexchange.com/questions/639807/latexdiff-and-achemso-not-showing-changes-to-the-title
# since latexdiff does not work with toprule, midrule, and bottomrule, So I need to delete that from the both old.tex and new.tex using sed -i '/midurle/' old.tex and so on.
# Here is my conversation with gemini: https://gemini.google.com/share/b0120090a1ff

sed -i '/midrule/d' old.tex
sed -i '/midrule/d' new.tex

sed -i '/toprule/d' old.tex
sed -i '/toprule/d' new.tex

sed -i '/bottomrule/d' old.tex
sed -i '/bottomrule/d' new.tex

latex -src -interaction=nonstopmode old.tex
bibtex old.aux
latex -src -interaction=nonstopmode old.tex
pdflatex -synctex=1 -interaction=nonstopmode old.tex
latex -src -interaction=nonstopmode new.tex
bibtex new.aux
latex -src -interaction=nonstopmode new.tex
pdflatex -synctex=1 -interaction=nonstopmode new.tex

latexdiff --exclude-textcmd="ce,midrule,toprule,bottomrule" --append-context1cmd="tabular,array" --enable-citation-markup old.bbl new.bbl > diff.bbl

latexdiff --exclude-textcmd="ce,midrule,toprule,bottomrule" --append-context1cmd="tabular,array" --enable-citation-markup old.tex new.tex > diff.tex
#latexdiff --append-context2cmd="\twocolumn,\abstract,\@twocolumnfalse,\title" old.bbl new.bbl > diff.bbl
#latexdiff --append-context2cmd="\twocolumn,\abstract,\@twocolumnfalse,\title" old.tex new.tex > diff.tex
latex -src -interaction=nonstopmode diff.tex
pdflatex -synctex=1 -interaction=nonstopmode diff.tex
