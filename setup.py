from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import codecs 
import os

VERSION = '1.0.1'

class CustomInstall(install):
    def run(self):
        subprocess.check_call("bash setup.sh", shell=True)
        install.run(self)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

DESCRIPTION = 'A voice assistant for Termux written in python using termux-api and g4f'

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()
    
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
    install_requires=requirements,
    cmdclass={'install': CustomInstall},
    keywords=[
        'python',
        'voice assistant',
        'termux',
        'termux-api',
        'g4f',
        'android',
    ],  
    url='https://github.com/ayusc/termux-sriparna',
    project_urls={
        'Source Code': 'https://github.com/ayusc/termux-sriparna',  
        'Bug Tracker': 'https://github.com/ayusc/termux-sriparna/issues', 
        'Feature Requests': 'https://github.com/ayusc/termux-sriparna/issues/1'
    },
    entry_points={
        'console_scripts': [
            'sriparna = sriparna.sriparna:main'
        ]
    }
)
