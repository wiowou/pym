import os

from make.compiler import Compiler

class Source(object):
    def __init__(self,name,compiler=Compiler(),outputDir='',idsuff=''):
        self.compiler = compiler
        self.name = name
        self.outputDir = outputDir
        self.idsuff = idsuff
    
    def __str__(self):
        s = self.objName() + ' : ' + self.name
        header = self.compiler.headerDep()
        for h in header:
            s += ' ' + h
        s += '\n'
        s += '\t' + self.compiler._sourceToObjectCommand_(self.objName(), self.name) + '\n'
        return s
    
    def id(self):
        name = os.path.basename(self.name)
        i = name.split('.')[0] + self.idsuff
        return i
    
    def objName(self):
        o = self.id() + '.o'
        outputDir = self.outputDir
        if (outputDir == ''):
            outputDir = 'ob'
        return os.path.join(outputDir,o)