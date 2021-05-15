# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython simulador orbitas planetarias

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = [
    Extension('cy_simulator',
              ['cy_simulator.pyx'],
              libraries=['m'],
              extra_compile_args=['-ffast-math',
                                  '-fopenmp', '-march=native'],
              extra_link_args=['-fopenmp']
              )]

setup(
    name='cy_simulator',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)