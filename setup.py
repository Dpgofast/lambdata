#!/user/bin/env python
''' Package setup/ installation and metadata for lambdata'''

import setuptools

REQUIRED = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn'
]
with open('README.MD', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='lambdata-dpgofast',
    version='0.0.6',
    author='Dpgofast',
    description=' A collection of Data Science helper functions',
    long_description=LONG_DESCRIPTION,
    long_descrition_content_type='text/markdown',
    url='https://github.com/Dpgofast/lambdata',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        ]
)
