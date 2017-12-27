# BibRemove
Remove a .bib file from a latex project. This replaces a \bibliography{references.bib} call with the contents of the .bbl file.

Usage:

To remove the .bib dependence of your main.tex file, simply use
```python
python bibremove.py --file main
```
The new tex file will be stored in main_out.tex

You can also overwrite the original file,
```python
python bibremove.py --file main --inplace
```
And have it compile the final tex file to pdf,
```python
python bibremove.py --file main --inplace --pdf
```
