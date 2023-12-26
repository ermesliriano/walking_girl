from setuptools import setup

setup(
    name='walking-girl',
    version='0.1.0',
    packages=['walking_girl'],
    install_requires=["pygame","importlib"],
    entry_points={
        'console_scripts': [
            'walking-girl = walking_girl.__main__:main'
        ]
    },
)
