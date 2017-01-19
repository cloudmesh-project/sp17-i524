Report Format
=============

This is a template that can be used for all papers in the class. Please note that we may update this template and it is your responsibility to check if your report follows the format.

To begin with a paper, you need to copy the template files into the directory where your paper will reside. For example, if you're working on `paper-1` and your HID is SP17-TS-0001, you will need to do this from the top level directory of your repository:

  mkdir paper1/SP17-TS-0001
  cp -r paper_template/* paper1/SP17-TS-0001

Assuming you have LaTeX installed on your system, then you can go into your paper directory and compile the LaTeX code using `make`:

  cd paper1/SP17-TS-0001
  make

`make` is a tool that automates builds by issuing a set of commands place in a `Makefile`. If you look at the Makefile that came with the template, you will find that the above command executed four other commands to compile the LaTeX code: `pdflatex`, followed by `bibtex`, followed by `pdflatex`, followed by `pdflatex` again. These commands compile the file `report.tex` into `report.pdf` making sure that the references defined in `references.bib` are properly resolved and included in the final PDF.

To view the generated report, you can execute the `view` target in the Makefile:

  make view

The process of compiling the LaTeX code generates a number of auxiliary files you will find in your paper directory. These can be removed with:

  make clean

Take a look at the other targets in the Makefile to see if you can figure out what they do.

If you didn't install LaTeX on your machine, but are using an online LaTeX environment like ShareLaTeX, this process will be different. Please, refer to the documentation for your environment.
