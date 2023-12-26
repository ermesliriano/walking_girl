from setuptools import setup

setup(
    name='moving-girl',
    version='0.0.1',
    packages=["moving-girl"],
    description='A girl that walks from one side to another',
    author='Ermes Liriano',
    author_email='ermes_jr@hotmail.com',
    install_requires=["pygame"],
    entry_points={
        "console_scripts": ["moving-girl = moving-girl.__main__:main"]
    }
)
