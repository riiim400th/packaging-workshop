from setuptools import setup

setup(
    name='hello_package',
    version='1.0',
    packages=['hello'],
    entry_points={
        'console_scripts': [
            'hello = hello.hello:say_hello'
        ]
    }
)
