from setuptools import setup, find_packages

setup(
    name='isofits',
    version='0.1.0',
    author='Parker Greene',
    author_email='parkergreene16@gmail.com',
    description='Python module for calculating hole/shaft tolerances per ISO 286-1',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)