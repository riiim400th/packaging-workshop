from setuptools import setup, find_packages

setup(
    name='hotel',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hotel = hotel.main_mod:main'
        ]
    },
)
