from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import codecs 
import os

VERSION = '1.0.5'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

DESCRIPTION = 'A voice assistant for Termux written in python using Termux Api'

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

class PostInstall(install):
    def run(self):
        os.system("bash setup.sh")
        install.run(self)
        
setup(
    name='termux-sriparna',
    version=VERSION, 
    author="Ayus Chatterjee",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'sriparna': ['apps.json']},
    include_package_data=True,
    cmdclass={'install': PostInstall},
    install_requires=requirements,
    keywords=[
        'python',
        'voice assistant',
        'termux',
        'termux-api',
        'g4f',
    ],  
    url='https://github.com/ayusc/termux-sriparna',
    project_urls={
        'Source Code': 'https://github.com/ayusc/termux-sriparna',  
        'Bug Tracker': 'https://github.com/ayusc/termux-sriparna/issues', 
        'Feature Requests': 'https://github.com/ayusc/termux-sriparna/issues/1'
    },
    entry_points={
        'console_scripts': [
            'sriparna = sriparna.sriparna:main',
            'sriparna-gui = sriparna.sriparna_gui:main', 
        ]
    }
)
