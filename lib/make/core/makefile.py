import os
import shutil

class Makefile():
    def __init__(self,name=''):
        self.name = name
        self.target = []
    
    def write(self):
        source = {}
        compiler = {}
        name = self.name
        if (self.name == ''):
            name = 'Makefile'
        allStr = 'all : '
        for t in self.target:
            allStr += t.callName() + ' '
            compiler[t.compiler.name+t.compiler.options] = t.compiler
            for s in t.source:
                source[s.id()] = s
                compiler[s.compiler.name+s.compiler.options] = s.compiler
        fout = open(name,'w')
        for c in compiler.values():
            fout.write(str(c)+'\n')
        fout.write('\n')
        fout.write(allStr+'\n\n')
        for t in self.target:
            fout.write(str(t)+'\n')
        fout.write('\n')
        for s in source.values():
            fout.write(str(s)+'\n')
        cleanStr = 'clean : \n'
        if (os.name == 'nt'):
            cleanStr += '\trmdir \s ob\n'
        else:
            cleanStr += '\trm -r ob\n'
        cleanStr += '\tmkdir ob\n'
        cleanallStr = 'cleanall : clean\n'
        for t in self.target:
            cleanallStr += '\trm ' + t.name + '\n'
        fout.write(cleanStr+'\n')
        fout.write(cleanallStr+'\n')
        fout.close()
        if (not os.path.exists('ob')):
            os.makedirs('ob')
        if (os.path.exists('__pycache__')):
            shutil.rmtree('__pycache__',True)
    
    def find(self,targName):
        for t in self.target:
            if (t.name == targName):
                return t
        return None