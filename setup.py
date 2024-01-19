

# from distutils.command.install import install
import os
from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools.command.sdist import sdist

# from grpc_tools import protoc

# from fix_protobuf_imports import fix_protobuf_imports

class my_sdist(sdist):
    def run(self) -> None:
        cwd = os.getcwd()
        os.chdir(cwd + "/protos")
        os.chdir(cwd)
        sdist.run(self)

class my_install(install):
    def run(self):
        cwd = os.getcwd()
        os.chdir(cwd + "/protos")
        os.chdir(cwd)
        install.run(self)

setup(name='orchestrator_utils',
version='0.2',
description='OMuProCU Utility Package',
url='#',
author='Timo Geier',
author_email='timo.geier@cs.hs-fulda.de',
license='MIT',
install_requires= [line.strip() for line in open("requirements.txt", "r").readlines()],
packages=find_packages() + find_packages(where='src', exclude=[]),
package_dir={'': 'src'},
cmdclass=dict(install=my_install, sdist=my_sdist),
zip_safe=False)