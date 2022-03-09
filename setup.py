# -*- coding: utf-8 -*-

# Learn more: https://github.com/mzahana/ZLAC8030L_CAN_controller.git
# Reference for Python package structuring (https://www.pythonforthelab.com/blog/how-create-setup-file-your-project/)

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ZLAC8030L_CAN_controller',
    version='0.1.0',
    description='A Python package for CANopen communication with the ZLAC8030L motor driver.',
    long_description=readme,
    author='Mohamed Abdelkader',
    author_email='mohamedashraf123@gmail.com',
    url='https://github.com/mzahana/ZLAC8030L_CAN_controller.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'zlac8030l_speed_test=tests.speed_test:main',
        ]
    },
    install_requires=[
        "canopen==1.2.0",
        "python-can==3.0.0",
        "wrapt==1.10.11",
        "setuptools==39.2.0"
    ]
)