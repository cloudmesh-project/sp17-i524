#
# run in python2
#
from __future__ import print_function
import glob
from ruamel import yaml
from pprint import pprint
import sys
import re

readmes = glob.glob("*/README.rst")

def readfile(filename):
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content

def read_readme(filename):
    # print ("R", filename)
    data = {
        "title" : "TBD",
        "textitle" : "TBD",
        "submitted" : "TBD",
        "author" : "TBD",
        "texauthor": "TBD",
        "hid" : "TBD",
        "pages" : 1,
        "id": filename.replace("/README.rst",""),
        "tex": filename.replace("README.rst","report/report.tex"),
        "pdf": filename.replace("README.rst","report/report.pdf")       
        }
    # print ("R", data)        
    with open(readme, 'r') as stream:
        for line in stream:
            # print ("L", line)
            line = line.replace("\n","")
            if line.startswith(":orphan:"): 
                pass
            elif ":" in line:
                (attribute, value) = line.split(":", 1)
                value = value.replace('"', '').strip()
                data[attribute] = value

     # FIND TITLE IN TEX FILE
    document = readfile (data["tex"])
    try:
        match = re.search(r'title\{.*\}', document, re.MULTILINE)
        title = match.group(0)
        title = title.replace("title{","")
        title = title.replace('}',"")
        if "LaTeX" in title:
            title = "Not Submitted"
        data["textitle"] = title
        
    except:
        pass

    # FIND AUTHOR IN TEX FILE

    authors = ""
    # print (document)
    for line in document.split("\n"):
        if "\\author" in line:
            authors = authors + line.split("{")[1].replace("}",", ")
    data["texauthor"] = authors[:-2]
    if data["texauthor"].startswith("John Smith, "):
        data["texauthor"] = "Author Missing"
    return data


entries = {}
for readme in readmes:
    id = readme.replace("/README.rst", "")
    entry = read_readme(readme)
    # print (entry)
    entries[id] = entry

# pprint(entries)    
# sys.exit()    

# print (entries)    


titlepagemacro = '''
\\usepackage{amsmath}
\\usepackage{tikz}
\\usepackage{epigraph}
\\usepackage{lipsum}

\\renewcommand\\epigraphflush{flushright}
\\renewcommand\\epigraphsize{\\normalsize}
\\setlength\\epigraphwidth{0.7\\textwidth}

\\definecolor{titlepagecolor}{cmyk}{1,.60,0,.40}

\\DeclareFixedFont{\\titlefont}{T1}{ppl}{b}{it}{0.5in}

\\makeatletter                       
\\def\\printauthor{%                  
    {\\large \\@author}}              
\\makeatother
\\author{%
    Editor: \\\\
    Gregor von Laszewski\\\\
    Department of Intelligent Systems Engeneering\\\\
    Indiana University \\\\
    \\texttt{laszewski@gmail.com}\\vspace{20pt} \\\\   
    }

% The following code is borrowed from: http://tex.stackexchange.com/a/86310/10898

\\newcommand\\titlepagedecoration{%
\\begin{tikzpicture}[remember picture,overlay,shorten >= -10pt]

\\coordinate (aux1) at ([yshift=-15pt]current page.north east);
\\coordinate (aux2) at ([yshift=-410pt]current page.north east);
\\coordinate (aux3) at ([xshift=-4.5cm]current page.north east);
\\coordinate (aux4) at ([yshift=-150pt]current page.north east);

\\begin{scope}[titlepagecolor!40,line width=12pt,rounded corners=12pt]
\\draw
  (aux1) -- coordinate (a)
  ++(225:5) --
  ++(-45:5.1) coordinate (b);
\\draw[shorten <= -10pt]
  (aux3) --
  (a) --
  (aux1);
\\draw[opacity=0.6,titlepagecolor,shorten <= -10pt]
  (b) --
  ++(225:2.2) --
  ++(-45:2.2);
\\end{scope}
\\draw[titlepagecolor,line width=8pt,rounded corners=8pt,shorten <= -10pt]
  (aux4) --
  ++(225:0.8) --
  ++(-45:0.8);
\\begin{scope}[titlepagecolor!70,line width=6pt,rounded corners=8pt]
\\draw[shorten <= -10pt]
  (aux2) --
  ++(225:3) coordinate[pos=0.45] (c) --
  ++(-45:3.1);
\\draw
  (aux2) --
  (c) --
  ++(135:2.5) --
  ++(45:2.5) --
  ++(-45:2.5) coordinate[pos=0.3] (d);   
\\draw 
  (d) -- +(45:1);
\\end{scope}
\\end{tikzpicture}%
}
'''

titlepage = '''
\\begin{titlepage}

\\noindent
\\titlefont Projects in Big Data \\\\ Software and Applications\\par
\\epigraph{Spring 2017}%
{\\textit{Bloomington, Indiana}}
\\null\\vfill
\\vspace*{1cm}
\\noindent
\\hfill
\\begin{minipage}{0.50\\linewidth}
    \\begin{flushright}
        \\printauthor
    \\end{flushright}
\\end{minipage}
%
\\begin{minipage}{0.02\\linewidth}
    \\rule{1pt}{125pt}
\\end{minipage}
\\titlepagedecoration
\\end{titlepage}
'''

print ("""
\\documentclass[12pt]{article}
\\usepackage{fullpage}
\\usepackage[final]{pdfpages}
\\usepackage{hyperref}
\usepackage{tocloft}
\\renewcommand\\cftsecafterpnum{\\vskip0pt}
\\renewcommand\\cftsubsecafterpnum{\\vskip0pt}

% Adjust sectional unit title fonts in ToC
\\renewcommand{\\cftsecfont}{\\sffamily}
\\renewcommand{\\cftsubsecfont}{\\sffamily}
""")

print(titlepagemacro)

print("""

\\textheight=23.5cm

\\begin{document}
%\\title{Big Data Technologies}

%\\author{Editor: Gregor von Laszewski}

""")

print(titlepage)

print("""

%\\maketitle

\\newpage
\\tableofcontents
\\newpage

% \section{Contributors}
""")

'''
print("\\begin{footnotesize}")
print("\\begin{tabular}{|llll|}")
print("\\hline \\textbf{Name} & \\textbf{HID} & \\textbf{Title} & \\textbf{Pages}\\\\ \hline \hline")
for id in entries:
    enrty = entries[id]
    print (entry["author"], "&", entry["hid"], "&", entry["title"], "&", entry["pages"], "\\\\")
    print ("\\hline")
print("\\end{tabular}")
print("\\end{footnotesize}")

print ("\\newpage")
'''

#reports = glob.glob("*/report/report.pdf")
reports = glob.glob("*/report/report.tex")

for report in reports:
    id = report.replace("/report/report.tex","")
    # print ("%", entries[id])
    
    document = readfile (report)
    pdf = report.replace(".tex",".pdf")
    title = report
   

    print("\\addtocounter{section}{1}")
    print("\\addcontentsline{toc}{section}{\\arabic{section} ",
              id + "\\newline",
              entries[id]["textitle"],"\\newline",
              entries[id]["texauthor"],
              "}")

    
    if not "Template for Preparing a Paper or Report for I524" in document:
        print ("\\includepdf[pages=-,pagecommand=\\thispagestyle{plain}]{" + pdf + "}")
    else:
        print("{\\Large", pdf, "not submitted}\\newpage")
    print ("")
print("\\end{document}")

