from setuptools import setup, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import os
import numpy
from io import open
import glob

def returnPyxFiles(path):
    l = []
    for i in os.listdir(path):
        if i.endswith(".pyx") or i.endswith(".c") or i.endswith(".pxd"):
            l.append(path+i)
    return l

def returnPxdFiles(path):
    l = []
    for i in os.listdir(path):
        if i.endswith(".pxd") or i.endswith(".c"):
            l.append(path+i)
    return l

def makeExtensions(path):
    extensions = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith(".pyx"):
                moduleFiles = [] 
                moduleFiles.append(root+'/'+file)
                if root+'/'+(file.split('.')[0]+'.pxd') in glob.glob(root+"/*.pxd"):
                    moduleFiles.append(root+'/'+(file.split('.')[0]+'.pxd'))
                pathWithFile = root+'/'+file.split('.')[0]
                moduleName = pathWithFile.replace('/','.')
                extensions.append(Extension(moduleName,moduleFiles,include_dirs=[numpy.get_include(),'./PyBoltz/','./PyBoltz/C/']))
    return extensions
extensions = makeExtensions('PyBoltz')

setup(
    ext_modules = cythonize(extensions),
    extra_compile_args=["-Wno-int-conversion"],
    cmdclass={'build_ext': build_ext}
)

