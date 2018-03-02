'''
Created on Mar 1, 2018

@author: bk
'''
from gpp import GNU_Compiler, GNUExe, SharedLib, StaticLib

class CC(GNU_Compiler):
    def __init__(self):
        GNU_Compiler.__init__(self)
        self.cmdName = 'gcc'
        self.name = 'gnu_c'
        self.ext = ['c','C']
        self.exclude = []

class Exe(GNUExe,CC):
    def __init__(self):
        GNUExe.__init__(self)
        CC.__init__(self)
        self.name = 'gnu_c_exe'

class Shared(SharedLib,CC):
    def __init__(self):
        SharedLib.__init__(self)
        CC.__init__(self)
        self.options = ['fPIC']
        self.name = 'gnu_c_shared'

class Static(StaticLib,CC):
    def __init__(self):
        StaticLib.__init__(self)
        CC.__init__(self)
        self.name = 'gnu_c_static' 