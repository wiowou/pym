'''
Created on Feb 3, 2018

@author: bk
'''
from make.compiler import Compiler

class NVCC(Compiler):
    def __init__(self):
        Compiler.__init__(self)
        self.cmdName = 'nvcc'
        self.name = 'nvidia-cuda-compiler'
        self.options = ''
        self.ext = ['cu','CU','cpp','cxx','CPP','CXX','cc','c++','C','c']
        self.compilationMethod = ' -dc'

    def _sourceToObjectCommand_(self,objFileName,srcName):
        opt = ' ' + self.options
        idir = ''
        for i in self.includeDir:
            idir += ' -I' + i
        return self.cmdName + self.compilationMethod + idir + opt + ' -o ' + objFileName + ' ' + srcName
    
    def _findIncludeFiles_(self, srcName):
        idep = []
        with open(srcName,'r') as f:
            for line in f:
                line = line.strip()
                if ('#include ' in line):
                    words = line.split()
                    i = words[1].strip()
                    i = i[1:-1]
                    idep.append(i)
        return idep
    
    def separateUnitCompilation(self):
        self.compilationMethod = ' -dc'
    
    def singleUnitCompilation(self):
        self.compilationMethod = ' -c'

class Exe(NVCC):
    def __init__(self):
        NVCC.__init__(self)
        self.name = 'nvidia-cuda-exe'
        self.includeDir = []
        self.libraryDir = []
        self.library = [] #examples are libadd.so, libadd.a
        self.options = ''

    def _buildCommand_(self,objNames,targetName):
        sharedLibrary = [e for e in self.library if e[-3:] == '.so']
        staticLibrary = [e for e in self.library if e[-2:] == '.a']
        opt = ' ' + self.options
        objects = ' '
        for o in objNames:
            objects += ' ' + o
        ldir = ''
        for l in self.libraryDir:
            ldir += ' -L' + l
        idir = ''
        j = 0
        for i in self.includeDir:
            if (j == 0):
                idir += ' -I' + i
            else:
                idir += ',' + i
        libso = ' '
        if len(sharedLibrary) > 0 and len(staticLibrary) > 0:
            libso = " --compiler-options '-Wl,-Bdynamic'"
        for l in sharedLibrary:
            libso += ' -l' + l[3:-3]
        liba = ''
        if len(staticLibrary) > 0:
            liba = " --compiler-options '-Wl,-Bstatic'"
            if (len(sharedLibrary) == 0):
                liba = ' -static'
        for l in staticLibrary:
            liba += ' -l' + l[3:-2]
        return self.cmdName + opt + objects + ' -o ' + targetName + ldir + idir + liba + libso

class Shared(NVCC):
    def __init__(self):
        NVCC.__init__(self)
        self.name = 'nvidia-cuda-shared'
        self.options = "-compiler-options '-fPIC' "
        self.includeDir = []
        self.libraryDir = []
        self.library = []
        self.options = ''

    def _buildCommand_(self,objNames,targetName):
        opt = ' --shared ' + self.options
        objects = ' '
        for o in objNames:
            objects += ' ' + o
        ldir = ''
        for l in self.libraryDir:
            ldir += ' -L' + l
        idir = ''
        for i in self.includeDir:
            idir += ' -I' + i
        lib = ''
        if (len(self.library) > 0):
            lib = "--compiler-options '-Wl,--whole-archive'"
        for l in self.library:
            lib += ' -l' + l
        if (len(self.library) > 0):
            lib += "--compiler-options '-Wl,--no-whole-archive'"
        return self.cmdName + opt + objects + ' -o ' + targetName + ldir + idir + lib

class Static(NVCC):
    def __init__(self):
        NVCC.__init__(self)
        self.name = 'nvidia-cuda-archiver'
        self.options = '--lib'

    def _buildCommand_(self,objNames,targetName):
        opt = ' ' + self.options
        objects = ' '
        for o in objNames:
            objects += ' ' + o
        return 'nvcc' + opt + ' ' + targetName + objects

class HostLinkObject(NVCC):
    def __init__(self):
        NVCC.__init__(self)
        self.name = 'nvidia-cuda-host-link-object'
        self.options = '--device-link'

    def _buildCommand_(self,objNames,targetName):
        opt = ' ' + self.options
        objects = ' '
        for o in objNames:
            objects += ' ' + o
        return 'nvcc' + opt + ' -o ' + targetName + objects
