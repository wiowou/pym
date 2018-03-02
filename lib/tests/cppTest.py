from make import Target
from make.compiler.gpp import Exe as gppExe
from make.compiler.gpp import Shared as gppShared

if __name__ == '__main__':
    exe=gppExe()
    exe.includeDir.append('inner')
    exe.libraryDir.append('.')
    exe.library = ['libadd.so']
    
    lib=gppShared()
    lib.includeDir.append('inner')
    print(str(lib))
    
    targ1=Target(name='test1',compiler=exe)
    print(str(targ1))
    
    targ3=Target(name='libadd.so',compiler=lib)
    print(str(targ3))
