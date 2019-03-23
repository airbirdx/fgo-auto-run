# encoding: utf-8
from setuptools import setup
import os, sys, shutil, platform

requirements = [
    'pillow',
    'openpyxl',
    'opencv-python',
    'numpy',
    'pangu'
]

if platform.system() == 'Windows':
    requirements.append('win10toast')
elif platform.system() == 'Darwin':
    pass

long_description = """
A python + adb semi-auto script for FGO.
"""

setup(
    name='fgo-auto-run',
    version='0.1',
    # packages=['fgo-auto-run'],
    description='fgo-auto-run',
    long_description=long_description,
    author='airbirdx',
    install_requires=requirements,
)

shutil.rmtree('./build')    #递归删除文件夹
shutil.rmtree('./dist')    #递归删除文件夹
shutil.rmtree('./fgo_auto_run.egg-info')    #递归删除文件夹