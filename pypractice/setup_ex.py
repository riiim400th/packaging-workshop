from setuptools import setup
import os

def strip_comments(l):
    return l.split('#',1)[0].strip()

def reqs(*f):
    with open(os.path.join(getcwd(),*f),encoding="utf-8") as f:
        return [strip_comments(l) for l in f]

setup(
    name='hello_package',
    version='1.0',
    packages=['hello'],
    entry_points={
        'console_scripts': [
            'hello = hello.hello:say_hello'
        ]
    }
    
    install_requires=reqs('requirements.txt')
)