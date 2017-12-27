
def latex_compile(fname,with_bib=False,full=False):
    from subprocess import call
    call(['pdflatex',fname])
    if with_bib:
        call(['bibtex',fname])
        if full:
            call(['pdflatex',fname])
    if full:
        call(['pdflatex',fname])
def replace_bib(fname,inplace=False,pdf=False):
    latex_compile(fname,with_bib=True)
    with open(fname+'.tex','r') as f:
        tex = f.read()
    with open(fname + '.bbl','r') as f:
        bib = f.read()
    first_split = tex.split(r'\bibliography{')
    if len(first_split) > 1:
        first_half = first_split[0]
        second_half = '}'.join(first_split[1].split('}')[1:])
        newtex = first_half + bib + second_half
    else:
        newtex = tex

    output = fname
    if not inplace:
        output += '_out'
    with open(output+'.tex','w') as f:
        f.write(newtex)
    if pdf:
        latex_compile(output,full=True)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Store the references directly in the tex file.')
    parser.add_argument('--file', type=str, default='main',
            help='The main filename.')
    parser.add_argument('--inplace', action='store_true',dest='inplace',
            help='Overwrite the input file.')
    parser.add_argument('--pdf', dest='pdf',action='store_true',
            help='Compile the final tex file to a pdf.')
    args = parser.parse_args()
    print(args)

    fname = args.file
    if '.tex' in fname:
        fname = fname.split('.tex')[0]

    replace_bib(fname, pdf=args.pdf, inplace=args.inplace)


