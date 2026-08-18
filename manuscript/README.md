# Manuscript build

The canonical source is `qls6_cardinality_29.tex`.

With a standard TeX Live installation:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error qls6_cardinality_29.tex
```

The bibliography is in `references.bib`.

The committed PDF is a convenience artifact for readers. Mathematical verification does not trust the PDF; the exact certificate and verification programs are the machine-checkable release artifacts.
