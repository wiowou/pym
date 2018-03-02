'''
Created on Nov 19, 2017

@author: 
'''
import pybaker as pb
import pybaker.nvidia.gnu as nv

if __name__ == '__main__':
    exe=nv.CUDA_Exe()
    exe.includeDir.append('inner')
    exe.libraryDir.append('.')
    exe.library = ['libadd.so']
    exe.ext = ['main.cpp']
    
    lib=nv.CUDA_Shared()
    lib.includeDir.append('inner')
    lib.exclude.append('main.cpp')
    
    targ1=pb.Target(name='test1',compiler=exe,makeFileName='test1.Makefile')
    targ1.sourceDir = '/home/bk/src/pybaker/UnitTests/cuda'
    
    targ3=pb.Target(name='libadd.so',compiler=lib,makeFileName='libadd.Makefile')
    targ3.sourceDir = '/home/bk/src/pybaker/UnitTests/cuda'
    
    targ3.build()
    targ1.build()
