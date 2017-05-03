import os

class classFileWrite:
    fileobj = None
    directory = "./benchmark"
    fpath = directory + "/test.txt"

    def __init__(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.openfile()

    def openfile(self):
        self.fileobj = open(self.fpath, "a")

    def writeline(self):
        line = "=" * 60
        line=line+"\n"
        self.fileobj.write(line)

    def writelog(self,logstr=""):
        self.fileobj.seek(0,0)
        logstr = logstr+"\n"
        self.fileobj.write(logstr)

    def closefile(self):
        self.fileobj.close()

