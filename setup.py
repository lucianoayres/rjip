from setuptools import setup, find_packages

setup(
    name='rjip',
    version='1.0.0',
    packages=find_packages(),
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'coverage',
        ]
    },
    entry_points={
        'console_scripts': [
            'rjip = main:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
