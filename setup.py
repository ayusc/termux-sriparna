from setuptools import setup, find_packages
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg
import codecs 
import os

VERSION = '1.0.4'

# https://stackoverflow.com/questions/21915469/python-setuptools-install-requires-is-ignored-when-overriding-cmdclass
class bdist_egg(_bdist_egg):
    def run(self):
        os.system("bash setup.sh")
        _bdist_egg.run(self)

DESCRIPTION = 'A voice assistant for Termux written in python using Termux Api'

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
    cmdclass={'bdist_egg': bdist_egg},
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
