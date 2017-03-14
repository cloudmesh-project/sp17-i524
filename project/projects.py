from __future__ import print_function
import glob
import yaml
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


\\begin{document}

\\title{Big Data Technologies}

\\author{Editor: Gregor von Laszewski}
\\maketitle

\\newpage
\\tableofcontents
\\newpage

\section{Contributors}
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

