# setup.py

from setuptools import setup, find_packages

setup(
    name="meu_pacote_exemplo",
    version="0.1.0",
    author="Seu Nome",
    description="Um pacote de exemplo para o exercício da DIO.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)