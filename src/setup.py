from setuptools import setup, find_packages

setup(
    name='magnets',  
    version='1.0.0',  
    packages=find_packages(),  
    install_requires=['flask', 'mongoengine', 'click'],
    entry_points={
        'console_scripts': [
            'magnets = magnets.cli:cli',
        ],
    },
)
