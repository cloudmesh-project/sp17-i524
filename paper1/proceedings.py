from __future__ import print_function
import glob
import yaml


readmes = glob.glob("*/README.rst")


def read_readme(filename):
    data = {
        "title" : "TBD",
        "submitted" : "TBD",
        "author" : "TBD",
        "hid" : "TBD",
        "pages" : 1,
        }
    with open(readme, 'r') as stream:
        for line in stream:
            line = line.replace("\n","")
            if line.startswith(":orphan:"): 
                pass
            elif ":" in line:
                (attribute, value) = line.split(":")
                value = value.replace('"', '').strip()
                data[attribute] = value
                
    return data
                
entries = []
for readme in readmes:
    entry = read_readme(readme)
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

reports = glob.glob("*/report.pdf")

for report in reports:
    print ("\\includepdf[pages=-]{" + report + "}")


print("\\end{document}")
