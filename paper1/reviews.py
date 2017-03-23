from __future__ import print_function
import glob
import yaml
from pprint import pprint
import sys

readmes = glob.glob("*/README.rst")

def read_readme(filename):
    # print ("R", filename)
    data = {
        "title" : "TBD",
        "submitted" : "TBD",
        "author" : "TBD",
        "hid" : "TBD",
        "pages" : 1,
        }
    # print ("R", data)        
    with open(readme, 'r') as stream:
        for line in stream:
            # print ("L", line)
            line = line.replace("\n","")
            if line.startswith(":orphan:"): 
                pass
            elif ":" in line:
                (attribute, value) = line.split(":",1)
                value = value.replace('"', '').strip()
                data[attribute] = value
                
    return data
                
entries = []
for readme in readmes:
    # print (readme)
    entry = read_readme(readme)
    # print (entry)
    entries.append(entry)

# print (entries)    

print ("""
\\documentclass[12pt]{report}
\\usepackage{fullpage}
\\usepackage[final]{pdfpages}
\\begin{document}

\\title{Big Data Technologies}

\\author{Editor: Gregor von Laszewski}
\\maketitle

\\newpage

\section{Contributors}
""")

print("\\begin{footnotesize}")
print("\\begin{tabular}{|llll|}")
print("\\hline \\textbf{Name} & \\textbf{HID} & \\textbf{Title} & \\textbf{Pages}\\\\ \hline \hline")
for entry in entries:
    print (entry["author"], "&", entry["hid"], "&", entry["title"], "&", entry["pages"], "\\\\")
    print ("\\hline")
print("\\end{tabular}")
print("\\end{footnotesize}")

reports = glob.glob("*/report-review.pdf")

for report in reports:
    print ("\\includepdf[pages=-]{" + report + "}")


print("\\end{document}")

