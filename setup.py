from setuptools import setup, find_packages

setup(
    name='matrix_pichain',
    version='0.1.0',
    author='KOSASIH',
    author_email='kosasihg88@gmail.com',
    description='A high-tech cryptocurrency platform based on blockchain technology.',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'requests==2.26.0',
        'web3==5.24.0',
        'pycryptodome==3.10.1',
        'pytest==6.2.5',
        'pylint==2.11.1',
        'sqlalchemy==1.4.22',
    ],
    entry_points={
        'console_scripts': [
            'matrix-pichain=src.main:main',  # Adjust the entry point as needed
        ],
    },
)
